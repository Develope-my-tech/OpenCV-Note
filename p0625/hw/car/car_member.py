class CarMember:
    def __init__(self, id=None, pwd=None, name=None, tel=None, car_num=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.tel = tel
        self.car_num = car_num

    def print_member(self):
        print(self.id,'/',self.pwd,'/',self.name,'/',self.tel,'/',self.car_num)

class CarMemberDao:
    def select(self, id):#id로 검색해서 CarMember객체로 반환
        pass

    def insert(self, mem):#회원가입한 정보 insert
        pass

    def update(self, mem):#내정보 수정. id가 동일한 행을 찾아 pwd, tel, car_num 수정
        pass

    def delete(self, id):#탈퇴. id가 동일한 행을 찾아 삭제
        pass
