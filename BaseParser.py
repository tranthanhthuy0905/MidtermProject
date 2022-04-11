import re


def baseObjectParser(inputVal):
    # _OB::=([A-Z][a-zA-Z0-9_]*)
    return re.sub("([A-Z][a-zA-Z0-9_]*)", "_OB", inputVal)


def baseClassParser(inputVal):
    # IM::= import (.+)
    import_pattern = "(import (.+))"
    # CL::= (class _OB)
    class_pattern = "(class _OB)"
    # ME::= (public static void main\(_OB argv\[\]\)( throws _OB)?)
    main_pattern = "(public static void main\(_OB argv\[\]\)( throws _OB)?)"

    # Check import
    check_import = re.sub(import_pattern, "IM", inputVal)
    # Check class, main method
    check_class = re.sub(class_pattern, "CL", check_import)
    check_method = re.sub(main_pattern, "ME", check_class)
    return check_method


def baseConstructorParser(inputVal):
    # _CTT::= DT\((DTX(\,DTX)*)?\)\{(S)+\}
    return re.sub(r'DT\((DTX(\,DTX)*)?\)\{(S)+\}', "_CTT", baseStatementParser(inputVal))


def baseStatementParser(inputVal):
    # S::= (X=[XNVE];)|(LOOP)|(SELECT)|(DE)+|(OT)+|(_SCAN)+|(_RE)|(_CMT)|(_CTT)
    statement_pattern = "((X=[XNVE];)|(LOOP)|(SELECT)|(DE)+|(OT)+|(_SCAN)+|(_RE)|(_CMT)|(_CTT))"
    return re.sub(statement_pattern, "S", inputVal)


def baseProgramParser(inputVal):
    # P::= IMCL\{(S|(M\{(S)+\}))*(ME\{(S|(M\{(S)+\}))+\})?(S|(M\{(S)+\}))*\}(S)*
    program_pattern = "(IMCL\{(S|(M\{(S)+\}))*(ME\{(S|(M\{(S)+\}))+\})?(S|(M\{(S)+\}))*\}(S)*)"
    return re.sub(program_pattern, "P", baseStatementParser(inputVal))


def baseCommentParser(input):
    # _CMT ::= (\/\/).+|(\/\*[\s\S]*?\*\/)|\/\*.*(IM|CL)
    comment_pattern = "(\/\/).+|(\/\*[\s\S]*?\*\/)|\/\*.*(IM|CL)"
    return re.sub(comment_pattern, "_CMT", input)


def baseSpecialityParser(inputVal):
    # _NEW ::= new( )+
    _NEW = "new( )+"
    check_new = re.sub(_NEW, "_NEW", inputVal)

    #_RETURN ::= return[ ]*
    _RE = "return[ ]*"
    check_return = re.sub(_RE, "_RETURN", check_new)

    # System
    _SI = "_OB.in"
    _SO = "((_OB.out.println)|(_OB.out.print))"
    check_systemIn = re.sub(_SI, "_SI", check_return)
    check_systemOut = re.sub(_SO, "_SO", check_systemIn)

    # Conditions
    _ELSEIF = "(else if( )*\()"
    _IF = "(if( )*\()"
    _ELSE = "(else( )*\{)"
    check_elseif = re.sub(_ELSEIF, "_ELIF(", check_systemOut)
    check_if = re.sub(_IF, "_IF(", check_elseif)
    check_else = re.sub(_ELSE, "_EL{", check_if)

    # Loops
    _WH = "(while( )*\()"
    _FOR = "(for( )*\()"
    check_while = re.sub(_WH, "_WH(", check_else)
    check_for = re.sub(_FOR, "_FOR(", check_while)

    # Datatype
    datatype_pattern = "(((private)|(public)) )?((byte)|(short)|(int)|(long)|(float)|(double)|(boolean)|(char)|(_OB))"
    check_datatype = re.sub(datatype_pattern, "DT", check_for)

    # String values
    check_string = re.sub(r'(["\'])((?:\\.|[^\\])*?)(\1)', "V", check_datatype)

    # Boolean Values
    boolean_pattern = "(true|false)"
    check_datatype = re.sub(boolean_pattern, "B", check_string)

    # Function
    function_pattern = "(((public static)|(public)|(static))[ ]+DT)"
    check_function = re.sub(function_pattern, "DT", check_datatype)

    return check_function


