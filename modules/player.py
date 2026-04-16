#making a player object to store the necessary info in one place
class Player():
    def __init__(self, name, job, role): #in ff14 theyre called jobs instead of classes so im doing that
        self.name = name
        self.job = job
        self.role = role
        
    def __str__(self):
        return f"{self.name}, {self.job}, {self.role}"
    
    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

