import { incrementCustomProperty, getCustomProperty, setCustomProperty } from "./updateCustomProperty.js"

const playerElement = document.querySelector("[data-player]")
const JUMP_SPEED = 0.45
const GRAVITY = 0.0017
const PLAYER_ANIMATION_COUNT = 2
const ANIMATION_TIME = 150

let isJumping
let playerAnimation
let currentAnimationTime
let yVelocity
export function setupPlayer () {
    isJumping = false
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
    if (isJumping){
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
    if(!isJumping) return

    incrementCustomProperty(playerElement, "--bottom", yVelocity * timeDifference)
    
    if (getCustomProperty(playerElement, "--bottom") <= 0){
        setCustomProperty(playerElement, "--bottom", 0)
        isJumping = false
    }

    yVelocity -= GRAVITY * timeDifference

}

function onJump(e) {
    if (e.code !== "Space" || isJumping) return

    yVelocity = JUMP_SPEED
    isJumping = true
}