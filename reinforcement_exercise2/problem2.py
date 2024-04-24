def first_chars(strings: list[str]) -> str:
    if not strings:
        return ""
    leading = strings[0]
    if type(leading) == str:
        return leading[0] + first_chars(strings[1:])
    elif type(leading) == list:
        return first_chars(leading) + first_chars(strings[1:])

# second test case (given in problem)
assert first_chars(['boo', 'was', ['sleeping', 'deeply'], 'that', 'night', ['as', ['usual']]]) == "bwsdtnau", "second test case for first_chars() not satisfied"


def count_bigger(nums: list[any], threshold: int) -> int:
    if not nums:
        return 0
    leading = nums[0]
    if type(leading) == int and int(leading) > int(threshold):
        return count_bigger(nums[1:], threshold) + 1
    elif type(leading) == list:
        return count_bigger(leading, threshold) + count_bigger(nums[1:], threshold)
    else:
        return count_bigger(nums[1:], threshold)
    
# edge case where list contains number exactly equal to threshold
assert count_bigger([1, 2.5, 3, 4, 5, 6], 2.5) == 4, "count_bigger() not counting a list of ints correctly"

# second test case (given in problem)
assert count_bigger(['boo', [3.0, 'is', 'perfect'], 'today', 5], 3) == 1, "second test case for count_bigger() not satisfied"
