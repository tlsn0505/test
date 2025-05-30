import random

class RSP:
    def __init__(self):
        self.rsp = {'가위', '바위', '보'}
        self._score = 0
        self._round = 5
        
class rsp_rule(RSP):
    
    def __init__(self):
        super().__init__()
        self._rule = {
            '가위': '바위',
            '바위': '보',
            '보': '가위'
        }

    def play(self):
        print('가위바위보 ai를 이겨라🤖!!')
        print('총 5 Round가 진행됩니다.')
        print('※ 게임 중 "#"을 누르면 종료합니다\n')

        for i in range(self._round):
            print('Round {}'.format(i+1))
            choice = input('가위,바위,보 중 하나를 쓰시오 :').strip()

            if choice == '#':
                print('가위바위보 게임을 종료합니다')
                return
            
            if choice not in self.rsp:
                print('잘못 입력하셨습니다. 다음 Round로 넘어가겠습니다.')
                print('가위, 바위, 보를 정확히 입력하세요\n')
                continue

            ai_choice = random.choice(list(self.rsp))
            print(f'ai의 선택 : {ai_choice}'.format(ai_choice))

            if choice == self._rule[ai_choice]:
                print('이기셨습니다!!😀\n')
                self._score += 1
                
            elif choice == ai_choice:
                print('비겼습니다!!😐\n')

            else:
                print('허헉 지셨네요 다음엔 이겨보아요! 😅\n')

        print('게임 종료!!!')
        print('이긴 Round {} / {}'.format(self._score, self._round))
