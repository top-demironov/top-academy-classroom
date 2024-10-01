# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника,
# удаление сотрудника, поиск сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.


a = input('укажите путь к файлу с сотрудниками: ')

ofcTxt: str = ''
with open(a, encoding='utf-8') as f:
    ofcTxt = f.read()


class Office:
    def __init__(self, employees: list):
        employees: list = ofcTxt.split('\n')
        self._employees: list = employees

    def __str__(self):
        return f"{self._employees}"

    def app_employees(self, Empl):
        self._employees.append(f'{Empl}')

    def search(self, i):
        i = str(i)
        for empl in self._employees:
            if i == empl[0]:
                print(empl)
            elif i in empl:
                print(empl)

    def editEmpl(self, i):
        i = str(i)
        count = 0
        for empl in self._employees:
            if i == empl[0]:
                print(empl)
                self._employees[count] = input('введите данные сотрудника с изменениями: ')
            elif i in empl:
                print(empl)
                self._employees[count] = input('введите данные сотрудника с изменениями: ')
            count += 1

    def deleteEmpl(self, i):
        i = str(i)
        for empl in self._employees:
            if i == empl[0]:
                print(empl)
                a = input('Удалить сотрудника? (да|нет): ')
                if a == "да":
                    self._employees.remove(empl)
            elif i in empl:
                print(empl)
                a = input('Удалить сотрудника? (да|нет): ')
                if a == "да":
                    self._employees.remove(empl)

    def load(self, ofcArr: list) -> list:
        for empl in self._employees:
            ofcArr.append(empl)
        return list(ofcArr)


class Empl:
    def __init__(self, name: str, age: int):
        self._name: str = name
        self._age: int = age

    def __str__(self):
        return f"{self._name}, {self._age}"


ofcTxt = Office([])
ofcArr = []

print('Здраствуйте, это система "Сотрудники"!')
print('Тут вы можете:')
print('1 добавить сотрудника')
print('2 редактировать сотрудника')
print('3 удалить сотрудника')
print('4 найти сотрудника по имени, фамилии, отчеству, возрасу или первой букве фамилии')
print('5 показать всех сотрудников')
print('6 Сохранить и выйти')

menu = input("введите номер пункта меню: ")
while menu != '6':
    menf = []
    if menu == "1":
        ofcTxt.app_employees(Empl(input("Введите ФИО сотрдника: "), int(input("Введите возраст: "))))
        print('Сотрудник добавлен!')
        menu = input("введите номер пункта меню: ")
    elif menu == "2":
        ofcTxt.editEmpl(input('Какого сотрудника редактировать?: '))
        menu = input("введите номер пункта меню: ")
    elif menu == "3":
        ofcTxt.deleteEmpl(input('Какого сотрудника удалить?: '))
        menu = input("введите номер пункта меню: ")
    elif menu == '4':
        ofcTxt.search(input('Введите имя,фамилию,отчество первую букву фамилии или возраст: '))
        menu = input("введите номер пункта меню: ")
    elif menu == '5':
        menf: list = ofcTxt.load(menf)
        menf = ('\n').join(menf)
        print(("\n"), menf, ('\n'))
        menu = input("введите номер пункта меню: ")
    else:
        print('Ты чё дурак?!')
        menu = input("введите номер пункта меню: ")

ofcArr: list = ofcTxt.load(ofcArr)
ofcArr = ('\n').join(ofcArr)
print('идёт запись!')
with open(a, 'w', encoding='utf-8') as f:
    f.write(ofcArr)
print("Досвидания!:)")