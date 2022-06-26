import { setupGround, updateGround } from "./ground.js"
import { setupPlayer, updatePlayer, getPlayerRect } from "./player.js"
import { setupEnemy, updateEnemy, getEnemyRects } from "./enemy.js"

const WORLD_WIDTH = 100
const WORLD_HEIGHT = 35
const SPEED_SCALE_INCREASE = 0.000005

const worldElement = document.querySelector("[data-world]")
const scoreElement = document.querySelector("[data-score]")
const startScreenElement = document.querySelector("[data-start-screen]")


setPixelToWorldScale()
window.addEventListener("resize", setPixelToWorldScale)
document.addEventListener("keydown", handleStart, { once: true })

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
  updatePlayer(timeDifference, speedScale)
  updateEnemy(timeDifference, speedScale)
  updateSpeedScale(timeDifference)
  updateScore(timeDifference, speedScale)
  if (isLose()) {
    return handleLose()
  }
  lastTime = time
  window.requestAnimationFrame(update)
}

function isLose() {
  const playerRect = getPlayerRect()
  return getEnemyRects().some(rect => isCollision(rect, playerRect))
}

function isCollision(rect1, rect2) {
  return rect1.left < rect2.right && rect1.top < rect2.bottom && rect1.right > rect2.left && rect1.bottom > rect2.top
}

function updateScore(timeDifference, speedScale) {
  score += (timeDifference * 0.005 * speedScale)
  scoreElement.textContent = Math.floor(score)
}

function updateSpeedScale(timeDifference) {
  speedScale += timeDifference * SPEED_SCALE_INCREASE
}

function handleStart() {
  lastTime = null
  speedScale = 1
  score = 0
  setupGround()
  setupPlayer()
  setupEnemy()
  startScreenElement.classList.add("hide")
  window.requestAnimationFrame(update)
}

function handleLose() {
  setTimeout(() => {
    document.addEventListener("keydown", handleStart, { once: true })
  }, 100)
  startScreenElement.classList.remove("hide")
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