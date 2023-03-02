while True:
    print("복리계산기 입니다")
    A=float(input("현재 금액을 입력해주세요. :"))
    B=float(input("목표 수익률을 입력해주세요. :"))
    C=int(input("목표 기간을 입력해주세요. :"))
    for i in range (1,C+1):
          D=A*(1+(B*0.01))**i
          E=A*(1+(B*0.01))**(i-1)
          F=D-E
          G=((D/A)*100)-100
          print("%d일     수익:%d원     금액:%d원     수익률:%3f"%(i,F,D,G),'%')
          print("")
    
