# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from semantic_analyzer import SemanticAnalyzer
from generated.LanguageLexer import LanguageLexer
from generated.LanguageParser import LanguageParser
from antlr4 import InputStream, CommonTokenStream

class CodeAnalyzerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Analizzatore di Codice")
        self.setGeometry(100, 100, 800, 600)

        # Area di testo per inserire il codice
        self.code_input = QTextEdit(self)
        self.code_input.setPlaceholderText("Scrivi il codice qui...")

        # Console di output per gli errori
        self.output_console = QTextEdit(self)
        self.output_console.setReadOnly(True)
        self.output_console.setPlaceholderText("Console di output...")

        # Pulsante "Run" per eseguire l'analisi
        self.run_button = QPushButton("Run", self)
        self.run_button.clicked.connect(self.run_analysis)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.code_input)
        layout.addWidget(self.run_button)
        layout.addWidget(self.output_console)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def run_analysis(self):
        # Ottiene il codice dall’area di testo
        input_code = self.code_input.toPlainText()

        # Usare ANTLR per tokenizzare e parsare
        input_stream = InputStream(input_code)
        lexer = LanguageLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = LanguageParser(token_stream)

        # Parsing e ottenimento dell’albero sintattico
        tree = parser.start_()

        # Verificare se ci sono errori di parsing
        if parser.getNumberOfSyntaxErrors() > 0:
            self.output_console.setPlainText("Errori di sintassi rilevati.")
            return

        # Se nessun errore, continuo con l'analisi semantica
        # Qui dovrei passare `tree` a `SemanticAnalyzer` per l'analisi semantica
        # Se nessun errore, continuo con l'analisi semantica
        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.visit(tree)  # Usare il visitor per analizzare l’albero

        if semantic_analyzer.errors:
            self.output_console.setPlainText("\n".join(semantic_analyzer.errors))
        else:
            self.output_console.setPlainText("Nessun errore trovato!")


app = QApplication(sys.argv)
window = CodeAnalyzerGUI()
window.show()
sys.exit(app.exec_())
