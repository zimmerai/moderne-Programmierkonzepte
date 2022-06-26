import {
    setCustomProperty,
    incrementCustomProperty,
    getCustomProperty,
  } from "./updateCustomProperty.js"
  
  const SPEED = 0.05
  const ENEMY_INTERVAL_MIN = 500
  const ENEMY_INTERVAL_MAX = 2000
  const worldElem = document.querySelector("[data-world]")
  
  let nextEnemyTime
  export function setupEnemy() {
    nextEnemyTime = ENEMY_INTERVAL_MIN
    document.querySelectorAll("[data-enemy]").forEach(enemy => {
      enemy.remove()
    })
  }
  
  export function updateEnemy(timeDifference, speedScale) {
    document.querySelectorAll("[data-enemy]").forEach(enemy => {
      incrementCustomProperty(enemy, "--left", timeDifference * speedScale * SPEED * -1)
      if (getCustomProperty(enemy, "--left") <= -100) {
        enemy.remove()
      }
    })
  
    if (nextEnemyTime <= 0) {
      createEnemy()
      nextEnemyTime =
        randomNumberBetween(ENEMY_INTERVAL_MIN, ENEMY_INTERVAL_MAX) / speedScale
    }
    nextEnemyTime -= timeDifference
  }
  
  export function getEnemyRects() {
    return [...document.querySelectorAll("[data-enemy]")].map(enemy => {
      return enemy.getBoundingClientRect()
    })
  }
  
  function createEnemy() {
    let calculateEnemyType
    const enemy = document.createElement("img")
    enemy.dataset.enemy = true
    calculateEnemyType = Math.random() * 100
    if (calculateEnemyType <= 50) {
        enemy.src = "img/Enemy1-coloured.png"
        enemy.classList.add("enemy1")
    } else {
        enemy.src = "img/Enemy2_coloured.png"
        enemy.classList.add("enemy2")
    }
    setCustomProperty(enemy, "--left", 100)
    worldElem.append(enemy)
  }
  
  function randomNumberBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
  }