from .ISS_MOEX import *
import os

def unityFiles():
    with open("D:/Study/ProjectSystem1/resources/tikers/TICK_MOEXBC.txt", "r") as TICKs:
        TICKs = [line.rstrip() for line in TICKs]
    for nameInterval in namesInterval:
        folder = 'D:/Study/ProjectSystem1/resources/Database/'+nameInterval #папка с файлами
        files = os.listdir(folder) #формируем список путей к файлам
        all_file_frames = [] #сюда будем добавлять прочитанную таблицу
        for f in TICKs:
            print('Reading %s'%(folder+'/'+f+'.xlsx'))
            tab = pd.read_excel(folder+'/'+f+'.xlsx',usecols=['close'])
            tab.columns = [f]
            all_file_frames.append(tab)
        all_frame = pd.concat(all_file_frames,axis=1) #  axis=0 если нужно добавить таблицу снизу и axis=1 если нужно слева
        all_frame.to_excel('D:/Study/ProjectSystem1/resources/Database/mergedFiles/final_file_{}.xlsx'.format(nameInterval), index=False) #получим файл final_file.xlsx в os.getcwd()