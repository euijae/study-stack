def count_seq(nums: list[int]) -> int:
    n = len(nums)
    if n < 2:
        return n

    def get_direction(curr, next) -> int:
        if curr == next:
            return 0
        return (next - curr) // abs(next - curr)
    
    direction = get_direction(nums[0], nums[1])
    count = 1
    
    for i in range(2, n):
        curr_direction = get_direction(nums[i-1], nums[i])    
        if curr_direction != direction:
            count += 1
            direction = curr_direction
            
    return count


print(count_seq([1, 2, 2, 3]) == 3)
print(count_seq([9, 9, 9, 9]) == 1)
print(count_seq([8, 2, 4, 5, 1, 1]) == 4)
print(count_seq([]) == 0)