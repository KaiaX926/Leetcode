import random

class Solution:

    def __init__(self, nums: List[int]):
        self.initial, self.sec = nums, nums
        
    def reset(self) -> List[int]:
        return self.initial
        
    def shuffle(self) -> List[int]:
        move = random.randint(0, len(self.initial))
        return random.sample(self.initial, len(self.initial)) 
