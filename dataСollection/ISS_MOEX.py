import requests
import apimoex
import openpyxl
import pandas as pd

board = 'TQBR'
start = '2018-06-17'
end = '2023-06-17'
intervals=[60,24,7,31]
namesInterval=['hourly','daily','weekly','monthly']
enumerations=[0,1,2,3]



def importData():
    with open("D:/Study/ProjectSystem1/resources/tikers/TICK_MOEXBC.txt", "r") as TICKs:
        TICKs = [line.rstrip() for line in TICKs]


    with requests.Session() as session:
        for enumeration in enumerations:
            process = 0
            for TICK in TICKs:
                process = process + 1
                print((process / len(TICKs)) * 100,'%')
                data = apimoex.get_board_candles(session, security=TICK, interval=intervals[enumeration], start=start, end=end, board=board)
                if data == []:
                    continue
                df = pd.DataFrame(data)
                df.to_excel("D:/Study/ProjectSystem1/resources/Database/{}/{}.xlsx".format(namesInterval[enumeration], TICK), index=False)
