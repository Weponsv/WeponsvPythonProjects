example = input()
test = input()

condition_1 = len(test) >= len(example)
condition_2 = test >= example
condition_3 = any(substring in test for substring in ["Мур", "мур", "хрр"])

if condition_1 and condition_2 and condition_3:
    print("True")
else:
    print("False")