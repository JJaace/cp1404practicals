import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_QUICK_PICKS = int(input("How many quick picks? "))


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < 6:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


for i in range(NUM_QUICK_PICKS):
    quick_pick = generate_quick_pick()
    formatted_quick_pick = " ".join(["{:2}".format(row) for row in quick_pick])
    print(formatted_quick_pick)
