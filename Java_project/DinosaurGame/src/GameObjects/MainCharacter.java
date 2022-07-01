package GameObjects;

import Util.Animation;
import Util.Resource;


import java.awt.*;

import static UI.GameScreen.GRAVITY;
import static UI.GameScreen.GROUNDY;

public class MainCharacter {

    private float x = 0;
    private float y = 0;
    private float speedY = 0;
    private Animation characterRun;
    private Rectangle rect;
    private boolean isAlive = true;
    private static final int maxJumps = 2;
    private static final int jumpCooldown = 10;
    private int jumps = 0;                   //number of remaining jumps
    private int jumpTimer = 1;




    public MainCharacter() {
        characterRun = new Animation(100);
        characterRun.addFrame(Resource.getResourceImage("Java_project/DinosaurGame/data/Mario1_coloured.png"));
        characterRun.addFrame(Resource.getResourceImage("Java_project/DinosaurGame/data/Mario2_coloured.png"));
        rect = new Rectangle();


    }

    public void update() {
        characterRun.update();
        //for jumping
        if (y >= GROUNDY - characterRun.getFrame().getHeight()) {
            speedY = 0;
            y = GROUNDY - characterRun.getFrame().getHeight();
            jumps = maxJumps;
            jumpTimer = 0;
        } else {
            speedY += GRAVITY;
            y += speedY;
            jumpTimer += 1;
        }
        rect.x = (int) x;
        rect.y = (int) y;
        rect.width = characterRun.getFrame().getWidth();
        rect.height = characterRun.getFrame().getHeight();
    }

    public void setJumps(int jumps) {
        this.jumps = jumps;
    }

    public void setJumpTimer(int jumpTimer) {
        this.jumpTimer = jumpTimer;
    }

    public Rectangle getBound() {
        return rect;
    }

    public void draw(Graphics g) {
        g.setColor(Color.black);
        g.drawImage(characterRun.getFrame(), (int) x, (int) y, null);
    }

    public void jump() {
        if((jumpTimer==0 || (jumps>0 && jumpTimer>jumpCooldown)) && isAlive) {
            speedY = -3.5f;
            y += speedY;
            jumps -= 1;
            jumpTimer = 1;
        }
    }

    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public float getSpeedY() {
        return speedY;
    }

    public void setSpeedY(float speedY) {
        this.speedY = speedY;
    }

    public void setAlive(boolean alive) {
        isAlive = alive;
    }

    public boolean getAlive() {
        return isAlive;
    }


}
