package GameObjects;

import GameObjects.Obstacle;
import GameObjects.Enemy;
import UI.GameScreen;
import Util.Resource;
import com.company.Main;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class EnemyManager {

    private List<Enemy> enemies;
    private Random random;
    private BufferedImage imageObstacle1, imageObstacle2;
    private MainCharacter mainCharacter;
    private GameScreen gameScreen;

    public EnemyManager(MainCharacter mainCharacter, GameScreen gameScreen) {
        this.gameScreen = gameScreen;
        this.mainCharacter = mainCharacter;
        enemies = new ArrayList<Enemy>();
        imageObstacle1 = Resource.getResourceImage("data/Enemy1-coloured.png");
        imageObstacle2 = Resource.getResourceImage("data/Enemy2_coloured.png");
        random = new Random();

        enemies.add(getRandomObstacle());
    }

    public void update(){
        for(Enemy e: enemies){
            e.update();
            if(e.isOver() && !e.gotScore()){
                gameScreen.plusScore(20);
                e.setGotScore(true);
            }
            if(e.getBound().intersects(mainCharacter.getBound())){
                mainCharacter.setAlive(false);
            }
        }
        Enemy firstEnemy = enemies.get(0);
        if(firstEnemy.isOutOfScreen()){
            enemies.remove(firstEnemy);
            enemies.add(getRandomObstacle());
        }
    }

    public void draw(Graphics g){
        for(Enemy e : enemies){
            e.draw(g);
        }
    }

    public void reset(){
        enemies.clear();
        enemies.add(getRandomObstacle());
    }

    private Obstacle getRandomObstacle(){
        Obstacle obstacle = new Obstacle(mainCharacter);
        obstacle.setPosX(600);
        obstacle.setPosY(80);

        if(random.nextBoolean()){
            obstacle.setImage(imageObstacle1);
        }else {
            obstacle.setImage(imageObstacle2);
        }
        return obstacle;
    }

}


