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

print(str(usd) + " USD = " + str(vnd) + "k VND")
