import { setupGround, updateGround } from "./ground.js"

const WORLD_WIDTH = 100
const WORLD_HEIGHT = 30
const SPEED_SCALE_INCREASE = 0.00001

const worldElement = document.querySelector("[data-world]")
const scoreElement = document.querySelector("[data-score]")
const startScreenElement = document.querySelector("[data-start-screen]")


setPixelToWorldScale()
window.addEventListener("resize", setPixelToWorldScale)
document.addEventListener("keydown", handleStart, {once: true})

let lastTime
let speedScale
let score
function update(time) {
  if (lastTime == null) {
    lastTime = time
    window.requestAnimationFrame(update)
    return
  }
  const timeDifference = time - lastTime

  updateGround(timeDifference, speedScale)
  updateSpeedScale(timeDifference)
  updateScore(timeDifference, speedScale)
  lastTime = time
  window.requestAnimationFrame(update)
}

function updateScore(timeDifference, speedScale) {
  score += (timeDifference *0.005 * speedScale)
  scoreElement.textContent = Math.floor(score)
}

function updateSpeedScale(timeDifference){
  speedScale += timeDifference * SPEED_SCALE_INCREASE
  console.log(speedScale)
}

function handleStart() {
  lastTime = null
  speedScale = 1
  score = 0
  setupGround()
  startScreenElement.classList.add("hide")
  window.requestAnimationFrame(update)
}

function setPixelToWorldScale() {
  let worldToPixelScale
  if (window.innerWidth / window.innerHeight < WORLD_WIDTH / WORLD_HEIGHT) {
    worldToPixelScale = window.innerWidth / WORLD_WIDTH
  } else {
    worldToPixelScale = window.innerHeight / WORLD_HEIGHT
  }

  worldElement.style.width = `${WORLD_WIDTH * worldToPixelScale}px`
  worldElement.style.height = `${WORLD_HEIGHT * worldToPixelScale}px`
}