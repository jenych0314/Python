import calcFunction

functionDic = {
    'factorial (!)': calcFunction.factorial,
    '-> binary': calcFunction.dec2bin,
    'binary -> dec': calcFunction.bin2dec,
    'dec -> roman': calcFunction.dec2roman,
    'roman -> dec': calcFunction.roman2dec,
}

functionList = [x for x in functionDic]