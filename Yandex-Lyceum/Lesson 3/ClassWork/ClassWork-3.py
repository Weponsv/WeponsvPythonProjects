size_a = int(input())
size_b = int(input())
    
thing_x = int(input())
thing_y = int(input())
thing_z = int(input())
    
fits = (
    (size_a >= thing_x and size_b >= thing_y) or
    (size_a >= thing_x and size_b >= thing_z) or
    (size_a >= thing_y and size_b >= thing_x) or
    (size_a >= thing_y and size_b >= thing_z) or
    (size_a >= thing_z and size_b >= thing_x) or
    (size_a >= thing_z and size_b >= thing_y)
)
    
print(fits)