#import sqlite3
from DTO import Supplier, Logistic, Clinic, Vaccine


class Suppliers:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, dto_instance):
        ins_dict = vars(dto_instance)
        params = list(ins_dict.values())
        stmt = 'INSERT INTO suppliers (id, name, logistic) VALUES (?,?,?)'
        self._conn.execute(stmt, params)
        self._conn.commit()

    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM suppliers ORDER BY id ASC')
        return [Supplier(int(x[0]), x[1], int(x[2])) for x in c.fetchall()]

    def find(self, name):
        stmt = "SELECT * FROM suppliers WHERE name=?"
        c = self._conn.cursor()
        c.execute(stmt, [name])
        x = c.fetchall()[0]
        return Supplier(int(x[0]), x[1], int(x[2]))

    def delete(self, dto_instance):
        stmt = 'DELETE FROM suppliers WHERE id=?'
        self._conn.execute(stmt, [dto_instance.id])
        self._conn.commit()

    def update(self, new_dto_instance):
        stmt = "UPDATE suppliers SET name=? , logistic=? WHERE id=?"
        self._conn.execute(stmt, [new_dto_instance.name , new_dto_instance.logistic, new_dto_instance.id])
        self._conn.commit()


class Logistics:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, dto_instance):
        ins_dict = vars(dto_instance)
        params = list(ins_dict.values())
        stmt = 'INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?,?,?,?)'
        self._conn.execute(stmt, params)
        self._conn.commit()

    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM logistics ORDER BY id ASC')
        return [Logistic(int(x[0]), x[1], int(x[2]), int(x[3])) for x in c.fetchall()]

    def find(self, id):
        stmt = 'SELECT * FROM logistics WHERE id=?'
        c = self._conn.cursor()
        c.execute(stmt, [id])
        x = c.fetchall()[0]
        return Logistic(int(x[0]), x[1], int(x[2]), int(x[3]))

    def delete(self, dto_instance):
        stmt = 'DELETE FROM logistics WHERE id=?'
        self._conn.execute(stmt, [dto_instance.id])
        self._conn.commit()

    def update(self, new_dto_instance):
        stmt = "UPDATE logistics SET count_sent=? , count_received=? WHERE id=?"
        self._conn.execute(stmt, [new_dto_instance.count_sent, new_dto_instance.count_received, new_dto_instance.id])
        self._conn.commit()


class Clinics:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, dto_instance):
        ins_dict = vars(dto_instance)
        params = list(ins_dict.values())
        stmt = 'INSERT INTO clinics (id, location, demand, logistic) VALUES (?,?,?,?)'
        self._conn.execute(stmt, params)
        self._conn.commit()


    def find(self, location):
        stmt = "SELECT * FROM clinics WHERE location=?"
        c = self._conn.cursor()
        c.execute(stmt, [location])
        x = c.fetchall()[0]
        return Clinic(int(x[0]), x[1], int(x[2]), int(x[3]))

    def delete(self, dto_instance):
        stmt = 'DELETE FROM clinics WHERE id=?'
        self._conn.execute(stmt, [dto_instance.id])
        self._conn.commit()


    def update(self, new_dto_instance):
        stmt = "UPDATE clinics SET demand=? , logistic=? WHERE id=?"
        self._conn.execute(stmt, [new_dto_instance.demand, new_dto_instance.logistic, new_dto_instance.id])
        self._conn.commit()


class Vaccines:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, dto_instance):
        ins_dict = vars(dto_instance)
        params = list(ins_dict.values())
        
        stmt = 'INSERT INTO vaccines (id, date, supplier, quantity) VALUES (?,?,?,?)'
        self._conn.execute(stmt, params)

    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM vaccines ORDER BY id ASC')
        return [Vaccine(int(x[0]), x[1], int(x[2]), int(x[3])) for x in c.fetchall()]

    def findmax(self):
        stmt = 'SELECT max(id) FROM vaccines'
        c = self._conn.cursor()
        c.execute(stmt)
        vv = c.fetchone()[0]
        return vv

    def delete(self, dto_instance):
        stmt = 'DELETE FROM vaccines WHERE id=?'
        self._conn.execute(stmt, [dto_instance.id])

    def update(self, new_dto_instance):
        stmt = "UPDATE vaccines SET quantity=? WHERE id=?"
        self._conn.execute(stmt, [new_dto_instance.quantity, new_dto_instance.id])
        self._conn.commit()

