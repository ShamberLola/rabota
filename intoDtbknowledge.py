from psycopg2 import Error
import psycopg2.extras

try:
    connection = psycopg2.connect(user="postgres",
                                  password="hohol",
                                  host="localhost",
                                  port="5432",
                                  database="washing_machine")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print("You are connected to base")

except (Exception, Error) as error:
    raise TypeError("Error while connecting to PostgreSQL", error)

knowledge = [
    ('A', '1:30', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'LG', 2022),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Samsung', 2023),
    ('A+', '1:45', 'Тихая работа', 'Энергосберегающий режим', 'Bosch', 2021),
    ('A++', '1:20', 'Быстрая стирка', 'Функция отложенного старта', 'Whirlpool', 2022),
    ('B', '2:30', 'Большой объем загрузки', 'Система антиаллергия', 'Ariston', 2020),
    ('A', '1:50', 'Интеллектуальная система управления', 'Сенсорное управление', 'Daewoo', 2021),
    ('A++', '1:40', 'Система защиты от детей', 'Функция пара', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022),
    ('A', '1:45', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'Whirlpool', 2021),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Функция отложенного старта', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчив ность к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022),
    ('A', '1:45', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'Whirlpool', 2021),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Функция отложенного старта', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022),
    ('A', '1:45', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'Whirlpool', 2021),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Функция отложенного старта', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30 ', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022),
    ('A', '1:45', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'Whirlpool', 2021),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Функция отложенного старта', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022),
    ('A', '1:45', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'Whirlpool', 2021),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Функция отложенного старта', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++ ', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022),
    ('A', '1:45', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'Whirlpool', 2021),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Функция отложенного старта', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022),
    ('A', '1:45', 'Уникальная система стирки', 'Эффективная стирка при низких температурах', 'Whirlpool', 2021),
    ('B', '2:00', 'Система защиты от протечек', 'Автоматическая дозировка моющего средства', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Функция отложенного старта', 'Haier', 2022),
    ('B+', '2:10', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Система самоочистки', 'Быстрая стирка 15 минут', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от перегрева', 'Функция предварительной стирки', 'Bosch', 2022),
    ('A', '1:35', 'Система контроля пены', 'Функция быстрой стирки', 'Whirlpool', 2021),
    ('B', '2:15', 'Система защиты от протечек', 'Функция отложенного старта', 'Ariston', 2020),
    ('A+', '1:50', 'Тихая работа', 'Энергосберегающий режим', 'Daewoo', 2021),
    ('A++', '1:40', 'Быстрая стирка', 'Система антиаллергия', 'Haier', 2022),
    ('B+', '2:05', 'Устойчивость к вибрациям', 'Эко-режим', 'LG', 2023),
    ('A', '1:30', 'Интеллектуальная система управления', 'Сенсорное управление', 'Samsung', 2021),
    ('A++', '1:25', 'Система защиты от детей', 'Функция пара', 'Bosch', 2022)
]


try:

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id SERIAL PRIMARY KEY,
            energy VARCHAR(10),
            time VARCHAR(10),
            dimensions VARCHAR(100),
            advantage VARCHAR(100),
            brand VARCHAR(50),
            year INTEGER
        )
    ''')

    insert_query = '''
          INSERT INTO knowledge (energy, time, dimensions, advantage, brand, year)
          VALUES (%s, %s, %s, %s, %s, %s)
        '''
    cursor.executemany(insert_query, knowledge)

    connection.commit()
    print(f"{cursor.rowcount} записей добавлено в таблицу.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

