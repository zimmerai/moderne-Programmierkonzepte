package UI;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;

public class GameWindow extends JFrame {

    private GameScreen gameScreen;

    public GameWindow() throws MalformedURLException {
        super("Jump - Jump - Jump!");
        setSize(600,175);
        setLocation(500, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        gameScreen = new GameScreen();
        add(gameScreen);
        addKeyListener(gameScreen);
    }

    public void startGame(){
        setVisible(true);
        gameScreen.startGame();
    }

    public void paint(Graphics g){
        super.paint(g);
        BufferedImage image = null;
        try{
            image = ImageIO.read(new File("data/cactus1.png"));
            g.drawImage(image, 300, 400, null);
        }catch (IOException e){
            e.printStackTrace();
        }

    }

    public static void main(String[] args) throws MalformedURLException {
        GameWindow gw = new GameWindow();
        gw.startGame();
    }

}
