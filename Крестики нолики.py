while True:  # Главный цикл
    # Игроки
    player_one = input("Введите игрока играющего за Х: ")
    player_two = input("Введите имя игрока играющего за О: ")


    # Матрица
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Функция для отображения игрового поля
    def board_table(table):
        for row in table:
            print("︳".join(row))
            print("-" * 7)


    # Функция для проверки победы
    def winner_check(board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return board[i][0]
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[2][0] == board[1][1] == board[0][2] != " ":
            return board[2][0]
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            return "Ничья"
        return None


    def tic_tac():
        current_player = "X"
        current_player_name = player_one
        moves = 0


        while moves < 9:
            board_table(board)
            print(f"Игрок {current_player_name}, ваш ход!")


            while True:
                try:
                    row, col = map(int, input("Введите номер строки и столбца через пробел (0, 1, 2): ").split())
                    if board[row][col] != " ":
                        print("Это поле уже занято, введите другое!")
                        continue
                    break
                except (ValueError, IndexError):
                    print("Пожалуйста, введите числа от 0 до 2!")


            board[row][col] = current_player
            moves += 1


            winner = winner_check(board)
            if winner:
                board_table(board)
                if winner == "Ничья":
                    print("Ничья!")
                else:
                    print(f"Поздравляем, игрок {player_one if winner == 'X' else player_two}, победил!")
                return


            current_player = "O" if current_player == "X" else "X"
            current_player_name = player_two if current_player == "O" else player_one


        board_table(board)
        print("Ничья!")


    # Запуск игры
    tic_tac()


    # Запрос на перезапуск
    restart = input("Хотите сыграть снова? (да/нет): ").strip().lower()
    if restart != "да":
        print("Спасибо за игру! До встречи!")
        break
