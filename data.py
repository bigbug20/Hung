class Student:
    
    count = 0
    
    def __init__(self, id, name, birth):
        self.id = id
        self.name = name
        self.birth = birth
        Student.count += 1
        
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
    
    def set_name(self, name):
        self.name = name
   
    def get_name(self):
        return self.name
    
    def set_birth(self, birth):
        self.birth = birth
   
    def get_birth(self):
        return self.birth
    
    def show_info(self):
        print(f"Id: {self.id}")
        print(f"Ten: {self.name}")
        print(f"Ngay sinh: {self.birth}")
        