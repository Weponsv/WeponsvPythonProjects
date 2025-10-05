#TESTS (DON'T NEED):
#import turtle
#ts = turtle.getscreen()
#turtle.hideturtle()
#turtle.write("CPU [HOLA]")
#turtle.exitonclick()


#WHAT'S NEW:
#     THERE IS A NEW CODE: "hehe" (USE ONLY ON PC!!!)
#     A COOL SCENE OF INSTALLING PACKAGES IF YOU SELECT THE LANGUAGES
#     SOME BUGS HAS BEEN REMOVED IN THE PROGRAMM AND IN THE CONSOLE
#     NOW YOU NEED TO WAIT THE QUESTION AND THE ANSWER OF THE CPU
#     THE LINES OF THE PROGRAMM ARE NOW ~500
#     SOME PARTS OF THE DIALOG WORKS WITH "AGE"
#     MORE QUESTIONS ON THE DIALOG
#     ADDED THE CALCULATOR

# In Menu write "CODES"
####################################
#CODES:
#ERROR ; AMOGUS ; ABOBUS ; HELOOO; 13579; hehe (ONLY PC!!!)

#IMPORTING "TIME"
import time

#THE CYCLE STARTS HERE:
cycle = True
while cycle:
    cycle = False

#MENU TITTLE
    print("  _________      __________                                                     ________                                             ")
    print(" |              |          |     |           |          |   |            |    /           \\     |                    /\\          |   ")
    print(" |              |          |     |           |          \\   |            |   |            |     |                   /  \\         \\  ")
    print(" |              |          |     |           |              |            |   |            |     |                  /    \\           ")
    print(" |              |__________|     |           |              |            |   |            |     |                 /      \\          ")
    print(" |              |                |           |              |------------|   |            |     |                /________\\         ")
    print(" |              |                |           |              |            |   |            |     |               /          \\        ")
    print(" |              |                |           |              |            |   |            |     |              /            \\       ")
    print(" |              |                |           |              |            |   |            |     |             /              \\      ")
    print(" |__________    |                |___________|              |            |    \\ ________ /      |_________   /                \\     ")

#MENU
    print("Lenguaje / Язык / Lenguage")
    print("ES = Español")
    print("EN = English")
    print("RU = Русский")
    print("IN = Informacion / Информация / Information ")
    print("CALC = Calculador / Калькулятор / Calculator ")
    print("")
    language = str(input()).lower()

#PC OR MOBILE:
    if language == "es":
        pc_or_mobile = str(input("Estas en PC? Y/n: ")).lower()
        time.sleep(0.5)
        print("Continuando el programma...")
        time.sleep(1.2)
        
        for x in range(55):
            print("")
            
    elif language == "en":
        pc_or_mobile = str(input("Are you on PC? Y/n: ")).lower()
        time.sleep(0.5)
        print("Continuing the programm...")
        time.sleep(1.2)
        
        for x in range(55):
            print("")
        
    elif language == "ru":
        pc_or_mobile = str(input("Ты на ПК? Y/n: ")).lower()
        time.sleep(0.5)
        print("Продолжаю программу...")
        time.sleep(1.2)
        
        for x in range(55):
            print("")
            
    elif language == "codes":
        pc_or_mobile = str(input("Are you on PC? Y/n: ")).lower()
        

#COOL SCENE
    if language == "es" or language == "en" or language == "ru":
        print("Installing the packages...")
        time.sleep(2)
        print("Unpacking the files...")
        time.sleep(1)
        print("Loading the programm...")
        time.sleep(0.2)
        print("Starting...")
        time.sleep(0.8)
        for x in range(52):
             print("")
    else:
        pass

