import requests
import sqlite3
import random
import time


print("")
print("____________________________")
print("")
print("   NITRO-GEN .GIFT v1.0.0   ")
print("")
print("  samuel9221991@icloud.com  ")
print("")
print("____________________________")
print("")



#________________
# EJECUCIONES
#________________


def empezar(nombre):

    # VARIABLES
    ñ = 0
    caracteres = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    db = sqlite3.connect("used.db")
    sql = db.cursor() 


    #CREACIÓN DE LA TABLA
    sql.execute('''
        CREATE TABLE IF NOT EXISTS USADO (
            LINK STR
        )
    ''')
    db.commit()


    # APERTURA DE LOS ARCHIVOS
    archivo = open(f"{nombre}.txt", "w+")
    archivo.close()
    archivo = open(f"{nombre}.txt", "a")
    

    # CUENTA CODIGOS
    sql.execute("SELECT * FROM USADO")
    print("")
    print(f"BLACKLISTED WORST CODES: {len(sql.fetchall())}")
    print("")
    db.commit()
    
    
    # INICIO
    while True:
        resultado = "".join([random.choice(caracteres) for i in range(16)])


        # BUSCA SI YA FUÉ CHECADO
        sql.execute(f"SELECT LINK FROM USADO WHERE LINK = '{resultado}'")
        ya_usado = len(sql.fetchall())
        db.commit()
    
        if ya_usado == 0:
            

            # REVISA SI FUNCIONA EL CODIGO
            pag = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{resultado}")

            if pag.status_code == 200:
                print(f"CORRECT LINK: discord.gift/{resultado}")

                archivo.write(f"CORRECT LINK: discord.gift/{resultado}\n")
                archivo.close()

                sql.execute(f"INSERT INTO USADO (LINK) VALUES ('{resultado}')")
                db.commit()
            
            elif pag.status_code == 429:
                print(pag.status_code)
                time.sleep(20)
            
            elif pag.status_code == 404:
                print(f"WORST LINK: discord.gift/{resultado}")
                sql.execute(f"INSERT INTO USADO (LINK) VALUES ('{resultado}')")
                db.commit()

        time.sleep(10)
            




#___________________
# INICIALIZACIÓN
#___________________


print("")
print("TYPE THE FILE NAME WHERE THE SCRIPT WILL SAVE THE CORRECT LINKS.")
opcion = input("> ").lower()

if opcion != "":
    empezar(opcion)

else:
    print(f"PUT A FUCKING TEXT.")
