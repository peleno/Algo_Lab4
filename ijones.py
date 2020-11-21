def read_input_from_stdin():
    width, height = list(map(int, input().split()))
    words = []
    for _ in range(height):
        word = input()
        words.append(word)
    return words


def ijones(corridor):
    height = len(corridor)
    width = len(corridor[0])
    # there is just one way to get to each tile in first column
    number_of_ways_to_get = [[1] for _ in corridor]
    prev_columns = {}
    for row in corridor:
        letter = row[0]
        prev_columns[letter] = prev_columns.get(letter, 0) + 1

    for j in range(1, width):
        current_column = {}
        for i in range(height):
            letter = corridor[i][j]
            number_of_ways = prev_columns.get(letter, 0)
            if letter != corridor[i][j - 1]:
                number_of_ways += number_of_ways_to_get[i][j - 1]
            number_of_ways_to_get[i].append(number_of_ways)
            current_column[letter] = current_column.get(letter, 0) + number_of_ways

        for letter in current_column:
            prev_columns[letter] = prev_columns.get(letter, 0) + current_column[letter]
    number_of_ways_to_exit = number_of_ways_to_get[0][-1]
    if height > 1:
        number_of_ways_to_exit += number_of_ways_to_get[-1][-1]
    return number_of_ways_to_exit

if __name__ == '__main__':
    corridor = read_input_from_stdin()
    exit_ways = ijones(corridor)
    print(exit_ways)