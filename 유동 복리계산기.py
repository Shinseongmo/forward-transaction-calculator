while True:
    A=float(input("1. 전체 시드를 입력해주세요. : "))
    B=float(input("2. 몇 프로 진입하실건가요? : "))
    C=float(input("3. 목표수익률을 적어주세요.(일) : "))
    D=int(input("4. 목표일을 설정해주세요. : "))
    print("")
    print("")
    for i in range(0,D):
        E=A*(B/100)
        K=A-E
        F=E*(C/100)
        H=F*(B/100)
        E=int((F*(B/100))+E)
        I=int(K+(F-H))
        A=int(E+I)
        P=format(A,',')
        J=format(I,',')
        L=format(E,',')
        if i+1<9:
            print(i+1,"    일","             예비시드:",J,"원","               투입시드:",L,"원")
            print("")
        if i+1>9 and i+1<100:
            print(i+1,"   일","             예비시드:",J,"원","               투입시드:",L,"원")
            print("")
        if i+1>99 and i+1<1000:
            print(i+1,"  일","             예비시드:",J,"원","               투입시드:",L,"원")
            print("")
        if i+1>999 and i+1<10000:
            print(i+1," 일","             예비시드:",J,"원","               투입시드:",L,"원")
            print("")
    print("")
    print('')
    print("                   총시드는",P," 원"," 입니다.")
    print('')
    print('')
    print('')
    print('')
    print('')
    
    
