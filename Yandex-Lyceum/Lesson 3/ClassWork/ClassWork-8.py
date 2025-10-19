first_road = input()
second_road = input()
third_road = input()

in_road = input()
not_in_road = input()

longest = 0

if (in_road in first_road) and (not_in_road not in first_road):
    if len(first_road) > longest:
        longest = len(first_road)

if (in_road in second_road) and (not_in_road not in second_road):
    if len(second_road) > longest:
        longest = len(second_road)

if (in_road in third_road) and (not_in_road not in third_road):
    if len(third_road) > longest:
        longest = len(third_road)

print(longest)