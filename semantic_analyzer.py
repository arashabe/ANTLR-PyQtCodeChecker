from generated.LanguageParser import LanguageParser
from generated.LanguageVisitor import LanguageVisitor


class SemanticAnalyzer(LanguageVisitor):
    """
    This class extends LanguageVisitor and is responsible for performing semantic analysis on a parsed input.
    It checks for various semantic errors, such as undeclared variables, type compatibility, and method declarations.
    It maintains state information about declared variables and methods within the current class context.
    """

    def __init__(self):
        super().__init__()
        self.errors = []
        self.declared_vars = {}  # Variables with associated types
        self.class_methods = {}  # Methods declared for each class
        self.predefined_methods = {"System.out.println"}  # Predefined methods
        self.current_class = None  # Current class
        self.valid_data_types = {"int", "float", "double", "boolean", "char", "String"}  # Valid data types

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):
        """
        This method visits a variable declaration node in the parse tree.
        It checks for the validity of the data type and ensures the variable is not already declared.
        It also verifies type compatibility between the declared variable and any assigned expression.
        If any semantic errors are found, they are added to the errors list.
        """

        # Get the line number from the context
        if ctx.start:
            line_number = ctx.start.line
        else:
            line_number = "unknown"

        if ctx.ID() is None:
            self.errors.append("Error at line {line_number}: Declaration without an identifier.")
            return None

        var_name = ctx.ID().getText()
        data_type = ctx.data_type().getText() if ctx.data_type() else None

        # Check if the data type is valid
        if data_type and data_type not in self.valid_data_types:
            self.errors.append(f"Error at line {line_number}: Invalid data type '{data_type}' for variable '{var_name}'.")

        if var_name in self.declared_vars:
            self.errors.append(f"Error at line {line_number}: Variable '{var_name}' already declared.")
        else:
            self.declared_vars[var_name] = data_type  # Associate the type with the variable

        # Check that the variable type is compatible with the assigned expression
        if ctx.expr():
            expr_type = self.get_expression_type(ctx.expr())
            if expr_type and not self.is_type_compatible(data_type, expr_type):
                self.errors.append(
                    f"Error at line {line_number}: Incompatible type '{expr_type}' with declaration '{data_type}' for variable '{var_name}'.")

        return self.visitChildren(ctx)

    def is_type_compatible(self, var_type, expr_type):
        """
        This method checks if the expression type (expr_type) is compatible with the variable type (var_type).
        It first ensures that the expression type is not None.
        Then it checks if the variable type and expression type are identical.
        Additionally, it allows permissible conversions, such as from 'int' to 'float'.
        If the types are not compatible, it returns False, indicating a type mismatch.
        """

        # No deduced type, error
        if expr_type is None:
            return False
        # Types must be identical
        if var_type == expr_type:
            return True
        # Allow permissible conversions (e.g., int -> float)
        if var_type == "float" and expr_type == "int":
            return True
        # No other conversions are allowed
        return False

    def visitAssignment(self, ctx: LanguageParser.AssignmentContext):
        """
        This method visits an assignment node in the parse tree.
        It verifies that the variable being assigned to has been declared.
        It also checks that the type of the expression being assigned is compatible with the type of the variable.
        If any semantic errors are found, such as using an undeclared variable or type mismatches, they are added to the errors list.
        """
        # Get the line number from the context
        if ctx.start:
            line_number = ctx.start.line
        else:
            line_number = "unknown"

        var_name = ctx.ID().getText()

        if var_name not in self.declared_vars:
            self.errors.append(f"Error at line {line_number}: Variable '{var_name}' used without declaration.")
            return None

        var_type = self.declared_vars[var_name]
        expr_type = self.get_expression_type(ctx.expr())

        if not self.is_type_compatible(var_type, expr_type):
            self.errors.append(f"Error at line {line_number}: Assignment of type '{expr_type}' to variable of type '{var_type}'.")

        return self.visitChildren(ctx)

    def visitMethod_declaration(self, ctx: LanguageParser.Method_declarationContext):
        """
        This method visits a method declaration node in the parse tree.
        It checks for the presence of a method name and adds the method to the current class.
        The method parameters are added to the list of declared variables for type checking within the method.
        It saves the current state of declared variables before visiting the method body to ensure scope isolation.
        After processing the method body, it restores the previous state of declared variables.
        Any semantic errors, such as undeclared parameters or duplicate method declarations, are added to the errors list.
        """
        # Get the line number from the context
        if ctx.start:
            line_number = ctx.start.line
        else:
            line_number = "unknown"

        if ctx.ID() is None:
            self.errors.append(f"Error at line {line_number}: Method without a name.")
            return None

        method_name = ctx.ID().getText()

        # Add the method to the current class
        if self.current_class:
            if self.current_class not in self.class_methods:
                self.class_methods[self.current_class] = set()
            self.class_methods[self.current_class].add(method_name)

        # Save the current state of declared variables
        previous_declared_vars = dict(self.declared_vars)

        # Add method parameters to declared variables
        if ctx.param_list() is not None:
            for param in ctx.param_list().param():
                if param.ID() is None:
                    self.errors.append(f"Error at line {line_number}: Parameter without an identifier.")
                else:
                    param_name = param.ID().getText()
                    param_type = param.data_type().getText() if param.data_type() else None
                    self.declared_vars[param_name] = param_type  # Associate the type with the parameter

        # Visit the method body and verify variable usage
        self.visit(ctx.block())

        # Restore the previous state of declared variables
        self.declared_vars = previous_declared_vars

        return None

    def visitMethod_call(self, ctx: LanguageParser.Method_callContext):
        """
        This method visits a method call node in the parse tree.
        It extracts the full method name and checks if it is a valid predefined method, such as those in System.out.
        For methods within the current class, it verifies that the method has been declared.
        If the method is not recognized or declared, a semantic error is added to the errors list.
        """
        # Get the line number from the context
        if ctx.start:
            line_number = ctx.start.line
        else:
            line_number = "unknown"

        # Get the full method name (e.g., example.countNumbers)
        method_name = ctx.qualified_name().getText()
        method_name_parts = method_name.split('.')
        method_name = method_name_parts[-1]

        # Check if it is a System.out method (predefined)
        if len(method_name_parts) > 1 and method_name_parts[0] == "System" and method_name_parts[1] == "out":
            valid_methods = {"println", "print", "readLine", "nextInt"}  # Add other valid methods if necessary
            if method_name not in valid_methods:
                self.errors.append(
                    f"Error at line {line_number}: Method '{method_name}' called on 'System.out' is not recognized as valid."
                )
            return self.visitChildren(ctx)

        # Now check methods in the current class
        if self.current_class:
            # Get the methods declared in the current class
            declared_methods = self.class_methods.get(self.current_class, set())
            # Check if the method is declared in the current class
            if method_name not in declared_methods:
                self.errors.append(
                    f"Error at line {line_number}: Method '{method_name}' called without being declared in class '{self.current_class}'."
                )
        else:
            self.errors.append(f"Error at line {line_number}: Method '{method_name}' called outside of a class.")

        return self.visitChildren(ctx)

    def visitClass_declaration(self, ctx: LanguageParser.Class_declarationContext):
        """
        This method visits a class declaration node in the parse tree.
        It checks for the presence of a class name and ensures it is not already declared as a variable or another class.
        If the class name is valid, it adds the class to the list of declared variables and valid data types.
        It sets the current class context and initializes the method list for the class.
        The method then visits all children of the class to process method declarations and other class members.
        Finally, it restores the previous class context after visiting the class declaration.
        Any semantic errors, such as duplicate class names or methods, are added to the errors list.
        """
        # Get the line number from the context
        if ctx.start:
            line_number = ctx.start.line
        else:
            line_number = "unknown"

        if ctx.ID() is None:
            self.errors.append(f"Error at line {line_number}: Class without a name.")
            return None

        class_name = ctx.ID().getText()

        # Avoid conflicts with already declared variables or classes
        if class_name in self.declared_vars or class_name in self.valid_data_types:
            self.errors.append(f"Error at line {line_number}: Class '{class_name}' already declared.")
        else:
            self.declared_vars[class_name] = "class"  # Add the class name
            self.valid_data_types.add(class_name)

        # Set the current class
        previous_class = self.current_class
        self.current_class = class_name

        # Initialize the methods of the class
        if class_name not in self.class_methods:
            self.class_methods[class_name] = set()

        # Add the methods of the current class to the list
        for child in ctx.children:
            if isinstance(child, LanguageParser.Method_declarationContext):
                method_name = child.ID().getText()
                if method_name in self.class_methods[class_name]:
                    self.errors.append(f"Error at line {line_number}: Method '{method_name}' already declared in class '{class_name}'.")
                else:
                    self.class_methods[class_name].add(method_name)

        # Visit all children of the class
        self.visitChildren(ctx)

        # Restore the previous class
        self.current_class = previous_class
        return None

    def visitFor_loop(self, ctx: LanguageParser.For_loopContext):
        """
        This method visits a for loop node in the parse tree.
        It visits the initialization, condition, and increment expressions of the for loop.
        It also visits the block of code that represents the body of the loop.
        This ensures that all parts of the for loop are semantically analyzed.
        """

        # Visit the declarations, conditions, and increments of the loop
        self.visitChildren(ctx)
        return None

    def visitWhile_loop(self, ctx: LanguageParser.While_loopContext):
        """
        This method visits a while loop node in the parse tree.
        It visits the condition expression of the while loop.
        It also visits the block of code that represents the body of the loop.
        This ensures that the condition and the body of the while loop are semantically analyzed.
        """

        # Visit the loop condition
        self.visitChildren(ctx)
        return None

    def visitTerm(self, ctx: LanguageParser.TermContext):
        """
        This method visits a term node in the parse tree.
        If the term is an identifier (ID), it checks whether the variable has been declared.
        If the variable is undeclared, a semantic error is added to the errors list.
        It ensures that terms used in expressions are valid and declared.
        """
        # Get the line number from the context
        if ctx.start:
            line_number = ctx.start.line
        else:
            line_number = "unknown"

        # If the term is an ID (a variable)
        if ctx.ID() is not None:
            var_name = ctx.ID().getText()
            if var_name not in self.declared_vars:
                self.errors.append(f"Error at line {line_number}: Variable '{var_name}' used without declaration.")
        return self.visitChildren(ctx)

    def get_expression_type(self, expr_ctx):
        """
        This method determines the type of an expression in the parse tree.
        It checks if the expression is a boolean, integer, float, string, or a declared variable.
        If the expression is an object creation, it retrieves the type of the created object.
        The method returns the detected type of the expression or None if the type cannot be determined.
        """

        # Get the text of the expression
        text = expr_ctx.getText()

        # Check if the text is a boolean value
        if text == "true" or text == "false":
            return "boolean"

        # Check if it is an integer
        if text.isdigit():
            return "int"

        # Check if it is a floating-point number
        try:
            float(text)
            if '.' in text or text.lower().endswith('f'):
                return "float"
        except ValueError:
            pass

        # Check if it is a string
        if text.startswith('"') and text.endswith('"'):
            return "String"

        # If it is a variable (ID), look it up in the list of declared variables
        if text in self.declared_vars:
            return self.declared_vars[text]  # Return the type of the declared variable

        # Check if it is an object creation (e.g., `new Type()`)
        if hasattr(expr_ctx, 'object_creation') and expr_ctx.object_creation() is not None:
            return expr_ctx.object_creation().qualified_name().getText()

        return None
