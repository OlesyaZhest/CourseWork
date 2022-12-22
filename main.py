from City import City
from API import API_KEY


if __name__ == "__main__":
    cities = [City('Tikhoretsk', API_KEY), City('Moscow', API_KEY), City('Saint-Petersburg', API_KEY)]
    command = ''

    while command != 'e':
        print('Текущий список городов: ')
        for num, city in enumerate(cities):
            print(num + 1, end='. ')
            city.show_city()

        print('\nУправление программой:\n',
              '\td - удалить город из списка\n',
              '\ti - добавить город в список\n',
              '\te - выйти из программы\n'
              '\tm - вывести более подробный прогноз погоды', sep='')
        command = input('Введите команду: ')
        print()

        if command == 'd':
            number = input('Введите номер города из списка: ')
            try:
                number = int(number)
                if number > len(cities) or number <= 0:
                    raise ValueError
                cities.pop(int(number) - 1)
            except ValueError:
                print('Некорректный номер')

        elif command == 'i':
            name = input('Введите название города на английском: ')
            if City.check_city_name(name, API_KEY):
                cities.append(City(name, API_KEY))
                print('Город добавлен!')
            else:
                print('Некорректное название города')

        elif command == 'm':
            number = input('Введите номер города из списка: ')
            try:
                number = int(number)
                if number > len(cities) or number <= 0:
                    raise ValueError
                for weather in cities[number - 1].get_more_weather()[::5]:
                    print(f'Дата: {weather.date}, описание: {weather.description}, '
                          f'температура: {weather.temp}, ' +
                          f'ощущается как: {weather.feels_like}')
            except ValueError:
                print('Некорректный номер!')

        else:
            print('Некорректная команда!')

        print()
