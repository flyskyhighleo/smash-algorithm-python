class Solution:
    def trap(self, height):
        n = len(height)
        cur_max = 0
        max_left = [0] * n
        for i in range(n):
            cur_max = max(cur_max, height[i])
            max_left[i] = cur_max

        cur_max = 0
        max_right = [0] * n

        for i in range(n - 1, -1, -1):
            cur_max = max(cur_max, height[i])
            max_right[i] = cur_max

        water = 0
        for i in range(n):
            water += (min(max_left[i], max_right[i]) - height[i])

        return water
