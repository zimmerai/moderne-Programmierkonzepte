document.addEventListener('DOMContentLoaded', () => {

    const player = document.querySelector(".player")
    let JumpCounter = 0
    let position = 150;

    function keyPressed(e) {
        if (e.keyCode === 32){ //Für jeden Key existiert ein keyCode. Hier wird "Spacebar" gefiltert
            if (JumpCounter<2){
                JumpCounter +=1
                jump()
            }
        }
    }
    document.addEventListener("keypress", keyPressed)

    function jump(){
        if(player.style.top){
            position = player.style.top.match(/\d+/g) //https://stackoverflow.com/questions/42827884/split-a-number-from-a-string-in-javascript
            console.log(position)
            console.log(position[0])
        }
        let upTimerInterval = setInterval(function() {
        //nach unten
        if(position<=10){
            clearInterval(upTimerInterval)
            let downTimerInterval = setInterval(function() {
            position +=10
            player.style.top = position + 'px'
            if (position >= 150){
                clearInterval(downTimerInterval)
                JumpCounter=0
            }
            }, 20)
        }
        //nach oben    
        position -= 10
        player.style.top = position + 'px' 
        }, 20)
    }

})