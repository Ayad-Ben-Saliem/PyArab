def اختبار():

    print('مرحبا def ')



س = 5

ص = 3



while س < 100:

    س += س/10



    if س - round(س) < 0.09:

        continue

    elif س - round(س) > 0.9:

        print("""***""")



    print(س, " >>>")

    for م in range(int(س)):

        print(م)



if س > ص:

    print("س أكبر من ص")

else :

    print("ص أكبر من س")



