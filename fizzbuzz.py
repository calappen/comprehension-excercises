for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and not i % 5 == 0:
        print("Fizz")
    elif i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
    else:
        print(i)
print("-----------------------")
fizzbuzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else("Fizz" if i % 3 == 0 and not i % 5 == 0 else("Buzz" if i % 5 == 0 and not i % 3 == 0 else i)) for i in range(1,101)]

for i in fizzbuzz:
    print(i)