#SPANISH PROGRAMM:
    if language=="es":
    
        print("CPU: Hola")
        time.sleep(1.2)
        print("CPU: Como te llamas?")
        name=str(input("TU: "))
        time.sleep(1.2)
        print("CPU: Hola", name)
        time.sleep(2)
    
        print("CPU: Que edad tienes?")
        age=int(input("TU: "))
        time.sleep(0.8)
        if age <= 18:
            print("CPU: Heres joven")
        elif 18 < age < 60:
            print("CPU: Heres un/a adulto/a")
        elif 90 > age >= 60:
            print("CPU: Heres una persona vieja/o")
        else:
            print("CPU: Esos an'os son muchos, pero ok")
        time.sleep(1.2)
        print("CPU: Yo tengo 2 años de edad")
        time.sleep(1.2)

        if age < 18:
            print("CPU: Vas a la escuela?")
            school=str(input("TU: "))
            time.sleep(1.2)
            print("CPU: ok")
            print("CPU: Yo no voy a la escuela ni al trabajo porque soy un robot programado")
            time.sleep(1.2)
        else:
            print("CPU: Tienes mas de 18 an'os, tu no vas a la escuela")
            time.sleep(1.2)    

        print("CPU: Tu tienes un hobby?")
        hobby_yes_no = str(input("TU: ")).lower()
        time.sleep(1.2)
        if hobby_yes_no == "si" or hobby_yes_no == "claro":
            print("CPU: Que hobby tienes?")
            hobby = str(input("TU: "))
            time.sleep(0.8)
            print("CPU: Que hobby interesante!")
        else:
            print("CPU: Que triste, tener un hobby es bueno")

        if age >= 14:
            print("CPU: Tu vas a trabajar?")
            work_yes_no = str(input("TU: ")).lower()
            time.sleep(1.2)
            if work_yes_no == "si" or work_yes_no == "claro":
                print("CPU: Que trabajo tienes?")
                work = str(input("TU: "))
                time.sleep(1.2)
                print("CPU: Trabaja duro y estaras feliz")
            else:
                print("CPU: Preparate, porque algun dia empezaras a trabajar (O ya trabajaste en tu vida)")
        else:
            print(f"CPU: Tu no puedes trabajar ya que tienes {age} an'os")

        time.sleep(1.2)
        print("CPU: Jugamos?")
        game_yes_no=str(input("TU: ")).lower()
        time.sleep(1.2)
        if game_yes_no=="si" or game_yes_no=="ok":
            print("CPU: Cual es mi nombre?")
            cpu_name=str(input("TU: ")).lower()
            time.sleep(1.2)
            if cpu_name=="cpu" or cpu_name=="computador":
                print("CPU: Logico, esta escrito")
                time.sleep(0.8)
                print("CPU: Chao")
                print("")
                time.sleep(2)
                print("Weponsv: Gracias por ver mi creacion")
            else:
                print("CPU: Incorrecto")
                time.sleep(0.8)
                print("CPU: Intenta otra vez")
                time.sleep(0.8)
                print("CPU: Cual es mi nombre?")
                cpu_name=str(input("TU: ")).lower()
                time.sleep(1.2)
                if cpu_name=="cpu" or cpu_name=="computador":
                    print("CPU: Correcto")
                    time.sleep(0.8)
                    print("CPU: Chao")
                    time.sleep(2)
                    print("")
                    print("Weponsv: Gracias por ver mi creacion")
                else:
                    print("CPU: Incorrecto, la respuesta hera 'CPU', hera cosa logica.")
                    time.sleep(0.8)
                    print("CPU: Chao")
                    time.sleep(2)
                    print("")
                    print("Weponsv: Gracias por ver mi creacion")
        else:
            print("CPU: OK")
            time.sleep(0.8)
            print("CPU: Chao")
            time.sleep(2.0)
            print("")
            print("Weponsv: Gracias por ver mi creacion")

