import sqlite3
import atexit
import DAO
import DTO


class Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        # self._conn.text_factory = bytes
        self.vaccines = DAO.Vaccines(self._conn)
        self.suppliers = DAO.Suppliers(self._conn)
        self.clinics = DAO.Clinics(self._conn)
        self.logistics = DAO.Logistics(self._conn)

    def close_db(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
                CREATE TABLE IF NOT EXISTS logistics (
                id      INTEGER PRIMARY KEY,
                name    TEXT    NOT NULL,
                count_sent INTEGER  NOT NULL,
                count_received INTEGER NOT NULL
                );
                
                CREATE TABLE IF NOT EXISTS suppliers (
                id      INTEGER PRIMARY KEY,
                name    TEXT NOT NULL,
                logistic    INTEGER,
                FOREIGN KEY (logistic)  REFERENCES logistics(id)
                );
                
            CREATE TABLE IF NOT EXISTS vaccines (
                id      INTEGER PRIMARY KEY,
                date    DATE    NOT NULL,
                supplier INTEGER,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (supplier)  REFERENCES suppliers(id)
                );

                CREATE TABLE IF NOT EXISTS clinics (
                id      INTEGER PRIMARY KEY,
                location    TEXT    NOT NULL,
                demand INTEGER  NOT NULL,
                logistic INTEGER NOT NULL,
                FOREIGN KEY (logistic)  REFERENCES logistics(id)
                );
            """)


    def getTotal(self):
        stmtLogistic = "SELECT sum(count_received), sum(count_sent) FROM logistics"
        stmtVaccine = "SELECT sum(quantity) FROM vaccines"
        stmtClinic = "SELECT sum(demand) FROM clinics"
        c = self._conn.cursor()
        totalInventory = c.execute(stmtVaccine).fetchone()[0]
        totalDemand = c.execute(stmtClinic).fetchone()[0]
        totalReceivedSent = c.execute(stmtLogistic).fetchone()
        vv = [str(i) for i in list(totalReceivedSent)]
        ccc = ','.join([str(totalInventory), str(totalDemand), vv[0], vv[1]])
        return ccc + '\n'


repo = Repository()
atexit.register(repo.close_db)
