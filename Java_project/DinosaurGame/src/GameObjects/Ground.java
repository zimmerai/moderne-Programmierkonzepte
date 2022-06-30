package GameObjects;

import UI.GameScreen;
import Util.Resource;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static UI.GameScreen.GROUNDY;

public class Ground {

    private List<ImageGround> imageList;
    private BufferedImage imageGround1, imageGround2, imageGround3;
    private Random random;

    public Ground(GameScreen game) {
        random = new Random();
        imageGround1 = Resource.getResourceImage("Java_project/DinosaurGame/data/ground1.png");
        imageGround2 = Resource.getResourceImage("Java_project/DinosaurGame/data/ground2.png");
        imageGround3 = Resource.getResourceImage("Java_project/DinosaurGame/data/ground3.png");
        imageList = new ArrayList<ImageGround>();
        int numberOfGroundTitle = 600 / imageGround1.getWidth() + 2;
        for (int i = 0; i < numberOfGroundTitle; i++) {
            ImageGround imageGround = new ImageGround();
            imageGround.posX = (int) (i * imageGround1.getWidth());
            imageGround.image = getGroundImage();
            imageList.add(imageGround);
        }
    }

    public void update() {
        for (ImageGround imageGround : imageList) {
            imageGround.posX-= 4;
        }
        ImageGround firstElement = imageList.get(0);
        if (firstElement.posX + imageGround1.getWidth() < 0) {
            firstElement.posX = imageList.get(imageList.size() - 1).posX + imageGround1.getWidth();
            imageList.add(firstElement);
            imageList.remove(0);

        }
    }

    public void draw(Graphics g) {
        for (ImageGround imageGround : imageList) {
            g.drawImage(imageGround.image, imageGround.posX, (int) GROUNDY - 20, null);
        }
    }

    private BufferedImage getGroundImage() {
        int i = random.nextInt(5);
        switch (i) {
            case 0:
                return imageGround1;
            case 1:
                return imageGround3;
            default:
                return imageGround2;
        }
    }

    private class ImageGround {
        int posX;
        BufferedImage image;
    }
}
