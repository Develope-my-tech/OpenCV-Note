import cx_Oracle

class CarMember:
    login_id = None #로그인 id를 저장할 클래스 멤버

    def __init__(self, id=None, pwd=None, name=None, tel=None, car_num=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.tel = tel
        self.car_num = car_num

    def print_member(self):
        print(self.id,'/',self.pwd,'/',self.name,'/',self.tel,'/',self.car_num)

class CarMemberDao:
    def select(self, id):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = 'select * from car_member where id=:1'
        d = (id,)
        cursor.execute(sql, d)
        row = cursor.fetchone()     # 행 1줄 가져오기
        conn.close()
        if row is not None:
            return CarMember(row[0], row[1], row[2], row[3], row[4])

    def insert(self, mem):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = 'insert into car_member values(:1, :2, :3, :4, :5)'
        d = (mem.id, mem.pwd, mem.name, mem.tel, mem.car_num)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def update(self, mem):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = 'update car_member set pwd=:1, tel=:2, car_num=:3 where id=:4'
        d = (mem.pwd, mem.tel, mem.car_num, mem.id)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def delete(self, id):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = 'delete car_member where id=:1'
        d = (id,)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()
