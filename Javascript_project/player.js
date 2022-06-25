import { incrementCustomProperty, getCustomProperty, setCustomProperty } from "./updateCustomProperty.js"

const playerElement = document.querySelector("[data-player]")
const JUMP_SPEED = 0.45
const GRAVITY = 0.0025
const PLAYER_ANIMATION_COUNT = 2
const ANIMATION_TIME = 150

let jumpCounter
let playerAnimation
let currentAnimationTime
let yVelocity
export function setupPlayer () {
    jumpCounter = 0
    playerAnimation = 0
    currentAnimationTime = 0
    yVelocity = 0 
    setCustomProperty(playerElement, "--bottom", 0)
    document.removeEventListener("keydown", onJump)
    document.addEventListener("keydown", onJump)
}

export function updatePlayer (timeDifference, speedScale) {
    handleRun(timeDifference, speedScale)
    handleJump(timeDifference)

}

function handleRun (timeDifference, speedScale) {
    if (jumpCounter > 0){
        playerElement.src = "img/Mario_klein1.png"
        return
    }

    if (currentAnimationTime >= ANIMATION_TIME) {
        playerAnimation = (playerAnimation + 1) % PLAYER_ANIMATION_COUNT
        playerElement.src = `img/Mario_klein${playerAnimation}.png`
        currentAnimationTime -= ANIMATION_TIME
    }
    currentAnimationTime += timeDifference * speedScale
}

function handleJump (timeDifference) {
    if(jumpCounter > 2 || jumpCounter == 0 ) return

    incrementCustomProperty(playerElement, "--bottom", yVelocity * timeDifference)
    
    if (getCustomProperty(playerElement, "--bottom") <= 0){
        setCustomProperty(playerElement, "--bottom", 0)
        jumpCounter = 0
    }
    console.log(yVelocity) 
    yVelocity -= GRAVITY * timeDifference

}

function onJump(e) {
    if (e.code !== "Space" || jumpCounter >= 2) return

    yVelocity = JUMP_SPEED
    jumpCounter += 1
}