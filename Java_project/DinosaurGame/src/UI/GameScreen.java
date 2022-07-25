package UI;

import GameObjects.*;
import Util.Resource;
import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;

public class GameScreen extends JPanel implements Runnable, KeyListener {

    public static final int GAME_BEGIN_STATE = 0;
    public static final int GAME_PLAY_STATE = 1;
    public static final int GAME_OVER_STATE = 2;

    public static final float GRAVITY = 0.3f;
    public static final float GROUNDY = 110;
    private MainCharacter mainCharacter;
    private Thread thread;
    private Ground ground;
    private Clouds clouds;
    private EnemyManager enemyManager;
    private int gameState = GAME_BEGIN_STATE;
    private BufferedImage imageGameOverText;
    private boolean jumpedInGame = false;

    public void setScore(int score) {
        this.score = score;
    }

    private static final int FPS = 60;                  //Frames per second
    private static final float FRAMETIME = 1000/FPS;     //Sleep function takes milliseconds, therefore 1000ms divided by fps
    private static final int GAMEOVER_FRAMES = 40;
    private int score;

    public GameScreen() {
        thread = new Thread(this);
        setVisible(true);
        mainCharacter = new MainCharacter();
        mainCharacter.setX(50);
        mainCharacter.setY(60);
        ground = new Ground(this);
        clouds = new Clouds();
        enemyManager = new EnemyManager(mainCharacter, this);
        imageGameOverText = Resource.getResourceImage("Java_project/DinosaurGame/data/gameover_text.png");
    }

    public void startGame() {
        thread.start();
    }

    @Override
    public void run() {
        while (true) {
            try {
                update();
                repaint();
                Thread.sleep((long) FRAMETIME);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void update(){
        switch (gameState){
            case GAME_PLAY_STATE:
                mainCharacter.update();
                ground.update();
                clouds.update();
                enemyManager.update();
                if(!mainCharacter.getAlive()){
                    gameState = GAME_OVER_STATE;
                }
                break;
        }
    }

    public void plusScore(int score){
        this.score += score;
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.decode("#f7f7f7"));
        g.fillRect(0, 0, getWidth(), getHeight());


        switch (gameState) {
            case GAME_BEGIN_STATE:
                mainCharacter.draw(g);
                break;
            case GAME_PLAY_STATE:
                clouds.draw(g);
                ground.draw(g);
                mainCharacter.draw(g);
                enemyManager.draw(g);
                g.drawString("HI" + String.valueOf(score), 500, 20);
                break;
            case GAME_OVER_STATE:
                clouds.draw(g);
                ground.draw(g);
                mainCharacter.draw(g);
                enemyManager.draw(g);
                g.drawString("HI" + String.valueOf(score), 500, 20);
                g.drawImage(imageGameOverText, 200,50, null);
                break;

        }

    }

    private void resetGame(){
        enemyManager.reset();
        try{
        Thread.sleep((long)(2*FRAMETIME));
        }catch(InterruptedException e){
            e.printStackTrace();
        }
        mainCharacter.setRemainingJumps(0);
        mainCharacter.setJumpTimer(1);
        mainCharacter.setAlive(true);
        mainCharacter.setX(50);
        mainCharacter.setY(GROUNDY);
        setScore(0);

    }

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if(gameState == GAME_PLAY_STATE) {
            mainCharacter.jump();
            jumpedInGame = true;
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        switch (e.getKeyCode()){
            case KeyEvent.VK_SPACE:
                if(gameState == GAME_BEGIN_STATE){
                    gameState = GAME_PLAY_STATE;
                }else if(gameState == GAME_OVER_STATE && jumpedInGame){
                    jumpedInGame = false;
                }else if(gameState == GAME_OVER_STATE){
                    try {
                        Thread.sleep((long) (GAMEOVER_FRAMES*FRAMETIME));
                    }catch(InterruptedException ex){
                        ex.printStackTrace();
                    }
                    resetGame();
                    gameState = GAME_PLAY_STATE;
                }
                break;
        }
    }
}
