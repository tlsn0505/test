import random

class RSP:
    def __init__(self):
        self.rsp = {'가위', '바위', '보'}
        self._score = 0
        self._round = 5
        
    def play(self):
        print('가위바위보 ai를 이겨라🤖!!')
        print('※ 게임 중 "#"을 누르면 종류합니다')

        for i in range(self._round):
            print('Round {}'.format(i+1))
            choice = input('가위,바위,보 중 하나를 쓰시오 :').strip()
            rounds = random.sample(self.rsp,k = 1)
            

            print('ai의 선택 : {}'.format(rounds))

            if choice == '#':
                print('가위바위보 게임을 종류합니다')
                break

            if choice == '가위' and rounds == '보':
                print('이기셨습니다!!😀')
                self._score += 1

            elif choice == '바위' and rounds == '가위':
                print('이기셨습니다!!😀')
                self._score += 1

            elif choice == '보' and rounds == '바위':
                print('이기셨습니다!!😀')
                self._score += 1

            elif choice == rounds:
                print('아쉽지만 비겼습니다.점수는 없어영😥')

            else:
                print('허헉 지셨네요 다음엔 이겨보아요! 😅')
        print('게임종류!!!')
        print('이긴 Round {} / {}'.format(self._score, self._round))              


        