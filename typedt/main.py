from insert.insert import response_menu

if __name__ == '__main__':
    print(f'|{"typedt":+^60}|')
    print(f'|{"Добро пожаловать в typedt":+^60}|')
    print(f'|{"":+^60}|')

    with open('text/start.txt') as file:
        for i in file.readlines():
            print(f'|{i.strip():^60}|')
    try:
        while True:
            print('=' * 200)
            print('Вы находитесь в <Главном меню>, введите нужную команду')
            INSERT = input('a => Aлгоритмы, c => Структуры данных, q <=> Выход : ').lower()
            print('=' * 200)
            if INSERT in 'qй':
                break
            if INSERT in 'фаafcс':
                response_menu(INSERT)
            else:
                print('введите команду!')

    except KeyboardInterrupt:
        print('[аА] - алогоритмы, [qQ] - выход, [cC] - структуры')
