from pickle import TRUE
from venv import create


from pathlib import Path


def storeHighscore(currenthighscore):
    highscoreDataFile = Path('Python_project/Data/highscoreData.txt')
    highscoreDataFile.touch(exist_ok=True)
    fileRead = open(highscoreDataFile, 'r')    
    allTimeHighscore = fileRead.read()    
    fileRead.close()
    
    if allTimeHighscore == '' or currenthighscore > int(allTimeHighscore):
        fileWrite = open(highscoreDataFile, 'w')
        fileWrite.write(str(currenthighscore))
        fileWrite.close
   

storeHighscore(10)