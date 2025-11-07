def find_fewest_coins(coins, target):
    # Edge cases
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    
    # Initialize DP array
    # dp[n] = minimum number of coins needed to make amount n
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 coins for amount 0
    
    # Track which coin was used to reach each amount (for reconstruction)
    parent = {}
    
    # Forward DP: Build up from amounts we can make
    for amount in range(target + 1):
        if dp[amount] == float('inf'):
            continue  # Can't make this amount, skip it
        
        # Try adding each coin (your "photoelectric effect" quantum jumps!)
        for coin in coins:
            next_amount = amount + coin
            
            # Stay within bounds
            if next_amount > target:
                continue
            
            # transfer function: dp[n+coin] = min(dp[n]+1, dp[n+coin])
            new_coin_count = dp[amount] + 1
            
            if new_coin_count < dp[next_amount]:
                dp[next_amount] = new_coin_count
                parent[next_amount] = coin  # Remember which coin we used
    
    # Check if target is reachable
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")
    
    # Reconstruct the solution by backtracking
    result = []
    current = target
    while current > 0:
        coin_used = parent[current]
        result.append(coin_used)
        current -= coin_used
    
    return sorted(result)  # Sort for test consistency


