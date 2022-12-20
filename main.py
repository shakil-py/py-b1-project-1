# ------------Constant/updateable Value------------

member_name = ["Shakil", "Babu", "Sadik", "Rayhan", "Morsed", "Ibrahim"]
food_list = ["Beef", "Chicken", "fish"]

# ----------------------------------------------------------

# -----------------------Input Data funtion-------------------------

# today_market_item=input("Please Enter Today Market item (like Chicken , Beef or fish) : ")
member = int(input("Please Enter amount of today Members : "))
market_cost = int(input("Pleasr enter foodMarket cost : "))

# ---------------------------------------------------------

# ------------------Oparetion of Data funtion----------------------
# ---- Oparetion funtion


def millrate():
    millrate = market_cost/(member*3)
    return millrate

# --- Alart funtion---#


def alart():
    if millrate > 20:
        print("Maneger your millrate is high to Previouse day :( !!!")
    elif millrate <= 20:
        print("Great job Maneger Continue Your manegment :)!")
    else:
        pass


# --- Main App Funtion -----
millrate = millrate()
alart = alart()


def mainapp():
    return print(millrate, alart)


mainapp()
