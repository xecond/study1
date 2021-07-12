import sys
import numpy as np

stop = False
var_dict = {}

while not stop:
    userinput = input()
    # Quit
    if userinput.lower() == 'quit':
        sys.exit()
    # Def
    elif userinput.startswith('def'):
        if userinput.count('=') == 0:
            print("오류: =가 없음")
        elif userinput.count('=') == 1:
            definition = userinput[4:].split('=')
            var = definition[0].strip()
            val = definition[1].strip()
            if val.isdigit() == True:
                var_dict[var] = int(val)
                var = int(val)
            else:
                if val.count(' ') == 0:
                    print("오류: 숫자칸에 문자가 존재")
                else:
                    print("오류: 숫자 사이에 공백 존재")
        else:
            print("오류: =가 두 개 이상 존재")
    # Calc
    elif userinput.startswith('calc'):
        if userinput.count('+') == 1:
            calculation = userinput[5:].split('+')
            opd1 = calculation[0].strip()
            opd2 = calculation[1].strip()
            if (opd1.isalpha() == False) or (opd2.isalpha() == False):
                if (opd1.isdigit() == True) or (opd2.isdigit() == True):
                    print("오류: 피연산자 중 변수가 아닌 숫자가 존재")
                else:
                    print("오류: 연산자가 한 종류 이상 존재")
            else:
                if (opd1 not in var_dict) or (opd2 not in var_dict):
                    print("오류: 선언되지 않은 변수를 사용")
                else:
                    print(var_dict[opd1] + var_dict[opd2])
        elif userinput.count('-') == 1:
            calculation = userinput[5:].split('-')
            opd1 = calculation[0].strip()
            opd2 = calculation[1].strip()
            if (opd1.isalpha() == False) or (opd2.isalpha() == False):
                if (opd1.isdigit() == True) or (opd2.isdigit() == True):
                    print("오류: 피연산자 중 변수가 아닌 숫자가 존재")
                else:
                    print("오류: 연산자가 한 종류 이상 존재")
            else:
                if (opd1 not in var_dict) or (opd2 not in var_dict):
                    print("오류: 선언되지 않은 변수를 사용")
                else:
                    print(var_dict[opd1] - var_dict[opd2])
        elif userinput.count('*') == 1:
            calculation = userinput[5:].split('*')
            opd1 = calculation[0].strip()
            opd2 = calculation[1].strip()
            if (opd1.isalpha() == False) or (opd2.isalpha() == False):
                if (opd1.isdigit() == True) or (opd2.isdigit() == True):
                    print("오류: 피연산자 중 변수가 아닌 숫자가 존재")
                else:
                    print("오류: 연산자가 한 종류 이상 존재")
            else:
                if (opd1 not in var_dict) or (opd2 not in var_dict):
                    print("오류: 선언되지 않은 변수를 사용")
                else:
                    print(var_dict[opd1] * var_dict[opd2])
        elif userinput.count('/') == 1:
            calculation = userinput[5:].split('/')
            opd1 = calculation[0].strip()
            opd2 = calculation[1].strip()
            if (opd1.isalpha() == False) or (opd2.isalpha() == False):
                if (opd1.isdigit() == True) or (opd2.isdigit() == True):
                    print("오류: 피연산자 중 변수가 아닌 숫자가 존재")
                else:
                    print("오류: 연산자가 한 종류 이상 존재")
            else:
                if (opd1 not in var_dict) or (opd2 not in var_dict):
                    print("오류: 선언되지 않은 변수를 사용")
                elif var_dict[opd2] == 0:
                    print("오류: 분모가 0")
                else:
                    if var_dict[opd1] % var_dict[opd2] == 0:
                        print(int(var_dict[opd1] / var_dict[opd2]))
                    else:
                        print(format(np.ceil(var_dict[opd1] / var_dict[opd2] * 1000)/1000,'.2f'))
        else:
            print("오류: 연산자가 한 개 이상 존재")
    # See
    elif userinput.startswith('see'):
        print(var_dict)
    # Undefined
    else:
        print('undefined')