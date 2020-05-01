from fractions import Fraction


def solution(pegs):
    array_length = len(pegs)
    if ((not pegs) or array_length == 1):
        return [-1, -1]
    case = True if (array_length % 2 == 0) else False
    addition = (- pegs[0] + pegs[array_length - 1]
                ) if case else (- pegs[0] - pegs[array_length - 1])
    if (array_length > 2):
        for index in range(1, array_length-1):
            addition += 2 * (-1)**(index+1) * pegs[index]
    initial_radius = Fraction(
        2 * (float(addition)/3 if case else addition)).limit_denominator()
    if initial_radius < 2:
        return [-1, -1]
    currentRadius = initial_radius
    for index in range(0, array_length-2):
        centre = pegs[index+1] - pegs[index]
        updated_radius = centre - currentRadius
        if (currentRadius < 1 or updated_radius < 1):
            return [-1, -1]
        else:
            currentRadius = updated_radius
    return[initial_radius.numerator, initial_radius.denominator]
