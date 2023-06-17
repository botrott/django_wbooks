from insert.insert import response_menu

SEPARATOR = 62
SEPARATOR_MENU = 60

if __name__ == '__main__':
    print(f'|{"typedt":+^{SEPARATOR_MENU}}|')
    print(f'|{"Добро пожаловать в typedt":+^{SEPARATOR_MENU}}|')
    print(f'|{"":+^{SEPARATOR_MENU}}|')

    with open('text/start.txt') as file:
        for i in file.readlines():
            print(f'|{i.strip():^{SEPARATOR_MENU}}|')
    try:
        while True:
            print('=' * SEPARATOR)
            print('Вы находитесь в <Главном меню>, введите нужную команду')
            INSERT = input('a => Aлгоритмы, c => Структуры данных, q <=> Выход : ').lower()
            print('=' * SEPARATOR)
            if INSERT in 'qй':
                break
            if INSERT in 'фаafcс':
                response_menu(INSERT)
            else:
                print('введите команду!')

    except KeyboardInterrupt:
        print('[аА] - алогоритмы, [qQ] - выход, [cC] - структуры')