#PROGRAMM IN ENGLISH:

    elif language == "en":
        
        print("CPU: Hello")
        time.sleep(1.2)
        print("CPU: What is your name?")
        name=str(input("YOU: "))
        time.sleep(1.2)
        print("CPU: Hello", name)
        time.sleep(2)
        
        print("CPU: How old are you?")
        age=int(input("YOU: "))
        time.sleep(0.8)
        if age <= 18:
            print("CPU: You are young")
        elif 18 < age < 60:
            print("CPU: You are an adult")
        elif 90 > age >= 60:
            print("CPU: You are a very old person")
        else:
            print("CPU: That age is strange, but ok")
        time.sleep(1.2)
        print("CPU: I am 2 years old")
        time.sleep(1.2)    
        
        if age < 18:
            print("CPU: Do you go to school?")
            school=str(input("YOU: "))
            time.sleep(1.2)
            print("CPU: I don´t go to school and I don´t go to work. (I´m a programm)")
        else:
            print("CPU: You have more than 18 years, you dont go to school")
            time.sleep(1.2)

        print("CPU: Do you have a hobby?")
        hobby_yes_no = str(input("YOU: ")).lower()
        time.sleep(1.2)
        if hobby_yes_no == "yes" or hobby_yes_no == "ok":
            print("CPU: What hobby you have?")
            hobby = str(input("YOU: "))
            time.sleep(0.8)
            print("CPU: What a interesting hobby!")
        else:
            print("CPU: Very sad, have a hobby is good")
        time.sleep(1.2)

        if age >= 14:
            print("CPU: Do you go to work?")
            work_yes_no = str(input("YOU: ")).lower()
            time.sleep(1.2)
            if work_yes_no == "ok" or work_yes_no == "yes" or work_yes_no == "yea":
                print("CPU: What work do you have?")
                work = str(input("YOU: "))
                time.sleep(1.2)
                print("CPU: Work hard and you will be good")
            else:
                print("CPU: You will need a work, not now, but another day (or maybe you already worked)")
        else:
            print(f"CPU: You can't go to work if you are {age}")
            
        time.sleep(1.2)
        print("CPU: Do you want to play?")
        game_yes_no=str(input("YOU: ")).lower()
        time.sleep(0.8)
        if game_yes_no=="yes" or game_yes_no=="ok":
            print("CPU: What is my name?")
            cpu_name=str(input("YOU: ")).lower()
            time.sleep(1.2)
            if cpu_name=="cpu" or cpu_name=="computer":
                print("CPU: Correct")
                time.sleep(0.5)
                print("CPU: Bye")
                print("")
                time.sleep(2)
                print("Weponsv: Thanks you for viewing my creation")
            else:
                print("CPU: Incorrect")
                time.sleep(0.8)
                print("CPU: Try again")
                time.sleep(0.8)
                print("CPU: What is my name?")
                
                cpu_name=str(input("YOU: "))
                time.sleep(1.2)
                if cpu_name=="cpu" or cpu_name=="computer":
                    print("CPU: Correct")
                    time.sleep(0.5)
                    print("CPU: Bye")
                    print("")
                    time.sleep(2)
                    print("Weponsv: Thanks you for viewing my creation")
                else:
                    print("CPU: Incorrect")
                    time.sleep(0.8)
                    print("CPU: The answer was 'CPU'")
                    print("")
                    time.sleep(2)
                    print("Weponsv: Thanks you for viewing my creation")
        else:
            print("CPU: OK")
            time.sleep(0.8)
            print("CPU: Bye")
            print("")
            time.sleep(2)
            print("Weponsv: Thanks you for viewing my creation")

