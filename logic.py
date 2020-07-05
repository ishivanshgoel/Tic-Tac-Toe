class Logic:
    def __init__(self,player_name):
        self.player=player_name

    nums={
        "00" : 0,
        "01" : 1,
        "02" : 2,
        "10" : 3,
        "11" : 4,
        "12" : 5,
        "21" : 6,
        "22" : 7,
        "23" : 8,
    }

    def check(self):
        nums=self.nums
        if(nums["00"]==nums["01"]==nums["02"]):
            return f"{self.player} Won!!"

        elif(nums["10"]==nums["12"]==nums["22"]):
            return f"{self.player} Won!!"
        
        elif(nums["21"]==nums["22"]==nums["23"]):
            return f"{self.player} Won!!"

        elif(nums["00"]==nums["12"]==nums["23"]):
            return f"{self.player} Won!!"
        
        elif(nums["02"]==nums["12"]==nums["21"]):
            return f"{self.player} Won!!"
  ## even more logic


##debugging
ll=Logic("Shivansh")
# ll.nums["00"]='x'
# ll.nums["01"]='x'
# ll.nums["02"]='x'

print(ll.check())
