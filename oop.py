class Hung:
    def __init__(self, para_sinhnhat, para_body, para_voiu):
        self.sinhnhat = para_sinhnhat
        self.body = para_body
        self.voiu = para_voiu
        
class Hung2023(Hung):
    def __init__(self, para_sinhnhat, para_body, para_voiu,para_nghe):
        super().__init__(para_sinhnhat, para_body, para_voiu)
        self.nghe = para_nghe
        

NTH = Hung2023("28/10/2002" , "Đẹp trai 6 múi", "Hồng Ngọc Mặp","Backend Dev" )

print(NTH.__dict__)