#PROGRAMM IN RUSSIAN:

    elif language=="ru":
            
        print("CPU: Привет")
        time.sleep(1.2)
        print("CPU: Как тебя зовут?")
        name=str(input("ТЫ: "))
        time.sleep(1.2)
        print("CPU: Привет",name)
        time.sleep(2)

        print("CPU: Сколько тебе лет?")
        age=int(input("ТЫ: "))
        time.sleep(0.8)
        if age <= 18:
            print("CPU: Ты молодой/ая")
        elif 18 < age < 60:
            print("CPU: Ты уже взрослый/ая")
        elif 90 > age >= 60:
            print("CPU: Ты очень старый/ая")
        else:
            print("CPU: Этот возраст странный, но ладно")
        time.sleep(1.2)
        print("CPU: А мне 2 года")
        time.sleep(1.2)    

        if age<18:
            print("CPU: Ты идёшь в школу?")
            school=str(input("ТЫ: "))
            time.sleep(1.2)
            print("CPU: А я не иду ни в школу, ни на работу. Я же робот")
        else:
            print("CPU: Тебе больше 18 лет, ты не идёшь в школу")
        time.sleep(1.2)
        
        print("CPU: У тебя есть хобби?")
        hobby_yes_no = str(input("ТЫ: ")).lower()
        time.sleep(1.2)
        if hobby_yes_no == "да" or hobby_yes_no == "есть"  or hobby_yes_no == "конечно":
            print("CPU: Какое хобби у тебя есть?")
            hobby = str(input("ТЫ: "))
            time.sleep(0.8)
            print("CPU: Какое интересное хобби!")
        else:
            print("CPU: Жаль, хобби это очень интересно")
        time.sleep(1.2)    

        if age >= 14:
            print("CPU: Ты идёшь на работу?")
            work_yes_no = str(input("ТЫ: ")).lower()
            time.sleep(1.2)
            if work_yes_no == "да" or work_yes_no == "конечно" or work_yes_no == "есть":
                print("CPU: Как ты работаешь?")
                work = str(input("ТЫ: "))
                time.sleep(1.2)
                print("CPU: Работай усердно и будешь счастлив!")
            else:
                print("CPU: Готовься, когда нибудь ты всё таки начнёшь работать (Хотя может ты уже на пенсии или проработал)")
        else:
            print(f"CPU: Ты не можешь работать, так как тебе {age}")
        time.sleep(1.2)    

        print("CPU: Хочешь поиграть?")
        game_yes_no=str(input("ТЫ: ")).lower()
        time.sleep(0.8)
        if game_yes_no=="да" or game_yes_no=="хорошо" or game_yes_no=="давай" or game_yes_no=="конечно":
            print("CPU: Как меня зовут?")
            cpu_name=str(input("ТЫ: ")).lower()
            time.sleep(0.5)
            if cpu_name=="cpu" or cpu_name=="компьютер":
                print("CPU: Правильно")
                time.sleep(0.8)
                print("CPU: Пока")
                print("")
                time.sleep(2)
                print("Weponsv: Спасибо что посмотрели на мою программу")
            else:
                print("CPU: Неправильно")
                time.sleep(0.6)
                print("CPU: Попробуй ещё раз")
                time.sleep(0.6)
                print("CPU: Как меня зовут?")
                cpu_name=str(input("ТЫ: ")).lower()
                time.sleep(1.2)
                if cpu_name=="cpu" or cpu_name=="компьютер":
                    print("CPU: Правильно")
                    time.sleep(0.8)
                    print("CPU: Пока")
                    print("")
                    time.sleep(2)
                    print("Weponsv: Спасибо что посмотрели мою программу")
                else:
                    print("CPU: Неправильно, ответ был 'cpu'.")
                    time.sleep(0.5)
                    print("CPU: Пока")
                    print("")
                    time.sleep(2)
                    print("Weponsv: Спасибо что посмотрели мою программу")
        else:
            print("CPU: Хорошо")
            time.sleep(0.8)
            print("CPU: Пока")
            print("")
            time.sleep(2)
            print("Weponsv: Спасибо что посмотрели мою программу")

