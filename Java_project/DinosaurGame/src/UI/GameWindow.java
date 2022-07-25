package UI;

import javax.swing.*;
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

    

    public static void main(String[] args) throws MalformedURLException {
        GameWindow gw = new GameWindow();
        gw.startGame();
    }

}
