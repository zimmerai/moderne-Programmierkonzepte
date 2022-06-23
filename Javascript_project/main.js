document.addEventListener('DOMContentLoaded', () => {

    const player = document.querySelector(".player")

    function keyPressed(e) {
        if (e.keyCode === 32){ //Für jeden Key existiert ein keyCode. Hier wird "Spacebar" gefiltert
            console.log("pressed")
        }
    }
    document.addEventListener("keypress", keyPressed)


})