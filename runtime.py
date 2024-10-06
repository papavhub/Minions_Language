import sys
import exceptions

class Minions:
    def __init__(self):
        self.data = ["Banana!"]*256

    def toNumber(self, code):
        if code == "Hana":
            return 1
        elif code == "Dul":
            return 2
        elif code == "Sae":
            return 3
        else:
            value = code.split("-")
            count = 0
            for v in value:
                if v == "Muak":
                    count += 1
                else:
                    raise exceptions.NumberException()
            return count

    @staticmethod
    def type(code):
        if 'Banana' in code:
            return 'REPEAT'
        if 'Poopaye!' in code:
            return 'END'
        if 'Tulaliloo ti amo!' in code:
            return 'INPUT'
        if 'Kanpai!' in code:
            return 'PRINT'
        if 'Gelato' in code:
            return 'DEF'

    def compileLine(self, code):
        if code == '':
            return None
        TYPE = self.type(code)
        
        if TYPE == 'DEF': # Gelato! Hana hem" -> data[1] = hem
            try:
                gelato, var, value = code.split(" ") # Gelato, var, value"
            except:
                raise exceptions.InputException()
            
            self.data[self.toNumber(var)] = value
            
        elif TYPE == 'END': # 프로그램 종료
            sys.exit()
            
        elif TYPE == 'INPUT': # Tulaliloo ti amo! String Hana hem -> data[1] = hem
            try:
                type, var = code.replace("Tulaliloo ti amo! ", "").split(" ") # tulaliloo, type, var
            except:
                raise exceptions.InputException()

            if type == "string" or type == "String": # String
                print("?")
                self.data[self.toNumber(var)] = str(input())
            elif type == "int" or type == "Int": # Int
                print("?")
                self.data[self.toNumber(var)] = int(input())
                
        elif TYPE == 'PRINT':
            try:
                kanpai = code.split(" ")
            except:
                raise exceptions.InputException()
            
            # data에 저장한 변수를 출력한다.
            if len(kanpai) == 2:
                try:
                    var = self.toNumber(kanpai[-1])
                    print(str(self.data[var]) + "!")
                    return
                except:
                    pass
            
            for k in kanpai:
                if k == "Kanpai!":
                    pass
                else:
                    print(str(k) + "!")
                    
        elif TYPE == 'REPEAT': # Banana Dul -> Banana Banana
            try:
                banana, number = code.split(" ")
            except:
                raise exceptions.InputException()
            
            for _ in range(self.toNumber(number)):
                print("Banana!")

    def compile(self, code, check=True, errors=100000):
        
        jun = False
        recode = ''
        spliter = '\n' if '\n' in code else '~'
        code = code.rstrip().split(spliter)
        
        # 시작, 끝 문법이 맞지 않는 경우
        if check and (code[0].replace(" ","") != 'Bello!' or code[-1] != 'Poopaye!' or not code[0].startswith('Bello!')):
            raise exceptions.MainException()
        
        index = 0
        error = 0
        while index < len(code):
            errorline = index
            c = code[index].strip()
            res = self.compileLine(c)
            if jun:
                jun = False
                code[index] = recode                
            if isinstance(res, int):
                index = res-2
            if isinstance(res, str):
                recode = code[index]
                code[index] = res
                index -= 1
                jun = True

            index += 1
            error += 1
            if error == errors:
                raise RecursionError(str(errorline+1) + '번째 줄에서 무한 루프가 감지되었습니다.')

    def compilePath(self, path):
        with open(path) as file:
            code = ''.join(file.readlines())
            self.compile(code)