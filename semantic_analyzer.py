# semantic_analyzer.py
from generated.LanguageParser import LanguageParser
from generated.LanguageVisitor import LanguageVisitor


class SemanticAnalyzer(LanguageVisitor):
    def __init__(self):
        super().__init__()
        self.errors = []
        # Tenere traccia delle variabili dichiarate
        self.declared_vars = set()

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):
        var_name = ctx.ID().getText()

        # Verificare se la variabile è già dichiarata
        if var_name in self.declared_vars:
            self.errors.append(f"Errore: Variabile '{var_name}' già dichiarata.")
        else:
            self.declared_vars.add(var_name)  # Aggiungere la variabile dichiarata

        return self.visitChildren(ctx)  # Visitare eventuali nodi figli

    def visitExpression(self, ctx: LanguageParser.ExpressionContext):
        var_name = ctx.ID().getText()

        # Verificare se la variabile è stata dichiarata prima di essere usata
        if var_name not in self.declared_vars:
            self.errors.append(f"Errore: Variabile '{var_name}' usata senza dichiarazione.")

        return self.visitChildren(ctx)  # Visitare eventuali nodi figli
