package GameObjects;

import java.awt.*;
import java.awt.image.BufferedImage;

public class Obstacle extends Enemy {

    private BufferedImage image;
    private int posX, posY;
    private Rectangle rect;
    private MainCharacter mainCharacter;
    private boolean gotScore = false;

    public Obstacle(MainCharacter mainCharacter) {
        this.mainCharacter = mainCharacter;
        posX = 200;
        posY = 70;
        rect = new Rectangle();
    }

    public void update() {
        posX -= 4;
        rect.x = posX;
        rect.y = posY;
        rect.width = image.getWidth();
        rect.height = image.getHeight();
    }

    @Override
    public boolean isOutOfScreen() {
        return (posX + image.getWidth() < 0);
    }

    @Override
    public boolean isOver() {
        return (mainCharacter.getX() > posX);
    }

    @Override
    public boolean gotScore() {
        return gotScore;
    }

    @Override
    public void setGotScore(boolean gotScore) {
        this.gotScore = gotScore;
    }

    @Override
    public Rectangle getBound() {
        return rect;
    }

    @Override
    public void draw(Graphics g) {
        g.drawImage(image, posX, posY, null);
    }

    public void setPosX(int x) {
        posX = x;
    }

    public void setPosY(int y) {
        posY = y;
    }

    public void setImage(BufferedImage image) {
        this.image = image;
    }


}
