# 가상 커피 머신 시스템 (Coffee Machine Simulator)

파이썬의 **함수 지향 프로그래밍**과 **전역 상태 관리**를 실습하기 위한 가상 시뮬레이터입니다. `MENU` 데이터를 활용하여 리소스를 관리하고, 사용자로부터 동전 입력을 받아 커피를 제조하는 로직을 구현했습니다.

### 주요 기능
* **재료 관리**: 음료 제조 시 물, 우유, 커피 원두의 잔량을 체크하고 실시간으로 차감합니다.
* **코인 프로세서**: 쿼터, 다임, 니켈, 페니 동전을 입력받아 총 합계 금액을 계산합니다.
* **결제 시스템**: 투입 금액 확인 후 거스름돈 계산(반올림 처리) 및 수익금을 관리합니다.
* **머신 리포트**: 현재 남은 재료와 누적 수익 상태를 실시간으로 출력합니다.

### 실행 방법 및 학습 포인트

```bash
# 1. 저장소 클론 (내 컴퓨터로 코드 복사)
git clone [https://github.com/sujih7-hwang/python-coffee-machine-mini_project-1.git](https://github.com/sujih7-hwang/python-coffee-machine-mini_project-1.git)

# 2. 프로젝트 폴더로 이동
cd python-coffee-machine

# 3. 프로그램 실행
python main.py
💡 학습 포인트 (Learning Points)
global 키워드: profit, resource 등 전역 변수의 상태를 함수 내부에서 수정하는 법 숙지

중첩 딕셔너리(Nested Dictionary): 복잡한 메뉴 레시피 데이터를 구조화하고 추출하는 방법

부동 소수점 오차 방지: 금융 계산 시 발생할 수 있는 오차를 round() 함수로 해결

비즈니스 로직 설계: (재료 확인 -> 결제 -> 제조)로 이어지는 단계별 조건문 처리 루틴 실습
