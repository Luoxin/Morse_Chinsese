# from date.SQL import executeSQL
import sqlite3


def executeSQL(*args):
    conn = sqlite3.connect("..\date\FourCornerCode.db")
    cursor = conn.cursor()
    if args.__len__()==2:
        re = cursor.execute(args[0], args[1])
        re=re.fetchall()
    elif args.__len__()==1:
        re=cursor.execute(args[0])
        re=re.fetchall()
    else:
        re=False
    conn.commit()
    cursor.close()
    conn.close()
    return re

class FCCmain:
    def __init__(self):
        pass

    def characterToCode(self,character="我爱你"):
        sql="select code from date where character=(?)"
        codes=[]
        for c in character:
            pare=(c,)
            code=executeSQL(sql,pare)
            codes.append(code[0][0])
        # print(codes)
        return codes

    def codeToCharacter(self,code="23550 20407 27292"):
        sql="select character from date where code=(?)"
        characters=[]
        for c in code.split(" "):
            if c.__len__()==0:
                break
            characters.append([])
            pare=(c,)
            character=executeSQL(sql,pare)
            for i in character:
                characters[-1].append(i[0])

        return characters

if __name__ == '__main__':
    a=FCCmain()
    c=a.codeToCharacter()
    print(c)
    # print(executeSQL('select code from date where character="我"'))