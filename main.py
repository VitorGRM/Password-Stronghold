import string
import  os
import  secrets
import random
import passwordmeter
import HandyTools
def Menu():
    HandyTools.Clean()
    print("Please, choose an option:")
    print()
    choice = input(" 1 - Generate passwords\n 2 - Test the stremght of your password\n 3 - Instructions\n 4 - Qiot\n")
    if choice == "1":
        GeneratePassword(CreateDataBase())
    elif choice == "2":
        TestPassword()
    elif choice == "3":
        Instructions()
    elif choice == "4":
        exit()
    else:
        input("Invalid option. Please, try again.")
        Menu()
def CreateDataBase():
    HandyTools.Clean()
    #The next lines will get data from user and organize them in 2d lists
    name = input("Please, insert your full name or any other words you like: ")
    if not name.isalpha or name.isspace():
        input("Invalid data. Please, enter only letters")
        GeneratePassword(CreateDataBase())
    name = name.split()
    for word in name:
        name[name.index(word)] = str(name[name.index(word)]).lower().capitalize()
    numbers = input("Please, insert your date of birth of any other number that you like and can remember. Please, "
                    "separate tem by spaces:")
    if not numbers.isalnum or numbers.isspace():
        input("Invalid data. Please, enter only numbers")
        GeneratePassword(CreateDataBase())
    numbers = numbers.split()
    provisory_signs = string.punctuation
    signs = []
    ind = 0
    for s in provisory_signs:
        signs.append(provisory_signs[ind])
        ind += 1
    #this is the 2d list that contains all info given by the user
    password_data_base = [
        name,
        numbers,
        signs,
    ]
    return password_data_base
def GeneratePassword(password_data_base):
    #this function receives the 2d list returned by the Generate password functiom
    HandyTools.Clean()
    counter = 0
    print("Random password combination:")
    while counter <= 8:
        password = ""
        while len(password)<8:
            #these are the indexes of the first level of password_data_base
            first_elemement = [0, 1, 2]
            #this will measure the lenght of each second level list in password_data_base
            second_element = list(map(len, password_data_base))
            for el in first_elemement:
                component = secrets.choice(first_elemement) #randomly pick an option
                password += password_data_base[component][secrets.randbelow((second_element[component]-1))]
        strenght, improvment = passwordmeter.test(password) #this check the strength of your password
        if int(strenght*100) >= 50:
            if int(strenght*100) >= 50 and int(strenght*100) <= 75:
                counter+=1
                print(password + "\t Good password. This password is " + str(int(strenght*100)) + "% strong!")
            elif int(strenght*100) > 75:
                counter += 1
                print(password + "\t Excelent password. This password is " + str(int(strenght*100)) + "% strong!")
    print()
    print("Smart passwords generator:")
    print()
    print("\t Fist shape:")
    options = 0
    #this loop will create 10 password randomly created under a defined shape
    while options < 10:
        selected_sign = secrets.choice(password_data_base[2][0:32])
        random_names = random.sample(password_data_base[0][0:], 2)
        smart_password1 = [selected_sign, random_names[0], secrets.choice(password_data_base[1][0:]), random_names[1], selected_sign]
        #now it is time to conver the smart_password list into a string
        smart_password1_str = ""
        listel = 0
        for i in smart_password1:
            smart_password1_str += smart_password1[listel]
            listel += 1
        strenght, improvment = passwordmeter.test(smart_password1_str)
        print(smart_password1_str + "\t This password is " + str(int(strenght*100)) + "% strong")
        options += 1
    print("\n Second shape:")
    options = 0
    while options < 10:
        selected_sign = secrets.choice(password_data_base[2][0:32])
        name = secrets.choice(password_data_base[0][0:])
        l = 0
        smart_password = ""
        while l < len(name):
            smart_password += str(name[l]).upper()
            l += 1
            if l < len(name):
                smart_password+= str(name[l]).lower()
                l+=1
        l = 0
        number = secrets.choice(password_data_base[1][0:])
        while l <len(number):
            smart_password += number[l] + selected_sign
            l += 1
        strenght, improvment = passwordmeter.test(smart_password)
        print(smart_password + "\t This password is " + str(int(strenght*100)) + "% strong")
        options += 1
    retry  = input("Would like to randomize the passwords with sameinformations? Type Y to restart the randomiezer")
    retry = retry.upper()
    if retry == "Y":
        GeneratePassword(password_data_base)
    else:
        menu_retry = input("Would to like to return to the menu? Type Y to go back to the main menu, or type N to "
                           "leave the app")
        menu_retry = menu_retry.upper()
        if menu_retry == "Y":
            Menu()
        else:
            exit()

def TestPassword():
    #this function receives a password by the user and tests its strength
    HandyTools.Clean()
    psswd = input("Please, insert your password: ")
    strength, improovement = passwordmeter.test(psswd)
    print("Your password " + psswd + " is " + str(int(strength*100)) + "% strong")
    retry = input("would you like to try again? Type Y for yes and N for no \n")
    if retry.upper() == "Y":
        Menu()
    else:
        exit()
def Instructions():
    instructions = "This application features two main functionalities. The first one is to randomly generate strong " \
                   "passwords containing data that users inserts. The second functionality tests the strength of a " \
                   "password given by the user. Makke sure to insert all the information properly and do not mix " \
                   "datatyoes, otherwise the application will exposa an error message. The complexity and variety of " \
                   "data inserted will directly interfere in how easy the password is to remember. Maybe it would be " \
                   "a nice idea to randomize the password many timesu ntil your find a password that matches yourself "
    HandyTools.TextAnimatio(instructions)
    input("Hit Enter and return ti the main menu")
    Menu()
Menu()
input("finished")