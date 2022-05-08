import random

# # 자주 쓸 것 같은 동작

# 카드 특성 뽑기
# target = base_list[51]
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
            base_list.append(card_one)
    # base_list.append("컬러 조커", "흑백 조커")
    # print(len(base_list))
    print("카드가 다 있군요!")

    for i in range(len(base_list)):
        deck_list.append(base_list[i])
    print("deck_list로 게임을 시작합니다!!")


# 덱이 비었으면 덱 섞기
def shuffle():
    for i in range(len(using_deck) - 1):
        
        if i == len(list) - 1:
            target = using_deck[i]

        else:
            deck_list.append(using_deck[i])


    # print(target)

    using_deck.clear()
    using_deck.append(target)

    print("덱이 비어 셔플합니다...")


# 덱에서 카드 뽑기
# n: 뽑을 카드 개수 , user: 카드를 뽑을 사람
def card_draw(n, user):
    n = int(n)
    user = int(user) - 1
    for i in range(n):
        print(i+1 , " 번째 카드!")
        draw_card = random.choice(deck_list)
        deck_list.remove(draw_card)
        print(draw_card)  
        users[user].append(draw_card)
        

        if len(deck_list) == 0 :
            print("남은 카드가 없으므로 셔플하겠습니다...")
            shuffle()
    print(len(deck_list), "장 남았습니다")

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

# 



# 메인 코드        

# # 기본이 될 카드 목록
base_list = []
# # 사용할 덱
deck_list = []
# # 사용한 카드
using_deck = []
# # 유저 목록 + 핸드 목록
users = []
            

# 코드 돌리기
if __name__ == "__main__":
    # 기본 세팅
    game_setting(3)
    # shuffle()
    # 동작 테스트
    card_draw(5, 1)
    card_draw(5, 2)
    card_draw(5, 3)
    
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

