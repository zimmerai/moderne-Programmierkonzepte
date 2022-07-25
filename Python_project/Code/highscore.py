from pickle import TRUE
from venv import create
from pathlib import Path


def store_highscore(current_highscore: int):
    highscore_data_file = Path('Python_project/Data/highscoreData.txt')
    highscore_data_file.touch(exist_ok=True)
    all_time_highscore = read_highscore()
    
    if all_time_highscore == '' or current_highscore > int(all_time_highscore):
        file_write = open(highscore_data_file, 'w')
        file_write.write(str(current_highscore))
        file_write.close

def read_highscore():
    highscore_data_file = Path('Python_project/Data/highscoreData.txt')
    highscore_data_file.touch(exist_ok=True)
    file_read = open(highscore_data_file, 'r')    
    allTimeHighscore = file_read.read()    
    file_read.close()
    return int(allTimeHighscore)