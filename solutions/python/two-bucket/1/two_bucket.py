def measure(bucket_one, bucket_two, goal, start_bucket):
    run = Measure(bucket_one=bucket_one, bucket_two=bucket_two, goal=goal, start_bucket=start_bucket)
    return run.solve()
    
class Measure:
    def __init__(self, bucket_one, bucket_two, goal, start_bucket):
        # Using dictionaries to avoid "current_one" ambiguity
        self.capacity = {"one": bucket_one, "two": bucket_two}
        self.amount = {"one": 0, "two": 0}  # Current water in each bucket
        self.goal = goal
        self.start_bucket = start_bucket
        self.moves = 0
        
        # Validate before starting
        self._validate_goal()
        self._which_start()
    
    def _validate_goal(self):
        """Check if goal is achievable"""
        import math
        
        bucket_one = self.capacity["one"]
        bucket_two = self.capacity["two"]
        
        # Goal must be <= at least one bucket
        if self.goal > bucket_one and self.goal > bucket_two:
            raise ValueError("Goal is larger than both buckets")
        
        # Goal must be divisible by GCD of bucket sizes
        gcd = math.gcd(bucket_one, bucket_two)
        if self.goal % gcd != 0:
            raise ValueError(f"Goal {self.goal} is not achievable with buckets {bucket_one} and {bucket_two}")
    
    def _which_start(self):
        """Identify which bucket is starting and which is other"""
        if self.start_bucket == 'one':
            self.starting = 'one'
            self.other = 'two'
        else:
            self.starting = 'two'
            self.other = 'one'
    
    def _is_empty(self, bucket):
        """Check if bucket is empty"""
        return self.amount[bucket] == 0
    
    def _is_full(self, bucket):
        """Check if bucket is full"""
        return self.amount[bucket] == self.capacity[bucket]
    
    def _fill_bucket(self, bucket):
        """Fill bucket to capacity"""
        self.amount[bucket] = self.capacity[bucket]
    
    def _empty_bucket(self, bucket):
        """Empty the bucket"""
        self.amount[bucket] = 0
    
    def _pour(self, from_bucket, to_bucket):
        """Pour from one bucket to another until source is empty or destination is full"""
        # Calculate how much we can transfer
        space_available = self.capacity[to_bucket] - self.amount[to_bucket]
        transfer_amount = min(self.amount[from_bucket], space_available)
        
        # Transfer the water
        self.amount[from_bucket] -= transfer_amount
        self.amount[to_bucket] += transfer_amount
    
    def _would_violate_forbidden_state(self, from_bucket, to_bucket):
        """Check if pouring would create forbidden state (starting empty, other full)"""
        # Simulate the pour
        space_available = self.capacity[to_bucket] - self.amount[to_bucket]
        transfer_amount = min(self.amount[from_bucket], space_available)
        
        # After pour, what would the state be?
        from_amount_after = self.amount[from_bucket] - transfer_amount
        to_amount_after = self.amount[to_bucket] + transfer_amount
        
        # Forbidden: starting bucket empty AND other bucket full
        if from_bucket == self.starting and to_bucket == self.other:
            if from_amount_after == 0 and to_amount_after == self.capacity[to_bucket]:
                return True
        return False
    
    def _is_goal_satisfied(self):
        """Check if either bucket has the goal amount"""
        return self.amount["one"] == self.goal or self.amount["two"] == self.goal
    
    def solve(self):
        """Main algorithm to solve the two-bucket problem"""
        # Special case: if goal equals starting bucket capacity
        if self.goal == self.capacity[self.starting]:
            self._fill_bucket(self.starting)
            self.moves = 1
            return (self.moves, self.starting, 0)
        
        # Special case: if goal equals other bucket capacity
        # We must avoid forbidden state (starting empty, other full)
        # So fill starting bucket FIRST, then fill other bucket
        if self.goal == self.capacity[self.other]:
            self._fill_bucket(self.starting)
            self.moves += 1
            self._fill_bucket(self.other)
            self.moves += 1
            return (self.moves, self.other, self.amount[self.starting])
        
        # Main loop for other cases
        max_iterations = 1000
        iterations = 0
        
        while not self._is_goal_satisfied():
            iterations += 1
            if iterations > max_iterations:
                raise ValueError("Algorithm exceeded maximum iterations")
            
            if self._is_empty(self.starting):
                self._fill_bucket(self.starting)
            elif self._is_full(self.other):
                self._empty_bucket(self.other)
            else:
                if self._would_violate_forbidden_state(self.starting, self.other):
                    raise ValueError("Would violate forbidden state rule")
                self._pour(self.starting, self.other)
            
            self.moves += 1
        
        # Return results
        if self.amount["one"] == self.goal:
            goal_bucket = "one"
            other_amount = self.amount["two"]
        else:
            goal_bucket = "two"
            other_amount = self.amount["one"]
        
        return (self.moves, goal_bucket, other_amount)