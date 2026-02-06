"""
Coffee Machine Program
작성일: 2026-01-08
설명: 전역 변수로 재료 상태를 관리하고, 사용자 입력을 받아 커피 제조 및 정산을 처리하는 시뮬레이터.
"""

# 커피 메뉴 데이터 (재료 배합비율 및 가격)
MENU = {
    'espresso': {
        'ingredients': {'water': 50, 'coffee': 18},
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {'water': 200, 'milk': 150, 'coffee': 24},
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {'water': 250, 'milk': 100, 'coffee': 24},
        'cost': 3.0
    }
}

# 머신 현재 상태 관리용 전역 변수
profit = 0
resource = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

def is_resource_sufficient(order_ingredients):
    """
    현재 남은 재료(resource)가 주문한 음료 레시피를 감당할 수 있는지 체크함.
    부족한 재료가 하나라도 있으면 바로 안내 메시지 띄우고 중단.
    """
    for item in order_ingredients:
        # 주문 요구량이 현재 보유량보다 크면 재료 소진으로 판단 
        if order_ingredients[item] > resource.get(item, 0):
            print(f'죄송합니다. {item} 재료가 부족합니다.')
            return False
    return True

def process_coins():
    """
    사용자로부터 4종류의 동전 개수를 각각 입력받아 총 합계 금액을 달러($)로 환산.
    """
    print("동전을 넣어주세요.")
    coins = {
        'quarter': 0.25,
        'dimes': 0.10,
        'nickels': 0.05,
        'pennies': 0.01
    }
    total_money = 0
    for coin, value in coins.items():
        count = int(input(f'{coin} 코인 개수 : '))
        total_money += count * value
    return total_money

def is_transaction_successful(money_received, drink_cost):
    """
    투입된 금액이 가격보다 높은지 확인하고, 성공 시 수익금 가산 및 거스름돈 계산.
    부동소수점 오차 방지를 위해 round 처리함.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)  
        global profit
        profit += drink_cost
        print(f'거스름돈 ${change}를 돌려드립니다.')
        return True
    
    print('죄송합니다. 금액이 부족합니다. 돈이 환불되었습니다.')
    return False

def make_coffee(drink_name, order_ingredients):
    """
    커피 제조 확정 시 실행. 전역 변수인 resource에서 사용한 재료만큼 차감 처리.
    """
    global resource
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f'여기 {drink_name}가 나왔습니다. 즐기세요!')

# --- 메인 비즈니스 로직 루프 ---
while True:
    choice = input('\n어떤 음료를 원하시나요?\n(espresso/latte/cappuccino/off/report) : ').lower()
    
    if choice == 'off':
        # 시스템 셧다운
        print("커피 머신을 종료합니다.")
        break
    
    elif choice == 'report':
        # 머신 현재 관리 상태(재료 잔량, 수익금) 리포트 출력
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${profit}")
    
    else:
        # 메뉴 존재 여부 확인 후 단계별 프로세스(재료 확인 -> 결제 -> 제조) 진행
        drink = MENU.get(choice)
        if drink:
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink["ingredients"])
        else:
            print('잘못된 입력입니다. 메뉴 이름을 정확히 입력해주세요.')
