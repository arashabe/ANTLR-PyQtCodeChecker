import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
                             QToolBar, QAction, QMessageBox)

from PyQt5.QtCore import Qt
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from generated.LanguageLexer import LanguageLexer
from generated.LanguageParser import LanguageParser
from semantic_analyzer import SemanticAnalyzer
from PyQt5.QtGui import QIcon, QPixmap


class CustomErrorMessage:
    @staticmethod
    def transform(msg, offending_symbol):
        # Transforms the default error message into something more readable
        if "no viable alternative at input" in msg:
            return f"Error near '{offending_symbol.text}'"
        return msg


class CodeAnalyzerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BugBuster")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Text area to input code
        self.code_input = QTextEdit(self)
        self.code_input.setPlaceholderText("Write code here...")

        # Output console for errors
        self.output_console = QTextEdit(self)
        self.output_console.setReadOnly(True)
        self.output_console.setPlaceholderText("Output console...")

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
        # Check if the text area is not empty
        if self.code_input.toPlainText().strip():
            self.run_action.setEnabled(True)
        else:
            self.run_action.setEnabled(False)

    def apply_stylesheet(self):
        self.setStyleSheet("""
            /* Set background color for the entire window */
        QMainWindow {
            background-color: #3f4240;  
        }
            QToolBar QToolButton {
                /*background-color: lightgreen;*/
                /*border: 1px solid white; */
                margin: 2px; 
                padding: 5px;
                color: white;
                font-size: 18px;
            }
            QToolBar QToolButton:hover {
                background-color: #161716;
                color: white;
            }

        /* Settings for the code editor */
        QTextEdit {
            background-color: #202420;
            border: 1px solid #055405;
            color: white;
            font-family: Consolas, monaco, monospace;
            font-size: 18px;
        }

        /* Settings for the error console */
        QTextEdit[readOnly="true"] {
            background-color: #202420;
            border: 1px solid #055405;
            color: white;
            font-family: Consolas, monaco, monospace;
            font-size: 14px;
        }
        """)

    def run_analysis(self):
        try:
            # Get the code from the text area
            input_code = self.code_input.toPlainText()

            # ANTLR for tokenizing
            input_stream = InputStream(input_code)
            lexer = LanguageLexer(input_stream)

            # Listener for lexical errors
            lexer_errors = []

            class LexerErrorListener(ErrorListener):
                def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                    lexer_errors.append((line, f"Error at line {line}, column {column}: {msg}"))

            lexer.removeErrorListeners()
            lexer.addErrorListener(LexerErrorListener())

            # Generate token stream
            token_stream = CommonTokenStream(lexer)
            token_stream.fill()  # Force token population

            # Manual check for UNKNOWN tokens
            for token in token_stream.tokens:
                if token.type == lexer.UNKNOWN:
                    lexer_errors.append(
                        (token.line,
                         f"Error at line {token.line}, column {token.column}: unrecognized symbol '{token.text}'")
                    )

            # Parsing and getting the parse tree
            parser = LanguageParser(token_stream)

            # Custom listener for syntactic errors
            parser_errors = []

            class ParserErrorListener(ErrorListener):
                def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                    # Use CustomErrorMessage class to transform the error message
                    msg = CustomErrorMessage.transform(msg, offendingSymbol)

                    if "at '<EOF>'" in msg:
                        msg = msg.replace(" at '<EOF>'", "")
                    parser_errors.append((line, f"Error at line {line}, column {column}: {msg}"))

            parser.removeErrorListeners()
            parser.addErrorListener(ParserErrorListener())

            tree = parser.start_()

            # Semantic analysis
            semantic_analyzer = SemanticAnalyzer()
            semantic_analyzer.visit(tree)

            # Combine lexical, syntactic, and semantic errors
            all_errors = lexer_errors + parser_errors + [(line, err) for err in semantic_analyzer.errors for line in
                                                         [int(err.split()[3][:-1])]]

            # Sort errors by line number
            all_errors.sort(key=lambda x: x[0])

            if all_errors:
                self.output_console.setPlainText("Errors found:\n" + "\n".join([error[1] for error in all_errors]))
            else:
                self.output_console.setPlainText("No errors found!")

        except Exception as e:
            self.show_error_message(f"An error occurred: {str(e)}")

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
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
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
