import tkinter as tk

def compute_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def compute_pc(num):
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                return f"{num} is a composite number. {i} × {num//i} = {num}"
                break
        else:
            return f"{num} is a prime number." 
    else:
        return f"{num} is not a prime number." 

def compute_lcm(x, y, z=None):
    if z:
        if z > x:
            greater = x
        elif x > y:
            greater = y
        else:
            greater = z
        while(True):
            if((greater % x == 0) and (greater % y == 0) and (greater % z == 0)):
                lcm = greater
                break
            greater += 1
    else:
        if x > y:
            greater = x
        else:
            greater = y
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
    return lcm

def compute_hcf(x, y, z=None):
    global hcf
    if z:
        if z > x:
            smaller = x
        elif x > y:
            smaller = y
        else:
            smaller = z
        for i in range(2, smaller+2):
            if((x % i == 0) and (y % i == 0) and (z % i == 0)):
                hcf = i
    else:
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i 
    return hcf 

while True:
    try:
        mtype = input("HCF, LCM, p/c or factors: ")
        mtype = mtype.lower()
        if mtype == "hcf":
            sntype = input("2 or 3 numbers: ")
            ntype = int(sntype)
            if ntype == 2:
                hcfx, hcfy = input("x, y: ").split(", ")
                print(compute_hcf(int(hcfx), int(hcfy)))
            elif ntype == 3:
                hcfx, hcfy, hcfz = input("x, y, z: ").split(", ")
                print(compute_hcf(int(hcfx), int(hcfy), int(hcfz)))
        elif mtype == "lcm":
            sntype = input("2 or 3 numbers: ")
            ntype = int(sntype)
            if ntype == 2:
                lcmx, lcmy = input("x, y: ").split(", ")
                print(compute_lcm(int(lcmx), int(lcmy)))
            elif ntype == 3:
                lcmx, lcmy, lcmz = input("x, y, z: ").split(", ")
                print(compute_lcm(int(lcmx), int(lcmy), int(lcmz)))
        elif mtype == "p/c":
            snum = input("Number: ")
            print(compute_pc(int(snum)))
        elif mtype == "factors":
            snum = input("Number: ")
            print(*compute_factors(int(snum)), sep=", ")
        elif mtype == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid. Please try again.")
    except KeyboardInterrupt:
        print("exit\nExiting...")
        break