def baseTermsParser(inputVal):
    # X::= [a-z]{1}[a-zA-Z0-9_]*
    identifier_pattern = "[a-z]{1}[a-zA-Z0-9_]*"
    # N::= [+-]?([0-9]*[.]?)[0-9]+
    number_pattern = "[+-]?([0-9]*[.]?)[0-9]+"

    check_identifier = re.sub(identifier_pattern, "X", inputVal)
    check_number = re.sub(number_pattern, "N", check_identifier)
    # 4. Delete the space
    return re.sub("\s", "", check_number)


def baseArithmeticParser(inputVal):
    # AOp ::= [+\-*/]
    arithmetic_pattern = "[+\-*/]"
    return re.sub(arithmetic_pattern, "AOp", inputVal)


def baseExpressionParser(inputVal):
    # E::= [XVN](AOp\(*[XVN]\)*)+|(X\(X\)N)|\([XVN]+\)(AOp[XNV])*
    expression_pattern = "[XVN](AOp\(*[XVN]\)*)+|(X\(X\)N)|\([XVN]+\)(AOp[XNV])*"
    return re.sub(expression_pattern, "E", inputVal)


def baseOutputParser(inputVal):
    output_pattern = "_SO((\([NXV](\+[NXV](\.X\(\))?)*\));)"
    return_pattern = "_RETURN[(]?([XNV](\+[NXV](\(\))?)*)[)]?\;"
    check_return = re.sub(return_pattern, "_RE", inputVal)
    return re.sub(output_pattern, "OT", check_return)


def baseDeclarationParser(inputVal):
    
    declaration_pattern = "((DTX(,X)*;)|(DTX=(X\(X\));)|(DTX=X.X\(\);)|(DTX(,X)*=((XE)+)\;)|(DTX(,X)*=([NVBE](AOp[NVBE])*)\;)|(DTX(,X)*=[NVB];))"
    return re.sub(declaration_pattern, "DE", inputVal)


def baseScannerParser(inputVal):
    scanner_pattern = "(DTX=_NEWDT\(((_SI)|X)+\);)"
    return re.sub(scanner_pattern, "_SCAN", inputVal)


def baseMethodParser(inputVal):
    method_pattern = "DTX\((DTX(,DTX)*)?\)"
    return re.sub(method_pattern, "M", inputVal)


def baseConditionParser(inputVal):
    conditional_pattern = "(<=)|(>=)|(!=)|(==)|(<)|(>)"
    logical_pattern = "(\&\&)|(\|\|)"
    condStatement_pattern = "[EX](AOp[NX])*COp([NX]AOp)*[NXE](LOpX(AOp[NX])*COp([NX]AOp)*[NX])*"

    # Check conditions
    check_conditional = re.sub(conditional_pattern, "COp", inputVal)
    check_logical = re.sub(logical_pattern, "LOp", check_conditional)
    check_condStatement = re.sub(condStatement_pattern, "COn", check_logical)

    return check_condStatement


def baseSelectionLoopParser(inputVal):
    # SELECT::= _IF\(COn\)\{(S)+\}(_ELIF\(COn\)\{(S)+\})*(_EL\{(S)+\})
    SELECT = "_IF\(COn\)\{(S)+\}(_ELIF\(COn\)\{(S)+\})*(_EL\{(S)+\})*"
    # LOOP::= (_WH\(COn\)\{(S)+\})|(_FOR\(SCOn;_LP\)\{(S)+\})
    LOOP = "((_WH\(COn\)\{(S)+\})|(_FOR\(SCOn\;_LP\)\{(S)+\}))"

    # Check number of while, if or for
    no_of_keywords = len(re.findall("((_WH)|(_IF)|(_FOR))", inputVal))
    total_running_time = no_of_keywords
    count = 0
    result = inputVal
    while no_of_keywords > 0 and count <= total_running_time:
        check_selection = re.sub(SELECT, "SELECT", result)
        check_loops = re.sub(
            LOOP, "LOOP", baseStatementParser(check_selection))
        result = baseStatementParser(check_loops)
        count += 1
        no_of_keywords = len(re.findall("((_WH)|(_IF)|(_FOR))", result))
    return result
