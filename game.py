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
        name = input('이름을 입력하세요 : ').strip()
        print(f'{name} vs ai 가위바위보 대결🤖!!')
        print('총 5 Round가 진행됩니다.')
        print('※ 게임 중 "#"을 누르면 종료합니다\n')

        valid_round = 0  # 정상 입력 라운드 수
        for i in range(self._round):
            print('Round {}'.format(i+1))
            choice = input(f'{name}님 가위,바위,보 중 하나를 선택해주세요 :').strip()

            if choice == '#':
                print('가위바위보 게임을 종료합니다')
                return
            
            if choice not in self.rsp:
                print('잘못 입력하셨습니다. 패배로 처리됩니다. 다음 Round로 넘어갑니다.')
                print('가위, 바위, 보를 정확히 입력하세요\n')
                # 패배로 처리 (score 변화 없음, 라운드만 소모)
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
        # 이름과 승률 기록
        win_rate = self._score / self._round
        f =  open("record.txt", "a", encoding="utf-8")
        f.write(f"{name}님의 승률 {win_rate:.1f}\n")
        # 기록이 6줄 이상이면 맨 위 한 줄 삭제
        f = open("record.txt", "r", encoding="utf-8")
        lines = f.readlines()
        if len(lines) > 5:
            f =open("record.txt", "w", encoding="utf-8")
            f.writelines(lines[1:])
        f.close()