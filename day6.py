from itertools import chain


input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')


# def new_fish_value(fish):
#     if fish == 0:
#         return 6
#     return fish - 1


def simulate(days):
    current_fish = [int(x) for x in raw[0].split(',')]
    for day in range(days):
        print(f"Start day {day + 1}. There are {len(current_fish)} fish")
        new_fish = (8 for fish in current_fish if fish == 0)
        # next_fish = map(new_fish_value, current_fish)
        next_fish = (6 if fish == 0 else fish-1 for fish in current_fish)
        current_fish = list(chain(next_fish, new_fish))
    return len(current_fish)


def part1():
    days = 80
    fish_count = simulate(days)
    print(f"After {days} days there are {fish_count} fish")



def part2():
    days = 256
    fish_count = simulate(days)
    print(f"After {days} days there are {fish_count} fish")


part2()
