from game import rsp_rule

def main():
    while True:
        try:
            num = input('게임을 시작 하시겠습니까?(진행:1, 종료:0) :')
            if num not in ('1', '0'):
                raise ValueError
        except ValueError:
            print('1 또는 0을 입력하세요.😕')
            continue
        
        if num == '0':
            print('게임을 종류합니다. 안녕히 가세요')
            break
        if num == '1':
            print('\n게임을 시작합니다\n')
            game = rsp_rule()
            game.play()
            while True:
                try:
                    num1 = input('\n게임을 다시 하시겠습니까?(진행:1, 종료:0) :')
                    if num1 not in ('1', '0'):
                        raise ValueError
                except ValueError:
                    print('1 또는 0을 입력하세요.😕')
                    continue
          
                if num1 == '0':
                    print('게임을 종류합니다. 다음에 또 찾아오세요 😊')
                    return
                if num1 == '1':
                    print('게임을 시작합니다')
                    game = rsp_rule()
                    game.play()

if __name__ == '__main__':
    main()