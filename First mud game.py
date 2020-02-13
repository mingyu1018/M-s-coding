# -*- Encoding: utf-8 -*-

def inventory1():
    print(f"다음은 {name}의 주머니속 물건들입니다.")
    print("무엇을 사용하시겠습니까?")
    ic = input('1.1000원')
    if ic == 1:
        print("1000원을 사용합니다.")

    else:
        print("잘못 누르셨습니다.-----------")
        inventory1()



def Start2():
    a = """당신은 집에 있습니다. 어디로 이동하시겠습니까?
            1. 마을 2. 생선가게 3. 이준상네 집 4.화장실
            """
    print(a)
    b = input('숫자를 누르세요. : ')

    if b == '1':
        print("마을로 이동하였습니다.--------------")
        village1()
    elif b == '2':
        print("생선가게로 이동하였습니다.----------------")
        time.sleep(3)
        print("생선에게 잡아 먹혔습니다.---------------")
        Start2()
    elif b == '3':
        print("이준상네 집으로 이동하였습니다.--------------")
        jsHouse2()
    elif b == '4':
        print("아까 갔습니다.------------------")
        Start2()
        time.sleep(fset)
    else:
        print("잘못 누르셨습니다.------------------")



def toilet():
    print(f"{name} : 아 오줌마려워..")
    time.sleep(fset)
    print(f"{name} : 어 이게 뭐야")
    time.sleep(fset)
    print(f"{name}은(는) 화장실에 떨어져있던 1000원을(를) 발견 하였다.")
    print("1000원을(를) 주머니에 넣었습니다.")
    time.sleep(fset)
    print("주머니에 있는 물건은 E 키를 눌러 열 수 있습니다.----------------------")
    time.sleep(fset)
    Start2()



def Start():
    a = """당신은 집에 있습니다. 어디로 이동하시겠습니까?
        1. 마을 2. 생선가게 3. 이준상네 집 4.화장실
        """
    print(a)
    b = input('숫자를 누르세요. : ')
    if b == '1':
        print("마을로 이동하였습니다.--------------")

        village1()
    elif b == '2':
        print("생선가게로 이동하였습니다.-----------------")
        time.sleep(3)
        print("당신은 생선에게 잡아 먹혔습니다.----------------")
        time.sleep(fset)
        Start()
    elif b == '3':
        print("이준상네 집으로 이동하였습니다.---------------------")
        jsHouse1()
    elif b == '4':
        print("화장실로 이동하였습니다.--------------------")
        toilet()
    else:
        print("잘 못 누르셨습니다.-------------------")
        Start()



def village1():
    c = """당신은 마을에서 친구 이준상을 만났습니다. 무엇을 하시겠습니까?
        1. 인사한다 2. 한 대 친다 3. 몰래 숨는다 4. 다시 집으로 돌아간다
        """
    print(c)
    d = input('숫자를 누르세요. : ')
    if d == '1':
        print("이준상(이)에게 인사했습니다.")
        time.sleep(fset)
        print(f"{name} : 준상아 여기서 뭐해?")
        time.sleep(fset)
        print("??? : 누구세요?")
        print("(그 사람은 사실 이준상이 아닌 이준상과 닮은 사람이었습니다.)")
        time.sleep(fset)
        print(f"{name}은(는) 너무 부끄러운 나머지 집으로 도망갔습니다.--------------")
        gameover()
    elif d == '2':
        print("/'그/'(을)를 칠 수 없습니다.---------------------")
        gameover()
    elif d == '3':
        print("이준상 몰래 숨었습니다.")
        time.sleep(fset)
        print("이준상 : 여기서 뭐해..?")
        print("그를 피할 수는 없었습니다.--------------------")
        gameover()
        
    elif d == '4':
        print("다시 집으로 돌아갑니다...---------------------------------")
        Start()
    else:
        print("잘 못 누르셨습니다.-----------------------")
        village1()



def jsHouse1():
    time.sleep(fset)
    print(f"{name} : 준상이 혹시 여기 있나요?")
    time.sleep(fset)
    print("이준상 엄마 : 준상이는 아까 밖으로 나갔어.")
    time.sleep(fset)
    print(f"""{name} : 아 알겠습니다. 
 ---(다시 집으로 돌아 갑니다.)--""")
    time.sleep(fset)
    Start()
    
    

def jsHouse2():
    time.sleep(fset)
    print(f"{name} : 준상이 혹시 여기 있나요?")
    time.sleep(fset)
    print("이준상 엄마 : 준상이는 아까 밖으로 나갔어.")
    time.sleep(fset)
    print(f"""{name} : 아 알겠습니다. 
 ---(다시 집으로 돌아 갑니다.)--""")
    time.sleep(fset)
    Start2()



def ftxt(q,w,e,r,t):
    k = f"""{q}
         1.{w} 2.{e} 3.{r} 4.{t}"""
    print()
    

def gameover():
    print("게임을 종료합니다.---------------------------")
    return 0;








import time
global name
global fset
name = input('당신의 이름은? ')
faster = input('''게임의 속도를 정하세요.
1.느리게 2.보통 3.빠르게
''')
if faster == '1':
    fset = 2.7
    print("게임 속도를\"느리게\"로 설정합니다.-----------------")
elif faster == '2':
    fset = 2.1
    print("게임 속도를\"보통\"으로 설정합니다.------------------")
elif faster == '3':
    fset = 1.5
    print("게임 속도를\"빠르게\"로 설정합니다.--------------------")
else:
    print("잘못 누르셨습니다.--------------------")
time.sleep(2)
Start()










