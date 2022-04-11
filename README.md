# MidtermProject

Also see [Project Description and Sample input code](https://drive.google.com/drive/folders/17GbDrZVuksgzciWI7q1hbypNfKT_Z_m9?usp=sharing) on the google drive:

**Goal: Write a program, in Python, that evaluates the correctness of a simple java program** (at first, just a driver). Try to maintain readable bottom-up pattern matching throughout your program by substituting lower-level constituents for representative symbols and use comments to show what BNF rule you are applying.

e.g. replace all valid identifiers with I, as in

#**Identifier** ::= [a-z][a-za-z0-9_]

inputString = re.sub("[a-z][a-za-z0-9_]\*",inputString, "I")

or Declaration Expressions

#**DeclarExp** ::= <Type><Identifier>; | <Type><Identifier>=<Number>;

inputputString = re.sub("TI(=N)?;",inputString,"D")

For C level credit:

- Develop a lexer for a simple driver only, that is, a class that contains only the method main (sample development code found in CLevel.java)
- Read in the entire program into a single string to parse (rather than line by line).
- Use pattern matching to ensure that the program conforms to the following Java language rules:
  1. The class definition, declaration of the static main, etc. conform to Java rules for the driver (you can assume there's no variability in these)
  2. Rules for declaring identifiers conform to Java language rules. You do not have to handle object or array declarations, just primitives.
  3. All reserved words are recognized as reserved words and treated accordingly (e.g. not as variable names).
  4. Rules for variable declarations, assignments and arithmetic statements are passed/ recognized if they conform to Java rules. You don’t need to parse parentheses or concatenate Strings for the C level code.
  5. Rule for simple output:
     System.out.println(“a single String”); or System.out.println(aNumberVariable);
  6. Any other structures not explicitly mentioned here (e.g. if/ switch) can be ignored at this time.

For B-level credit: Do everything listed in the C-level. In addition, include

- Rules for if, if/else and while statements, which will be recognized as correct if they conform to their Java rule forms. Assume that branching statements must have {}’s even if they contain a single statement (this makes the problem easier).
- To recognize this expanded inventory, you will have to recognize rules for correct Conditional operations.
- Rules for String concatenation (“The answer is “ + faren);
- Sample code that must be correctly compiled is listed in BLevel.java

For A-level credit: Do everything listed in the C-and B-levels. In addition, include

- Expanded rules for Arithmetic expressions that contain balanced parentheses.
- Rules that parse user Input (Scanner declaration and use);
- Rules for for statements. Again, assume that branching statements must have {}’s even if they contain a single statement (this makes the problem easier) and you can assume the for loop is standard (as seen in ALevel.java).
- Rules that parse another static function (besides main) with input parameters.

For Extra Credit:

- Recognize another file that is a class definition, including attributes, constructor(s) and methods.
- Recognize object declarations (you don’t have to ascertain if the declaration matches the constructor, just if it has the right general form).
- Sample code that must be correctly compiled is listed in Temperature.java and ExtraLevel.java
