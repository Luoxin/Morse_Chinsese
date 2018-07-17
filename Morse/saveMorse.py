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


executeSQL('delete from Morse')
executeSQL('delete from Morse_special')


Morse={'1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
       '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
       "a":".-","b":"-...","c":"-.-.","d":"-..","e":".", "f":"..-.",
       "g":"--.","h":"....","i":"..","j":".---", "k":"-.-","l":".-..",
       "m":"--","n":"-.","o":"---", "p":".--.","q":"--.-","r":".-.",
       "s":"...","t":"-", "u":"..-","v":"...-","w":".--","x":"-..-",
       "y":"-.--", "z":"--..",":":"--..--",".":".-.-.-",',':'--..--',
       '\'':'.----.','?':'..--..','-':'-....-','/':'-..-.','=':'-...-',
       '(':'-.--.',')':'-.--.-','!':'-.-.--','_':' ..-- .-','"':'.-..-.',
       '@':'--.-. ','&':'....','+':'.-.-.'}




sql='insert into Morse values (?,?)'
for i in Morse.keys():
    pare=(i,Morse[i])
    executeSQL(sql,pare)


Morse_special={'EEEE etc':'........','SOS':'...---...','wait':'.-...','go':'.-.'}
sql='insert into Morse_special values (?,?)'
for i in Morse_special.keys():
    pare=(i,Morse_special[i])
    executeSQL(sql,pare)
