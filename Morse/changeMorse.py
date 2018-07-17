import sqlite3
import re

from user.FCCmain import FCCmain

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




class Morse:

    def __init__(self):
        self.FCC=FCCmain()
        # self.startcode=""

        pass

    def LettetoMorse(self,s="我爱你"):

        #判断是否有中文
        zhPattern = re.compile(u'[\u4e00-\u9fa5]')
        match = zhPattern.search(s)
        if match:
            temp_s=self.FCC.characterToCode(s)
            s=""
            for i in temp_s:
                s+=i+" "
        # print(s)

        Morsecodes=""
        try:
            for i in s:
                if i ==" ":
                    Morsecodes+="  "
                    continue
                try:
                    sql='select code from Morse_special where characters=(?)'
                    pare=(i,)
                    Morsecode=executeSQL(sql,pare)
                    Morsecodes+=Morsecode[0][0]
                except:
                    sql="select Morse from Morse where character=(?)"
                    pare=(i,)
                    Morsecode=executeSQL(sql, pare)
                    Morsecodes += Morsecode[0][0]
                finally:
                    Morsecodes+=" "
            return Morsecodes
        except:
            return None

    def MorsetoLetter(self,s="..--- ----- .---- .....   ....- ....- --... .---- "):

        characters=""
        try:
            for cs in s.split("   "):
                for c in cs.split(" "):
                    if c.__len__()==0:
                        continue
                    try:
                        sql='select characters from Morse_special where code=(?)'
                        pare=(c,)
                        character=executeSQL(sql,pare)
                        characters+=character[0][0]
                    except:
                        sql="select character from Morse where Morse=(?)"
                        pare=(c,)
                        character=executeSQL(sql, pare)
                        characters += character[0][0]
                characters+=" "

            zhPattern = re.compile('[\d]')
            match = zhPattern.search(characters)
            if match:
                for i in characters.split(" "):
                    # print(i.__len__())
                    if i.__len__()!=5 and i.__len__()!=0:
                        return characters
                characters=self.FCC.codeToCharacter(characters)

            return characters
        except:
            return None



if __name__ == '__main__':
    a=Morse()
    # s=a.LettetoMorse("我爱你")
    s=a.MorsetoLetter('..--- ...-- ..... ..... -----   ..--- ----- ....- ----- --...   ..--- --... ..--- ----. ..--- ')
    print(s)

