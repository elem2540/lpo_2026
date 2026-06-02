import mysql.connector as mysqlcon
import pprint
import datetime
from abc import ABC, abstractmethod


class CDataBase:
    def connessione_al_DB(self):
        mysqlcon_obj = mysqlcon.MySQLConnection()
        mysqlcon_obj.connect(option_files="my.cnf")

        print("My SQL connection ID is: {}".format(mysqlcon_obj.connection_id))
        return mysqlcon_obj

    def esegui_query(self, query):
        printer = pprint.PrettyPrinter(indent=1)
        mysqlcon_obj = self.connessione_al_DB()
        results = mysqlcon_obj.cmd_query(
            query
        )
        result_set = mysqlcon_obj.get_rows()
        printer.pprint(result_set)
        return result_set

    def chiudi_connessione(self):
        mysqlcon_obj = self.connessione_al_DB()
        mysqlcon_obj.close()


class CEvento:

    def __init__(self, idEvento: int, data: str):
        self.idEvento = idEvento
        self.data = data

    @classmethod
    @abstractmethod
    def crea_evento(cls):
        pass

    @abstractmethod
    def calcola_prezzo(self):
        pass


class CSagra(CEvento):
    costo_personale = 1500

    def __init__(self, costo_cibo, idEvento, data):
        self.costo_cibo = costo_cibo
        super().__init__(idEvento, data)

    def calcola_prezzo(self):
        return self.costo_cibo * self.costo_personale


class CConcerti(CEvento):
    moltiplicatore_costo_base = 20
    def __init__(self, numero_musicisti, durata, idEvento, data):
        self.numero_musicisti = numero_musicisti
        self.durata = durata
        super().__init__(idEvento, data)



if __name__ == "__main__":
    db = CDataBase()
    query = ("""
            SELECT nome, anno, incasso 
            FROM alberghi
            """)
    db.connessione_al_DB()
    db.esegui_query(query)
    db.chiudi_connessione()
