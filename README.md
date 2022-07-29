# moderne-Programmierkonzepte
Sammlung von allen 3 Jump and Run Projekten.

Die Programme sind alle von dem obersten Ordner "moderne-Programmierkonzepte" ausführbar (bei JavaScript gibt es zusätzliches Setup)

# Tutorials und eigene Erweiterungen
Wir haben alle als Grundlage für unseren Code ein Tutorial für das Chrome-Dino-Game genutzt und alles darüber hinaus wenn nicht anders gekennzeichnet eigenständig programmiert

## JAVA (Lisa)

### Setup
* Führen Sie im GameWindow die main-Methode aus

### Tutorial
[Tutorial Playlist: Chrome offline game tutorial](https://www.youtube.com/playlist?list=PLOgQJY7VjpBQhCZDWbucTp8WU8nXkbtUB)

### Eigene Erweiterungen
* Einfügen anderer Bilder und notwendige Anpassungen im Code wegen Position, Größe, etc.
* Implementierung eines Double-Jumps
* Fixen von Bugs beim Jumps
* Einfügen unterschiedlicher Gegner (Schlange, Virus)
* Verbesserung des HighScores 

### Controls
* Springen: "Space"

## JavaScript (Aidan)
### Setup (Vorraussetzung npm)
* navigieren Sie im Terminal in den Ordner "Javascript_Project"
* führen Sie den Befehl "npm install" aus
* nach erfolgreicher Installation starten Sie den Server mit "npx live-server"

### Controls
* Springen: "W", "Space" oder "Pfeil nach oben"
* Ducken: "S", "C" oder "Pfeil nach unten"

### Tutorial
[How To Create Your First Game - JavaScript](https://www.youtube.com/watch?v=47eXVRJKdkU)

### Eigene Erweiterungen
* Einfügen anderer Bilder und notwendige Anpassungen im Code wegen Position, Größe, etc. 
* Mehrere Wolken in unterschiedlichen Höhen, die langsamer als der Boden sind
* Verschiedene Tastatureingaben zur Steuerung (Space, Pfeil hoch, "W" zum Springen; Pfeil runter, "S" und "C"zum Ducken bzw. Schrumpfen)
* Highscore
* Einfügen von unterschiedlichen Gegnern (Virus, Schlange und Rakete)
* Double Jump 
* "ducken" Funktion

## Python (Johanna)
### Setup
* Führen sie die "main.py" in "Python_project" aus um das Spiel zu starten

### Controls
* Springen: "W", "Space" oder "Pfeil nach oben"
* Ducken: "S" oder "Pfeil nach unten"

### Tutorialreihe
* [Part 1: Setup and Dino Animation](https://www.youtube.com/watch?v=wnBGG7JLrkg&ab_channel=CodeBucket)
* [Part 2: Jumping and Ducking Motion](https://www.youtube.com/watch?v=aAkO8Pketkg&ab_channel=CodeBucket)
* [Part 3: Score and Background](https://www.youtube.com/watch?v=KbKMqxVw8x0&ab_channel=CodeBucket)
* [Part 4: Obstacles and Collision](https://www.youtube.com/watch?v=LYvrb-1ntIE&ab_channel=CodeBucket)
* [Part 5: Menu and Final Touches](https://www.youtube.com/watch?v=xQ5UCzFKR58&ab_channel=CodeBucket)
### Eigene Erweiterungen
Dieses Projekt ist meine erste Python-Erfahrung und daher habe ich viel Zeit verwendet, um mich in Python einzuarbeiten.
* Einfügen anderer Bilder und notwendige Anpassungen im Code wegen Position, Größe, etc. 
* Mehrere Wolken in unterschiedlichen Höhen, die langsamer als der Boden sind
* Verschieden Tastatureingaben zur Steuerung (Space, Pfeil hoch, "W" zum Springen; Pfeil runter und "S" zum Ducken bzw. Schrumpfen; ESC zum Beenden)
* Highscore, der auf beiden Screens angezeigt werden kann (Menu- und Spiel-Screen)
* Umwandlung des Vogels zu einer Rakete, die schneller als der Boden ist
* Double Jump 
(sehr kompliziert zu lösen in Python, da die Tastatureingabe nur überprüft, ob eine Taste gedrückt wird und deshalb nicht nur einmal triggert, sondern mehrmals; Dabei habe ich Hilfe von Aidan bekommen, der mit mir gemeinsam mehrere Stunden verschiedene Möglichkeiten und Ideen ausprobiert und Probleme analysiert hat. Durch diese Gespräche und Auseinandersetzung konnte ich mit weiterer Hilfe von Lisas bestehendem Code für den Double Jump eine funktionierende Lösung für den Double Jump in Python entwickeln und implementieren.)
