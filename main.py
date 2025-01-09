import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
                             QToolBar, QAction, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QTextCursor, QColor, QTextCharFormat
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from generated.LanguageLexer import LanguageLexer
from generated.LanguageParser import LanguageParser
from semantic_analyzer import SemanticAnalyzer


class CustomErrorMessage:
    # Provides utility methods for transforming default error messages into more readable and user-friendly text.
    @staticmethod
    def transform(msg, offending_symbol):
        # Transforms specific parser error messages into clearer explanations.
        # like unexpected end of input and incomplete statements.
        if "mismatched input '<EOF>'" in msg:
            if offending_symbol.text == "<EOF>":
                return "Unexpected end of input: check for missing or incomplete statements."
            return f"Error near '{offending_symbol.text}'"
        if "no viable alternative at input" in msg:
            if offending_symbol.text == "<EOF>":
                return "Incomplete statement or missing input at the end of the code."
            return f"Error near '{offending_symbol.text}'"
        return msg


class CodeAnalyzerGUI(QMainWindow):
    # Main GUI class for the code analyzer application.
    # Provides a text editor for writing code, an output console for displaying errors,
    # and tools for analyzing and interacting with the input code.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BugBuster")
        self.setGeometry(100, 100, 800, 600)
        self.error_lines = {}
        self.initUI()

    def initUI(self):
        # Initializes the user interface elements, including the code editor,
        # output console, toolbar, and layout.
        # Sets up actions like running analysis, cleaning input, and exiting the application.

        # Text area to input code
        self.code_input = QTextEdit(self)
        self.code_input.setPlaceholderText("Write code here...")

        # Output console for errors
        self.output_console = QTextEdit(self)
        self.output_console.setReadOnly(True)
        self.output_console.setPlaceholderText("Output console...")
        self.output_console.mousePressEvent = self.handle_output_click

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.code_input, stretch=3)
        layout.addWidget(self.output_console, stretch=1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # Run button
        self.run_action = QAction(QIcon("images/bug.png"), "", self)
        self.run_action.setEnabled(False)
        self.run_action.triggered.connect(self.run_analysis)
        self.run_action.setToolTip("Debug")
        toolbar.addAction(self.run_action)

        # Clean button
        clean_action = QAction(QIcon("images/broom.png"), "", self)
        clean_action.triggered.connect(self.clean_text)
        clean_action.setToolTip("Clean")
        toolbar.addAction(clean_action)

        # Info button
        info_action = QAction(QIcon("images/info.png"), "", self)
        info_action.triggered.connect(self.show_info)
        info_action.setToolTip("Info")
        toolbar.addAction(info_action)

        # Exit button
        exit_action = QAction(QIcon("images/power-off.png"), "", self)
        exit_action.triggered.connect(self.confirm_exit)
        exit_action.setToolTip("Exit")
        toolbar.addAction(exit_action)

        self.code_input.textChanged.connect(self.check_text)

        self.apply_stylesheet()

    def check_text(self):
        if self.code_input.toPlainText().strip():
            self.run_action.setEnabled(True)
        else:
            self.run_action.setEnabled(False)

    def apply_stylesheet(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #3f4240; }
            QToolBar QToolButton { margin: 2px; padding: 5px; color: white; font-size: 18px; }
            QToolBar QToolButton:hover { background-color: #161716; color: white; }
            QTextEdit { background-color: #202420; border: 1px solid #055405; color: white; font-family: Consolas, monaco, monospace; font-size: 18px; }
            QTextEdit[readOnly="true"] { background-color: #202420; border: 1px solid #055405; color: white; font-family: Consolas, monaco, monospace; font-size: 14px; }
        """)

    def run_analysis(self):
        # Performs lexical, syntactic, and semantic analysis on the user's code.
        # Collects errors from each phase of analysis and displays them in the output console.
        try:
            input_code = self.code_input.toPlainText()
            input_stream = InputStream(input_code)
            lexer = LanguageLexer(input_stream)
            lexer_errors = []

            class LexerErrorListener(ErrorListener):
                # Custom error listener for the parser to capture and format syntax errors.
                # Overrides the default error handling mechanism to provide more user-friendly messages.
                def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                    lexer_errors.append((line, f"Error at line {line}, column {column}: {msg}"))

            lexer.removeErrorListeners()
            lexer.addErrorListener(LexerErrorListener())
            token_stream = CommonTokenStream(lexer)
            token_stream.fill()

            for token in token_stream.tokens:
                if token.type == lexer.UNKNOWN:
                    lexer_errors.append(
                        (token.line, f"Error at line {token.line}, column {token.column}: unrecognized symbol '{token.text}'")
                    )

            parser = LanguageParser(token_stream)
            parser_errors = []

            class ParserErrorListener(ErrorListener):
                def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                    msg = CustomErrorMessage.transform(msg, offendingSymbol)

                    if "'<EOF>'" in msg:
                        msg = msg.replace(" at '<EOF>'", "")
                    parser_errors.append((line, f"Error at line {line}, column {column},  {msg}"))

            parser.removeErrorListeners()
            parser.addErrorListener(ParserErrorListener())
            tree = parser.start_()

            semantic_analyzer = SemanticAnalyzer()
            semantic_analyzer.visit(tree)

            all_errors = lexer_errors + parser_errors + [(line, err) for err in semantic_analyzer.errors for line in [int(err.split()[3][:-1])]]
            all_errors.sort(key=lambda x: x[0])

            self.error_lines = {}
            if all_errors:
                self.output_console.clear()
                for line, message in all_errors:
                    self.error_lines[message] = line
                    self.output_console.append(message)
            else:
                self.output_console.setPlainText("No errors found!")

        except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")

    def handle_output_click(self, event):
        # Handles user clicks on the output console.
        # Checks if the clicked error message corresponds to a specific line number
        # and highlights that line in the code editor.
        cursor = self.output_console.cursorForPosition(event.pos())
        cursor.select(QTextCursor.LineUnderCursor)
        clicked_text = cursor.selectedText()

        if clicked_text in self.error_lines:
            line_number = self.error_lines[clicked_text]
            self.highlight_line(line_number)

    def highlight_line(self, line_number):
        # Highlights the specified line in the code editor.
        # Moves the cursor to the given line and sets focus on the editor for clarity.
        cursor = self.code_input.textCursor()
        cursor.movePosition(QTextCursor.Start)
        for _ in range(line_number - 1):
            cursor.movePosition(QTextCursor.Down)
        extra_selection = QTextEdit.ExtraSelection()
        line_color = QColor("#383631")
        extra_selection.format.setBackground(line_color)
        extra_selection.format.setProperty(QTextCharFormat.FullWidthSelection, True)
        extra_selection.cursor = cursor
        self.code_input.setExtraSelections([extra_selection])
        self.code_input.setTextCursor(cursor)
        self.code_input.setFocus()

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message, QMessageBox.Ok)

    def clean_text(self):
        self.code_input.clear()
        self.output_console.clear()

    def show_info(self):
        info_text = (
            "BugBuster\n"
            "Version: 1.0\n"
            "Author: Arash Abedi\n"
            "Release Year: 2024\n"
            "This application analyzes code for lexical, syntactic, and semantic errors."
        )
        QMessageBox.information(self, "Information", info_text)

    def confirm_exit(self):
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CodeAnalyzerGUI()
    logo_pixmap = QPixmap("images/logo.png")
    logo_pixmap = logo_pixmap.scaled(64, 64, aspectRatioMode=Qt.KeepAspectRatio)
    app.setWindowIcon(QIcon(logo_pixmap))
    window.show()
    sys.exit(app.exec_())
