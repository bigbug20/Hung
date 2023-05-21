class Hung:
    def __init__(self, para_sinhnhat, para_body, para_voiu):
        self.sinhnhat = para_sinhnhat
        self.body = para_body
        self.voiu = para_voiu
        
    def embe(self):
        return "Vợ iu của Hùng la:" + self.voiu
        

NTH = Hung("28/10/2002" , "Đẹp trai 6 múi", "Hồng Ngọc Mặp" )

print(NTH.embe())
