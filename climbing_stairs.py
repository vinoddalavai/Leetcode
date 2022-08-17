class ClimbingStairs:
    def climb_stairs(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
        for index in range(4, n + 1):
            dp[index] = dp[index - 1] + dp[index - 2]
        return dp[n]


n1, n2, n3, n4 = 3, 4, 5, 6
obj = ClimbingStairs()
print("Ways to climb stairs: ")
print(f"For {n1} = {obj.climb_stairs(n1)}")
print(f"For {n2} = {obj.climb_stairs(n2)}")
print(f"For {n3} = {obj.climb_stairs(n3)}")
print(f"For {n4} = {obj.climb_stairs(n4)}")