#MENU OF CODES:

    elif language=="codes":
        print("PLEASE ENTER SECRET CODE FOR SPAM:")
        secret_code=str(input())
        if secret_code=="ERROR":
            for x in range (100000000000000000000):
                print("ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR     ERROR")
                print("")

        if secret_code=="AMOGUS":
            for x in range (100000000000000000000):
                print("AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS     AMOGUS")
                print("")

        if secret_code=="ABOBUS":
            for x in range (100000000000000000000):
                print("ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS     ABOBUS")
                print("")

        if secret_code=="13579":
            for x in range (100000000000000000000):
                print("ё1234567890-=йцукенгшщзхъфывапролджэ\\ячсмитьбю.     ё1234567890-=йцукенгшщзхъфывапр.     ё1234567890-=йцукенгшщзхъфывапролджэ\\ячсмитьбю.     ё1234567890-=йцукенгшщзхъфывапролджэ\\ячсмитьбю.")
                print("")
        if secret_code == "HELLOOO":
            for x in range(100000000000000000000):
                print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                print("")
        if secret_code == "hehe":
            if pc_or_mobile == "y" or pc_or_mobile == "yes":
                import subprocess
                def restart_computer():
                    subprocess.call(["shutdown", "-r", "-t", "15"])
                restart_computer()
                print("15 SECONDS TO RESTART")
                for x in range (10000):
                    print("hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe hehe")
                    
            else:
                time.sleep(2)
                print("ERROR")
                time.sleep(0.5)
                print("You're not on PC")
                time.sleep(0.8)
                cycle_yes_no = str(input("Restart the programm? Y/n: ")).lower()
                if cycle_yes_no == "yes" or cycle_yes_no == "y":
                    time.sleep(2)
                    for x in range(55):
                        print("")
                    cycle = True
                else:
                    print("PROGRAMM TURNED OFF")
                    

        else:
            print("SUS")
            print("PROGRAMM TURNED OFF")

#INFORMATION  MENU
    elif language=="in":
        print("             INFORMATION:                ")
        print("                                         ")
        print("  \\              /\\              /     ")
        print("   \\            /  \\            /      ")
        print("    \\          / E  \\          /       ")
        print("     \\        /   P  \\        /        ")
        print("      \\      /   O    \\      /         ")
        print("       \\    /     N    \\    /          ")
        print("        \\  /     S      \\  /           ")
        print("         \\/       V      \\/            ")
        print("                                         ")
        print("         Version: 1.1.1.FULL             ")
        print("           CREATOR: WEPONSV              ")
        print("                                         ")
        print("             UPDDATE INFO:               ")
        print("                                         ")
        print("• NEW CODE: 'hehe' (ONLY ON PC!!!)       ")
        print("• A COOL SCENE IF YOU SELECT A LANGUAGE  ")
        print("• THE CPU NOW HAVE BREAKS IN THE DIALOG  ")
        print("• NOW THERE ARE ~520 LINES               ")
        print("• SOMETIMES THE PROGRAMM WORK WITH 'AGE' ")
        print("• MORE QUESTIONS IN THE DIALOG           ")
        print("• ADDED A CALCULATOR                     ")
        print("• ALL UPDATES WILL BE IN INFORMATION MENU")
        print("• MANY BUGS HAVE BEEN FIXED              ")
        print("                                         ")
        print("                                         ")
        print("       To continue press ENTER:          ")
        

        waiting=str(input())
        for x in range(135):
            print("")
        cycle = True

#CALCULATOR MENU
    elif language == "calc":
        calc_again = True
        while calc_again:
            n1 = int(input("Number 1: "))
            sign = str(input("*,/,+,-: "))
            n2 = int(input("Number 2: "))
            time.sleep(1)
            if sign == "/":
                if n2 == 0:
                    time.sleep(0.5)
                    print("Trying again...")
                    time.sleep(0.5)
                    print("ERROR: You can't divide to 0")
                else:
                    print(n1 / n2)
            elif sign == "*":
                print(n1 * n2)
            elif sign == "+":
                print(n1 + n2)
            elif sign == "-":
                print(n1 - n2)
            else:
                time.sleep(0.5)
                print("Trying again...")
                time.sleep(0.5)
                print("ERROR: What sign to operate?")
            time.sleep(0.8)
            
            calc_again = str(input("Again? Y/n: ")).lower()
            if calc_again == "no" or calc_again == "n":
                time.sleep(0.5)
                calc_again = False
                
                cycle_yes_no = str(input("Start The programm again? Y/n: ")).lower()
                if cycle_yes_no == "no" or cycle_yes_no == "n":  
                    time.sleep(0.5)
                    cycle = False
                else:
                    time.sleep(0.5)
                    cycle = True
            else:
                calc_again = True
                
#TURNING OFF MENU:
        else:
            print("PROGRAMM TURNED OFF")

    else:
        print("SUS")
        print("PROGRAMM TURNED OFF")