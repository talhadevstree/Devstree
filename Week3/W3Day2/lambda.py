number = [1,3,4,7]
map = list(map(lambda x: x * x , number))
print("Map Element",map)


nums = [5, 2, 3, 4, 1, 7]
even = list(filter(lambda x: x % 2 == 0, nums))
print("Filter Element",even)  

data = [(1, 3), (2, 1), (4, 2)]
sorted = sorted(data , key=lambda  x : x [1])
print("Sorted Element",sorted)
