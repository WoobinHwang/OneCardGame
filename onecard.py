import random

# # 자주 쓸 것 같은 동작

# 카드 특성 뽑기
# target = card_list[51]
# test = target.split(" ")

# # 사용자 정의 함수
# 게임 세팅
def game_setting(how_many):
    for i in range(how_many):
        users.append([])
    # print(users)
        
    pattern_limit = ["♥ ", "♣ ", "♠ ", "◆ "]
    number_limit = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    for i in pattern_limit:
        for j in number_limit:
            card_one = str(i) + str(j)
            card_list.append(card_one)
    # card_list.append("컬러 조커", "흑백 조커")
    # print(len(card_list))
    print("카드가 다 있군요!")

# 덱 섞기
def shuffle():
    for i in range(len(card_list)):
        using_deck.append(card_list[i])
    print("셔플중입니다...")


# 덱에서 카드 뽑기
# n: 뽑을 카드 개수 , user: 카드를 뽑을 사람
def card_draw(n, user):
    n = int(n)
    user = int(user) - 1
    for i in range(n):
        print(i+1 , " 번째 카드!")
        draw_card = random.choice(using_deck)
        using_deck.remove(draw_card)
        print(draw_card)  
        users[user].append(draw_card)
        

        if len(using_deck) == 0 :
            print("남은 카드가 없으므로 셔플하겠습니다...")
            shuffle()
    print(len(using_deck), "장 남았습니다")

# 내 카드 패  user 핸드 개수 출력
def hand_info():
    for i in range(len(users)):
        if i == 0:
            print("나의 카드 " ,users[i])
            # print("testing")
        else:
            print(i+1, "번째 유저", len(users[i]) , " 장 들고있습니다.")
            # print("testing")

# n번째 카드 내기
def select_card(card):
    users[0].remove(card)
    print("remove!")



# 메인 코드        
using_deck = []
card_list = []
users = []
            
if __name__ == "__main__":
    # 기본 세팅
    game_setting(3)
    shuffle()
    # 동작 테스트
    card_draw(5, 1)
    card_draw(2, 2)
    card_draw(3, 3)
    
    hand_info()

    while True:
        n= input("Do Action! ")

        if n == "draw" :
            card_draw()

        try:
            for i in range(len(users[0])):
                if users[0][i] == n:
                    select_card(n)
                    hand_info()
                
        except ValueError:
            print("다시 입력하세요.")
        except IndexError:
            # print('다시@@')
            continue

            
                
                
                    

        # if str(type(n))== "<class 'str'>":

        #     try: 
        #         select_card(n)
        #         hand_info()
        #     except ValueError:
        #         print("다시 입력하세요.")

        # else:
        #     print("입력해주시기 바랍니다.")

