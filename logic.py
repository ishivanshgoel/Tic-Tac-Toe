## game logic
class Logic:
    def __init__(self,player_name):
        self.player=player_name
        self.nums={
            "00" : 0,
            "01" : 1,
            "02" : 2,
            "10" : 3,
            "11" : 4,
            "12" : 5,
            "20" : 6,
            "21" : 7,
            "22" : 8,
        }

    def check(self):
        nums=self.nums
        for i in range(3):
            for j in range(3):
                print(nums[f"{i}{j}"])
        # row 0 
        if(nums["00"]==nums["01"]==nums["02"]):
            return f"{self.player} Won!!"
        # row 1
        elif(nums["10"]==nums["11"]==nums["12"]):
            return f"{self.player} Won!!"
        # row 2
        elif(nums["20"]==nums["21"]==nums["22"]):
            return f"{self.player} Won!!"
        # diagonal
        elif(nums["00"]==nums["11"]==nums["22"]):
            return f"{self.player} Won!!"
        # diagonal
        elif(nums["02"]==nums["11"]==nums["20"]):
            return f"{self.player} Won!!"
        # column 1
        elif(nums["00"]==nums["11"]==nums["21"]):
            return f"{self.player} Won!!"
        # column 2
        elif(nums["01"]==nums["11"]==nums["21"]):
            return f"{self.player} Won!!"
        # column 3
        elif(nums["02"]==nums["12"]==nums["22"]):
            return f"{self.player} Won!!"
## even more logic

##debugging
# ll=Logic("Shivansh")
# # ll.nums["00"]='x'
# # ll.nums["01"]='x'
# # ll.nums["02"]='x'

# print(ll.check())
