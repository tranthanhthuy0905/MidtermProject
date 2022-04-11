from BaseParser import *


def parser(inputVal):
    
    # Check object 
    check_object = baseObjectParser(inputVal)
    
    # Check Import, Class, Method
    check_class = baseClassParser(check_object)

    # Check Comment
    check_comment = baseCommentParser(check_class)

    # Check special cases/ special words
    check_specialCases = baseSpecialityParser(check_comment)

    # Check Terms (deleting space here)
    check_terms = baseTermsParser(check_specialCases)

    # Check additional methods
    check_additionalMethods = baseMethodParser(check_terms)

    # Check increment loop
    loop = "(X\+\+)"
    check_incrementLoop = re.sub(loop, "_LP", check_additionalMethods)

    # Check scanner
    check_scanner = baseScannerParser(check_incrementLoop)

    # Check output, return
    check_outputReturn = baseOutputParser(check_scanner)

    # Check Arithmetic
    check_arithmetic = baseArithmeticParser(check_outputReturn)

    # Check expression
    check_expression = baseExpressionParser(check_arithmetic)

    # Check condition statement
    check_conditions = baseConditionParser(check_expression)

    # Check Declarations
    check_declaration = baseDeclarationParser(check_conditions)

    # Check Constructor
    check_constructor = baseConstructorParser(check_declaration)
    
    # Check Statements
    check_statement = baseStatementParser(check_constructor)

    # # Check Selection, Loop
    check_selectionLoop = baseSelectionLoopParser(check_statement)

    # Check program
    #return(check_comment)
    return(baseProgramParser(check_selectionLoop))


def testFile(inputFile):
    test_file = open(inputFile, "r")
    data = test_file.read()
    test_file.close()
    if (data.count("(") != data.count(")")):
        print("Fail to check balanced Parentheses in " + inputFile)
        return
    return data


def main():
    '''Test C-level'''
    # print("Parsing C-level: ")
    print(parser(testFile("testC.java")))

    '''Test B-level'''
    #print("Parsing B-level: ")
    print(parser(testFile("testB.java")))

    '''Test A-level'''
    #print("Parsing A-level: ")
    print(parser(testFile("testA.java")))
    
    print(parser(testFile("ExtraCredit.java")))

    '''Test Extra'''
    #print("Parsing A-level: ")
    print(parser(testFile("Temperature.java")))
main()
