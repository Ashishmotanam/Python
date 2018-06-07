def h_line ( size ):
    return " ---" * size + " \n"

def v_line ( size ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += h_line(size)
        board += v_line(size)
    board += h_line(size)
    return board

if __name__ == "__main__":
    size = int(input("What size game board do You want? "))
    print(gameboard(size))
