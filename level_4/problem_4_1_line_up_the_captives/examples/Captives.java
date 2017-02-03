//import LineUpTheCaptives;

public class Captives{
    public static void main(String[] args)
    {
	int x = Integer.parseInt(args[0]);
	int y = Integer.parseInt(args[1]);
	int n = Integer.parseInt(args[2]);
	LineUpTheCaptives c = new LineUpTheCaptives();
	System.out.println(c.answer(x, y, n));
    }
}
