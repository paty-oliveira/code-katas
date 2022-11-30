def is_divisible_by(divisible_by, number):
    return number % divisible_by == 0


def fizz_buzz(number):
    lst = []
    for i in range(1, number + 1):
        if is_divisible_by(3, i) and is_divisible_by(5, i):
            lst.append("FizzBuzz")
        elif is_divisible_by(3, i):
            lst.append("Fizz")
        elif is_divisible_by(5, i):
            lst.append("Buzz")
        else:
            lst.append(str(i))

    return lst

