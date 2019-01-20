public class Main {

    public static void main(String[] args) {
        singleTest();
        //allTests();
    }

    public static void singleTest() {
        Manager manager = new Manager();
        manager.parse("input");
    }

    public static void allTests() {
        int N = 12;
        Manager manager = new Manager();
        for (int id = 0; id < N ; id++) {
            System.err.println("Running test" + (id + 1));
            manager.parse("tests/" + (id + 1));
        }
    }
}
