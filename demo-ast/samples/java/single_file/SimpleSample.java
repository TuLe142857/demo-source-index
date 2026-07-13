/**
 * This is class docstring
 */
public class SimpleSample {
    private int number;
    private String text;

    public SimpleSample(int number, String text) {
        this.number = number;
        this.text = text;
    }

    public void printInfo() {
        System.out.println(text + ": " + number);
    }

    public static void main(String[] args) {
        SimpleSample sample = new SimpleSample(42, "Hello Tree-sitter");
        sample.printInfo();
    }
}