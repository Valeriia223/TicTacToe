import random


class TicTacToe:
    def __init__(self):
        # Список, в котором фиксируются уже занятые клетки
        self.used_cells = []
        # Перечень всех клеток, доступных в игре
        self.all_cells = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        # Перечень клеток, доступных для хода компьютера
        self.available_cells_for_computer = self.all_cells
        self.all_moves_p = []
        self.all_moves_c = []
        self.win_options = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22'],
                            ['00', '10', '20'], ['01', '11, 21'], ['02', '12', '22'],
                            ['00', '11', '22'], ['02', '11', '20']]
        self.n = 0
        self.P = ''

    def set_used_cells(self, move):
        self.used_cells.append(move)

    def get_used_cells(self):
        return self.used_cells

    def get_all_cells(self):
        return self.all_cells

    def set_available_cells_for_computer(self, move):
        self.available_cells_for_computer.remove(move)

    def get_available_cells_for_computer(self):
        return self.available_cells_for_computer

    def set_all_moves_p(self, move):
        self.all_moves_p.append(move)

    def get_all_moves_p(self):
        return self.all_moves_p

    def set_all_moves_c(self, move):
        self.all_moves_c.append(move)

    def get_all_moves_c(self):
        return self.all_moves_c

    def set_n(self, i):
        self.n += i

    def get_n(self):
        return self.n

    def set_P(self):
        self.P = str(input('Вы будете играть "x" или "0"? '))

    def get_P(self):
        return self.P

    def cancel(self, i):
        if TicTacToe.get_P(self) == 'x':
            for j in range(len(self.used_cells)-(2*i), len(self.used_cells), 1):
                self.available_cells_for_computer.append(self.used_cells[j])
            i = -i
            del self.used_cells[(2*i):]
            del self.all_moves_p[i:]
            del self.all_moves_c[i:]
            TicTacToe.set_n(self, i)
        elif TicTacToe.get_P(self) == '0':
            for j in range(len(self.used_cells)-(2*i)-1, len(self.used_cells), 1):
                self.available_cells_for_computer.append(self.used_cells[j])
            i = -i
            del self.used_cells[((2 * i)-1):]
            del self.all_moves_p[i:]
            del self.all_moves_c[(i-1):]
            TicTacToe.set_n(self, i)

    def check_used_cells(self, move):
        if move in TicTacToe.get_used_cells(self):
            return False
        else:
            return True

    def move_cancel(self):
        c = int(input('Сколько ходов вы хотите отменить? '))
        if c <= TicTacToe.get_n(self):
            TicTacToe.cancel(self, c)
            if TicTacToe.get_P(self) == 'x':
                TicTacToe.func_px(self)
            elif TicTacToe.get_P(self) == '0':
                TicTacToe.func_p0(self)
        else:
            print('Ошибка. Столько ходов ещё не было сделано')
            TicTacToe.move_p(self)

    # описывает ход пользователя
    def move_p(self):
        move_p = str(input('Ваш ход: '))
        if move_p == 'cancel':
            TicTacToe.move_cancel(self)
        else:
            if not (move_p in TicTacToe().get_all_cells()):
                print('Ошибка: Выход за пределы поля')
                return TicTacToe.func_px(self)
            if TicTacToe.check_used_cells(self, move_p) == False:
                print('Ошибка: Эта клетка уже занята')
                TicTacToe.move_p(self)
            else:
                TicTacToe.set_used_cells(self, move_p)
                TicTacToe.set_available_cells_for_computer(self, move_p)
                TicTacToe.set_all_moves_p(self, move_p)
                TicTacToe.set_n(self, 1)

    def move_c(self):
        move_c = str(random.choice(TicTacToe.get_available_cells_for_computer(self)))
        print('Ход компьютера:', move_c)
        TicTacToe.set_available_cells_for_computer(self, move_c)
        TicTacToe.set_all_moves_c(self, move_c)
        TicTacToe.set_used_cells(self, move_c)
        print('Занятые клетки: ', TicTacToe.get_used_cells(self))

    #вызывается, если пользователь ходит "x":
    def func_px(self):
        if TicTacToe.get_n(self) < 3:
            print('Ход № ', TicTacToe.get_n(self) + 1)
            TicTacToe.move_p(self)
            TicTacToe.move_c(self)
            TicTacToe.func_px(self)
        if TicTacToe.get_n(self) == 3:
            if TicTacToe.check_win(self) == False:
                print('Ход № ', TicTacToe.get_n(self) + 1)
                TicTacToe.move_p(self)
                TicTacToe.move_c(self)
                TicTacToe.check_win_1(self)

    # вызывается, если пользователь ходит "0":
    def func_p0(self):
        if TicTacToe.get_n(self) < 3:
            print('Ход № ', TicTacToe.get_n(self) + 1)
            TicTacToe.move_c(self)
            TicTacToe.move_p(self)
            TicTacToe.func_p0(self)
        if TicTacToe.get_n(self) == 3:
            if TicTacToe.check_win(self) == False:
                print('Ход № ', TicTacToe.get_n(self) + 1)
                TicTacToe.move_c(self)
                TicTacToe.move_p(self)
                TicTacToe.check_win_1(self)

    def check_win(self):  # Проверка выигрыша
        if (sorted(TicTacToe.get_all_moves_p(self)) in self.win_options
                and sorted(TicTacToe.get_all_moves_c(self)) in self.win_options):
            print('Вы сыграли в ничью! Поздравляем и желаем удачи в следующей игре!')
            return True
        elif sorted(TicTacToe.get_all_moves_p(self)) in self.win_options:
            print('Вы выиграли:) Поздравляем с победой!')
            return True
        elif sorted(TicTacToe.get_all_moves_c(self)) in self.win_options:
            print('Вы проиграли:( Желаем удачи в следующей игре!')
            return True
        else:
            return False

    def check_win_1(self):
        all_moves_p_1 = sorted(TicTacToe.get_all_moves_p(self)[:3])
        all_moves_p_2 = (TicTacToe.get_all_moves_p(self)[0],
                         TicTacToe.get_all_moves_p(self)[1],
                         TicTacToe.get_all_moves_p(self)[3])
        all_moves_p_2 = sorted(list(all_moves_p_2))
        all_moves_p_3 = (TicTacToe.get_all_moves_p(self)[0],
                         TicTacToe.get_all_moves_p(self)[2],
                         TicTacToe.get_all_moves_p(self)[3])
        all_moves_p_3 = sorted(list(all_moves_p_3))
        all_moves_p_4 = sorted(TicTacToe.get_all_moves_p(self)[1:])
        all_moves_c_1 = sorted(TicTacToe.get_all_moves_c(self)[:3])
        all_moves_c_2 = (TicTacToe.get_all_moves_c(self)[0],
                         TicTacToe.get_all_moves_c(self)[1],
                         TicTacToe.get_all_moves_c(self)[3])
        all_moves_c_2 = sorted(list(all_moves_c_2))
        all_moves_c_3 = (TicTacToe.get_all_moves_c(self)[0],
                         TicTacToe.get_all_moves_c(self)[2],
                         TicTacToe.get_all_moves_c(self)[3])
        all_moves_c_3 = sorted(list(all_moves_c_3))
        all_moves_c_4 = sorted(TicTacToe.get_all_moves_c(self)[1:])
        if ((
                all_moves_p_1 in self.win_options or all_moves_p_2 in self.win_options
                or all_moves_p_3 in self.win_options or all_moves_p_4 in self.win_options)
                and (all_moves_c_1 in self.win_options or all_moves_c_2 in self.win_options
                     or all_moves_c_3 in self.win_options or all_moves_c_4 in self.win_options)):
            print('Вы сыграли в ничью! Поздравляем и желаем удачи в следующей игре!')
            return True
        elif (all_moves_p_1 in self.win_options or all_moves_p_2 in self.win_options
              or all_moves_p_3 in self.win_options or all_moves_p_4 in self.win_options):
            print('Вы выиграли:) Поздравляем с победой!')
            return True
        elif (all_moves_c_1 in self.win_options or all_moves_c_2 in self.win_options
              or all_moves_c_3 in self.win_options or all_moves_c_4 in self.win_options):
            print('Вы проиграли:( Желаем удачи в следующей игре!')
            return True
        else:
            print('Ничья! Ни вы, ни компьютер не подобрали выигрышную стратегию:( '
                  'Желаем удачи в следующей игре!')
            return False

    def play(self):
        print('Ваше поле для игры в крестики-нолики:')
        print('  0 1 2')
        print('0 - - -')
        print('1 - - -')
        print('2 - - -')
        TicTacToe.set_P(self)
        print('Чтобы сделать ход, введите клетку, в которой хотите поставить x или 0 \n'
              'и введите её номер в форме  ij, где i - номер строки, j - номер столбца. \n'
              'Чтобы отменить один или несколько ходов, \n'
               'в свой ход вместо номера клетки введите "cancel"')
        n = 0  # Число ходов
        if TicTacToe.get_P(self) == 'x':
            TicTacToe.func_px(self)

        if TicTacToe.get_P(self) == '0':
            TicTacToe.func_p0(self)


TicTacToe().play()
