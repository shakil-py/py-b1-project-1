# -----------------------Input Data funtion-------------------------

food_item = input(
    "Please Enter Today Market item (like Chicken , Beef or fish) : ")
member = int(input("Please Enter amount of today Members : "))
market_cost = int(input("Pleasr enter foodMarket cost : "))
# food_item = set(input("Enter Today Food item : "))

# ---------------------------------------------------------
# ------------Constant/updateable Value------------

member_name = ["Shakil", "Babu", "Sadik", "Rayhan", "Morsed", "Ibrahim"]
food_list = ["beef", "chicken", "fish", "egg"]


# ----------------------------------------------------------
# ------------------Oparetion of Data funtion----------------------
# --------------------Other Funtion-----------------------------


def foodcycle():
    for i in range(len(food_list)):
        if food_list[i] == food_item:
            next_item = print("Next Market item is "+ food_list[i+1])
            return next_item

 # ---- Oparetion funtion


def millrate():
    millrate = market_cost/(member*6)
    return millrate

# --- Alart funtion---#


def alart():
    if millrate > 20:
        str1 = print("Maneger your millrate is high to Previouse day :( !!!")
        return str1
    elif millrate <= 20:
        str2 = print("Great job Maneger Continue Your manegment :)!")
        return str2
    else:
        pass


# --- Main App Funtion -----
millrate = millrate()
alart = alart()
foodcycle = foodcycle()


def mainapp():
    main = print(millrate, alart, foodcycle)
    return main


mainapp()
