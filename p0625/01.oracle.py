import cx_Oracle
class Test:
    def __init__(self, num=None, name=None, price=None, desc=None):
        self.num = num
        self.name = name
        self.price = price
        self.desc = desc

    def print(self):
        print("num:", self.num, '/ name:', self.name, '/price:', self.price, '/descript:',self.desc)


class Dao_test:
    def select_all(self):
        conn =cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()  # sql 문을 실행하고 select인 경우 검색 결과 반환
        sql = "select * from test"
        cursor.execute(sql)
        datas = []
        for row in cursor:  # 검색된 줄 수 만큼 반복. 한줄씩 붙여서 row에 저장
            datas.append(Test(row[0], row[1], row[3]))
        conn.close()
        return datas

    def select(self, num):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        # 커서 객체 생성
        cursor = conn.cursor()
        sql = "select * from test where num=:1"
        d = (num,)  # 튜플 형태로 sql 바인딩할 값을 지정
        cursor.execute(sql, d)
        row = cursor.fetchone() # 검색 결과인 cursor에 한 줄 추출
        # cursor.fetchall() : 전체 줄 추출
        conn.close()    # 연결을 끊는다.
        if row is not None:
            return Test(row[0], row[1], row[2], row[3])

    def insert(self, t):    # Test 객체를 insert할 제품의 이름, 가격, 설명을 받아옴
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = "insert into test values(seq_test.nextval, :1, :2, :3)"
        # 실행할 sql 정의
        d = (t.name, t.price, t.desc)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

    def update(self, t):
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/xe", encoding='utf-8')
        cursor = conn.cursor()
        sql = "update test set price=:1, disc=:2 where num=:3"
        d = (t.price, t.desc, t.num)
        cursor.execute(sql, d)
        conn.commit()
        conn.close()

def main():
    dao = Dao_test()
    dao.insert(Test(0, 'ccc', 1500, 'iinfo3'))
    dao.update(Test(11, '', 2500, '가나다'))
    datas = dao.select_all()
    for t in datas:
        t.print()

main()


