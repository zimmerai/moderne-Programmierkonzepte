import {
    setCustomProperty,
    incrementCustomProperty,
    getCustomProperty,
  } from "./updateCustomProperty.js"
  
  const SPEED = 0.05
  const SPEED_BULLET = 0.08
  const ENEMY_INTERVAL_MIN = 1000
  const ENEMY_INTERVAL_MAX = 2500
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
    if (enemy.className == "enemy3") {
        incrementCustomProperty(enemy, "--left", timeDifference * speedScale * SPEED_BULLET * -1)
    } else {
        incrementCustomProperty(enemy, "--left", timeDifference * speedScale * SPEED * -1)
    }
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
  
  //Hitbox für Kollision von den Gegnern
  export function getEnemyRects() {
    return [...document.querySelectorAll("[data-enemy]")].map(enemy => {
      return enemy.getBoundingClientRect()
    })
  }
  
  function createEnemy() {
    let calculateEnemyType
    const enemy = document.createElement("img")
    enemy.dataset.enemy = true
    calculateEnemyType = Math.random() * 30
    if (calculateEnemyType <= 10) {
        enemy.src = "img/Enemy1-coloured.png"
        enemy.classList.add("enemy1")
    } else if ( calculateEnemyType > 10 && calculateEnemyType >= 20) {
        enemy.src = "img/Enemy2_coloured.png"
        enemy.classList.add("enemy2")
    } else {
        enemy.src = "img/Bullet.png"
        enemy.classList.add("enemy3")
    }
    setCustomProperty(enemy, "--left", 100)
    worldElem.append(enemy)
  }
  
  function randomNumberBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
  }