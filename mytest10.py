def PrintingCosts(Line):
    sum = 0
    Line = Line.replace(' ', '')
    Line = [x for x in Line]
    for i in range(len(Line)):
        if Line[i] == ' ':
            sum += 0
        elif Line[i] == '\'' or Line[i] == '`':
            sum += 3
        elif Line[i] == '.':
            sum += 4
        elif Line[i] == '\"':
            sum += 6
        elif Line[i] == ',' or Line[i] == '-' or Line[i] == '^':
            sum += 7
        elif Line[i] == ':' or Line[i] == '_':
            sum += 8
        elif Line[i] == '!' or Line[i] == '~':
            sum += 9
        elif Line[i] == '>' or Line[i] == '\\' or Line[i] == '/' or Line[i] == '<':
            sum += 10
        elif Line[i] == ';':
            sum += 11
        elif Line[i] == '(' or Line[i] == '|' or Line[i] == ')':
            sum += 12
        elif Line[i] == 'v' or Line[i] == 'r' or Line[i] == 'x' or Line[i] == '+':
            sum += 13
        elif Line[i] == 'Y' or Line[i] == '=':
            sum += 14
        elif Line[i] == '?' or Line[i] == 'i':
            sum += 15
        elif Line[i] == 'L' or Line[i] == 'T' or Line[i] == 'l' or Line[i] == '7':
            sum += 16
        elif Line[i] == 't' or Line[i] == 'c' or Line[i] == 'u' or Line[i] == '*':
            sum += 17
        elif Line[i] == 'J' or Line[i] == 'n' or Line[i] == ']' or Line[i] == '{' or Line[i] == 'X' or Line[i] == '}' or Line[i] == 'f' or Line[i] == 'I' or Line[i] == '[':
            sum += 18
        elif Line[i] == 'V' or Line[i] == 'z' or Line[i] == 'w' or Line[i] == '1':
            sum += 19
        elif Line[i] == 'o' or Line[i] == 'F' or Line[i] == 'j' or Line[i] == 'C':
            sum += 20
        elif Line[i] == 'h' or Line[i] == 'K' or Line[i] == '4' or Line[i] == 'k' or Line[i] == 's':
            sum += 21
        elif Line[i] == '2' or Line[i] == 'Z' or Line[i] == '%' or Line[i] == 'm' or Line[i] == '0':
            sum += 22
        elif Line[i] == '8' or Line[i] == 'P' or Line[i] == '3' or Line[i] == 'e' or Line[i] == 'U' or Line[i] == 'a':
            sum += 23
        elif Line[i] == '&' or Line[i] == '#' or Line[i] == 'A' or Line[i] == 'y':
            sum += 24
        elif Line[i] == 'b' or Line[i] == 'd' or Line[i] == 'p' or Line[i] == 'G' or Line[i] == 'S' or Line[i] == 'q' or Line[i] == 'H' or Line[i] == 'N':
            sum += 25
        elif Line[i] == 'D' or Line[i] == '9' or Line[i] == 'E' or Line[i] == 'W' or Line[i] == '6' or Line[i] == 'O':
            sum += 26
        elif Line[i] == '5':
            sum += 27
        elif Line[i] == 'R' or Line[i] == 'M':
            sum += 28
        elif Line[i] == '$' or Line[i] == 'B':
            sum += 29
        elif Line[i] == 'g':
            sum += 30
        elif Line[i] == 'Q':
            sum += 31
        elif Line[i] == '@':
            sum += 32
        else:
            sum += 23
    return sum


