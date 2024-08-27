# sum the marks of each key and print as <key> has got <marks>.


def marksCalculate(details):
    for key, value in details.items():
        sum = 0
        for mark in range(len(value)):
            sum += value[mark]
        print(f'{key} has scored {sum} marks.')

        # Other Approch

        tot_marks = sum(value)
        print(f'{key} has scored {tot_marks} marks.')


details = {
    "anirudh": [45, 44, 33, 12, 5, 6, 45, 6, 2],
    "sanjay": [67, 89, 96],
    "vandana": [76, 43, 53, 21, 22],
    "vivek": [11, 22, 31, 78, 94],
}
marksCalculate(details)
