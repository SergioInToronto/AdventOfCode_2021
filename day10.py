input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

lines = raw


ILLEGAL_CLSINGS_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def matches(opening, closing):
    if opening == '[':
        return closing == ']'
    if opening == '{':
        return closing == '}'
    if opening == '(':
        return closing == ')'
    if opening == '<':
        return closing == '>'
    raise ValueError(opening)


def diagnose_line(line):
    stack = []
    illegal_closings = []
    for index, char in enumerate(line):
        if char in '[{(<':
            stack.append(char)
        elif char in '>)}]':
            opening = stack.pop()
            if matches(opening, char):
                continue
            print(f'Char {index + 1}: "{opening}" does not match {char}')
            illegal_closings.append(char)
            break # part 1
    if stack:
        print(f'Char {index + 1} is incomplete')
        return 'incomplete', illegal_closings
    if illegal_closings:
        return 'corrupted', illegal_closings
    print(f'Char {index + 1} looks good')


def part1():
    tally = 0
    for line in lines:
        result, illegal_closings = diagnose_line(line)
        if not illegal_closings:
            continue
        assert len(illegal_closings) == 1
        score = ILLEGAL_CLSINGS_POINTS[illegal_closings[0]]
        tally += score

    print(f"Total score: {tally}")


def part2():
    pass




part1()
# part2()
