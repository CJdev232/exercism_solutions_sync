def combinations(target, size, exclude):
    combo = Combinations(target,size,exclude)
    return combo.backtrack()

class Combinations:
    def __init__(self,target,size,exclude):
        self.target = target
        self.size = size
        self.exclude = exclude if exclude else set()
        self.result = []
    def backtrack(self):
        self._backtrack_helper(current_combo=[],start_point=1,remaining_sum=self.target,remaining_size=self.size)
        return sorted(self.result)
    def _backtrack_helper(self,current_combo,start_point,remaining_sum,remaining_size):
        if not remaining_size and not remaining_sum:
            self.result.append(list(current_combo))
        if not remaining_size and remaining_sum:
            current_combo = []
        if remaining_size and remaining_sum:
            for digit in range(start_point,10):
                if digit in self.exclude:
                    continue 
                current_combo.append(digit)
                self._backtrack_helper(current_combo,start_point=digit+1,remaining_sum=remaining_sum-digit,remaining_size=remaining_size-1)
                current_combo.pop()
        
            
        
                
        
        
        
    
    
