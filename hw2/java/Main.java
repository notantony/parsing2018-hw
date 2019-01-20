

public class Main {
    public static void main(String[] args) {
        singleTest("input.txt", "out");
        //runTests(18);
    }

    private static void singleTest(String inputFile, String outputDirectory) {
        Tester tester = new Tester();
        tester.visualizerTest(inputFile, outputDirectory);
    }

    private static void runTests(int n) {
        Tester tester = new Tester();
        for (int i = 1; i <= n; i++) {
            System.err.println("Running test #" + i);
            tester.visualizerTest("tests\\in" + i + ".txt", "tests\\out" + i);
        }
    }
}
