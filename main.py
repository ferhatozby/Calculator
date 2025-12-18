def start1():
    ok= input("Başlamak İçin X e Basınız: ")

    if ok != "X":
        while ok!="X":
            ok=input("Başlamak İçin X e Basınız: ")

def get_numbers():
    try:

        sayi1=input("Birinci Sayıyı Giriniz: ")

        sayi2 =input("İkinci Sayıyı Giriniz: ")
        if sayi2==int(sayi2) and sayi1==int(sayi1):
            print()
    except ValueError:
        print("Lütfen Sayı Giriniz: ", get_numbers())




    print("+"

          " -"
          
          " *"
          
          " /")
    sayi=input("Lütfen Operatörlerden Biriniz Basınız: ")

    while sayi!="+"and sayi!="-" and sayi!="*"and sayi!="/":

        sayi=input("Lütfen Operatörlerden Biriniz Basınız: ")


    if sayi=="+":
        print("Sonucunuz", sayi1+sayi2)
    if sayi=="-":
        print("Sonucunuz", sayi1-sayi2)
    if sayi=="*":
        print("Sonucunuz", sayi1*sayi2)
    if sayi=="/":
        print("Sonucunuz", sayi1/sayi2)
def main():
    go=input("Devam Etmek İster Misiniz (Evet/Hayır): ")
    if go=="Evet"or go=="evet":

        start1()
        get_numbers()

    if go=="hayır"or go=="Hayır":
        print("Bizi Tercih Ettiğiniz İçin Teşekkürler")
    else:
        main()

print(start1())
print(get_numbers())


print(main())
