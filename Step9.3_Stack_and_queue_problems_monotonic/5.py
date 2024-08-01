# Trapping Rainwater

def trap(height):
    max_left = 0
    left = 0
    length = len(height)
    result = 0
    max_right = 0
    right = length - 1

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                result += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                result += max_right - height[right]
            right -= 1
    return result
height= [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
