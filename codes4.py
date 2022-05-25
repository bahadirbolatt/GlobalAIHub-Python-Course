while True:
    try:
        x = int(input("lütfen bir numara giriniz:"))
        print(x)
        break
    except ValueError:
        print("girilen değer bir numara değil, tekrar deneyin.")