grammar Language;

// Start rule for the grammar; it consists of one or more statements
start_: statement+ ;

statement: declaration ';'              // Variable declaration
         | expression ';'               // Any expression
         | method_declaration           // Method declaration
         | main_method_declaration      // Main method declaration
         | class_declaration            // Class declaration
         | loop                         // Loop (for, while, etc.)
         | block                        // Block of code
         | return_statement ';'         // Return statement
         | if_statement                 // If statement
         ;

block: '{' statement* '}' ;
// Example:
// {
// int a = 5;
// System.out.println(a);
// }


// Variable declarations
// int number = 10;
declaration: visibility_specifier? 'static'? data_type ID ('=' expr)? ;


// Data types that can be used in declarations
// int, float, double, boolean, char, String, MyClass
data_type: 'int' | 'float' | 'double' | 'boolean' | 'char' | 'String' | qualified_name ;

// Expressions
expression: assignment
          | method_call
          | increment_expr
          | assignment_expr
          | object_creation
          | 'this' '.' ID
          ;
// Example:
// assignment: number = 20;
// method_call: printMessage("Hello");
// increment_expr: number++;
// assignment_expr: number += 5;
// object_creation: MyClass obj = new MyClass();
// 'this' '.' ID: this.number


// Assignment expressions
assignment: ID '=' expr
          | object_creation
          | 'this' '.' ID '=' expr
          ;
// Example:
// ID '=' expr: number = 20;
// object_creation: MyClass obj = new MyClass();
// 'this' '.' ID '=' expr: this.number = 30;




// Object creation expression
object_creation: 'new' qualified_name '(' arg_list? ')' ;
// Example:
// MyClass obj = new MyClass();



// Increment expressions
increment_expr: ID '++' | ID '--' ;
// Example:
// number++


// Assignment expressions
assignment_expr: ID ('+=' | '-=' | '*=' | '/=') expr ;
// Example:
// number += 5
// number -= 3



// Return statement
return_statement: 'return' expr ;
// Example:
// return 42;


// If statements
if_statement: 'if' '(' expr ')' block ( 'else' block )? ;
// Example:
// if (x > 10) {
//     System.out.println("x is greater than 10");
// } else {
//     System.out.println("x is not greater than 10");
// }


// Method calls
method_call: qualified_name '(' arg_list? ')' ;
// Example:
// myObject.myMethod(arg1, arg2);

qualified_name: ID ('.' ID)* ;
// Example:
// java.util.ArrayList

arg_list: expr (',' expr)* ;
// Example:
// (arg1, arg2, arg3)



// Main method declaration
main_method_declaration: 'public' 'static' 'void' 'main' '(' 'String' '[]' 'args' ')' block ;
// Example:
// public static void main(String[] args) {
//     // code
// }


// Method declarations
method_declaration: visibility_specifier? 'static'? return_type? ID '(' param_list? ')' block ;
// Example:
// public void myMethod(int param) {
//     // Method body
// }


// Visibility specifiers
visibility_specifier: 'public' | 'private' | 'protected' ;
// Example:
// public, private, protected


// Return types
return_type: 'void' | data_type ;
// Example:
// void, int, String


// Parameter list
param_list: param (',' param)* ;
// Example:
// (int param1, String param2)

// Parameter definition
param: data_type ID ;


// Class declaration
class_declaration: visibility_specifier? 'static'? 'class' ID '{' class_body '}' ;
// Example:
// public class MyClass {
//     // Class body
// }


// Class body
class_body: (declaration ';' | method_declaration | main_method_declaration | class_declaration)* ;
// Example:
// public class MyClass {
//     int number;
//     public void myMethod() {
//         // Method body
//     }
//     public static void main(String[] args) {
//         // Main body
//     }
//     public class InnerClass {
//         // Inner class body
//     }
// }



// Loops
loop: for_loop | while_loop ;
// Example:
// for_loop: for (int i = 0; i < 10; i++) {
//               // loop body
//           }


// For loop
for_loop: 'for' '(' (declaration | expression | increment_expr)? ';' expr? ';' (expression | increment_expr)? ')' block ;
// Example:
// for (int i = 0; i < 10; i++) {
//     System.out.println(i);
// }


// While loop
while_loop: 'while' '(' expr ')' block ;
// Example:
// while (x < 5) {
//     x++;
// }



// Expressions and terms
expr: expr ('*' | '/' | '%') expr
    | expr ('+' | '-') expr
    | expr ('<' | '<=' | '>' | '>=') expr
    | expr ('==' | '!=') expr
    | expr ('&&' | '||') expr
    | term
    ;
// Example:
// true || false
// 5 != 6

term
    : method_call
    | ID
    | NUMBER
    | '(' expr ')'
    | STRING_LITERAL
    | BOOLEAN_LITERAL
    | 'true'
    | 'false'
    | ('!' expr)
    | object_creation
    | 'this'
    ;

// Example:
// myObject.myMethod();
// "Hi"
// (x + y)
// true


// Lexical tokens
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
// Example:
// variableName, myClass, _temp

// Numbers, including integer and floating-point literals
NUMBER: [0-9]+('.'[0-9]+)? ('f' | 'F')? ;
// Example:
// 123, 45.67, 3.14f, 2.718F


STRING_LITERAL: '"' ~["\\]* '"' ;
// Example:
// "Hi"


BOOLEAN_LITERAL: 'true' | 'false' ;
// Example:
// true, false


// Whitespace characters
WS: [ \t\n\r]+ -> skip ;

// Comments
COMMENT: '//' ~[\r\n]* -> skip ;


// Unrecognized tokens
UNKNOWN: . ;