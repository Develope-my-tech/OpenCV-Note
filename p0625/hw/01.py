import cx_Oracle


class CarMember:
    def __init__(self, id=None, pwd=None, name=None, tel=None, car_num=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.tel = tel
        self.car_num = car_num

    def print_member(self):
        print(self.id, '/', self.pwd, '/', self.name, '/', self.tel, '/', self.car_num)

class CarMemberDao:
    def select(self, id):   # id로 검색해서 CarMember 객체로 반환
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = "select * from car_member where id=:1"
        d = (id,)
        cursor.execute(sql, d)
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            return CarMember(row[0], row[1], row[2], row[3], row[4])

    def insert(self, mem):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = "insert into car_member values[:1, :2, :3, :4, :5]"
        d = (mem.id, mem.pwd, mem.name, mem.tel, mem.car_num)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def update(self, mem):  # 내 정보 수정. id가 동일한 행을 찾아 pwd, tel, car_num 수정
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = "update car_member set pwd=:1, tel=:2, car_num=:3 where id=:4"
        d = (mem.pwd, mem.tel, mem.car_num, mem.id)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()


    def delete(self, id):   # 탈퇴
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = "delete car_member where id=:1"
        d = (id,)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()



