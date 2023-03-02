while True:
    print("$$$$순환매 계산기$$$")
    print('')
    print("")
    K=float(input("    레버리지를 입력하세요. : "))
    print("")
    A=float(input("    첫 진입가격을 입력하세요. : "))
    print("")
    B=float(input("    첫 진입 시드 총액을 입력하세요. : "))
    print("")
    C=float(input("    성공한 진입가격을 입력하세요. : "))
    print("")
    D=float(input("    성공한 매도가격을 입력하세요. : "))
    print("")
    E=float(input("    매수 진입 시드 총액을 입력하세요. : "))
    print("")
    F=float(input("    실제 매도 시드 총액을 입력하세요. : "))
    print("")
    J=int(input("    포지션 입력해주세요(롱=1 or 숏=2): "))
    print("")
    print("")
    print("")
    
    if J==1:
        print("롱  순환매 성공 후의 실질 평단가를 알려드리겠습니다.")
        print("")
        G=((D-C)/C)*K*(F/E)
        H=(K/(K+G))*A
        print("          %d원"%H)
    else:
        print("숏  순환매 성공 후의 실질 평단가를 알려드리겠습니다.")
        print("")
        G=((C-D)/C)*K*(F/E)
        H=(K/(K-G))*A
        print("          %d원"%H)


