<<<<<<< HEAD
while True:
    try:
        usd = int(input("Nhap USD:"))
        if usd < 0 :
            print("Nhap sai vui long nhap lai so nguyen: ")
        else :
            break
    except ValueError:
        print("Nhap sai vui long nhap lai so nguyen: ")

vnd = usd * 22
=======
usd = int(input("Nhap USD: "))
vnd = int(usd * 22)
>>>>>>> 393d2dc669a581a2af08416b786b2efb9eb250be

print(str(usd) + " USD = " + str(vnd) + "k VND")
