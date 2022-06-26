import {
    setCustomProperty,
    incrementCustomProperty,
    getCustomProperty,
  } from "./updateCustomProperty.js"
  
  const SPEED = 0.001
  const worldElem = document.querySelector("[data-world]")
  

  export function setupClouds() {
    document.querySelectorAll("[data-cloud]").forEach(cloud => {
        cloud.remove()
      })
    for (let i=0; i<5; i++){
        createClouds()
    }

  }
  
  export function updateClouds(timeDifference, speedScale) {
    document.querySelectorAll("[data-cloud]").forEach(cloud => {
      incrementCustomProperty(cloud, "--left", timeDifference * speedScale * SPEED * -1)
      if (getCustomProperty(cloud, "--left") <= -10) {
        cloud.remove()
        createClouds()
      }
    })

  }
  
  
  function createClouds() {
    const cloud = document.createElement("img")
    cloud.dataset.cloud = true
    cloud.src = "img/Cloud.png"
    cloud.classList.add("cloud")
    setCustomProperty(cloud, "--bottom", randomNumberBetween(25,80))
    setCustomProperty(cloud, "--left", randomNumberBetween(50,100))
    worldElem.append(cloud)
  }
  
  function randomNumberBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
  }