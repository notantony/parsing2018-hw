import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.ParseException;
import java.util.concurrent.TimeUnit;

public class Tester {
    public void visualizerTest(String in, String out) {
        try (FileInputStream input = new FileInputStream(in)) {
            Visualizer visualizer = new Visualizer();
            Parser parser = new Parser();
            Files.createDirectories(Paths.get(out));
            try (Writer w = Files.newBufferedWriter(Paths.get(out + "\\out.tex"), StandardCharsets.UTF_8)) {
                visualizer.visualize(w, parser.parse(input));
            }
            String command = "F:\\Program Files\\MiKTeX 2.9\\miktex\\bin\\x64\\lualatex.exe";
            Files.createDirectories(Paths.get(out + "\\logs"));
            Process process = new ProcessBuilder(command, "out.tex")
                    .redirectOutput(Paths.get(out + "\\logs\\out.txt").toFile())
                    .redirectError(Paths.get(out + "\\logs\\err.txt").toFile())
                    .directory(Paths.get(out).toFile()).start();
            boolean closed = false;
            try {
                closed = process.waitFor(10, TimeUnit.SECONDS);
            } catch (InterruptedException ignored) {
            }
            if (closed) {
                if (process.exitValue() != 0) {
                    System.err.println("Warning: LuaLatex returned non-zero code, error may have occurred while visualising.\n" +
                            "See log files to get more info");
                }
            } else {
                System.err.println("Error occurred while visualising.\n" +
                        "See log files to get more info");
                process.destroy();
            }
        } catch (ParseException e) {
            System.err.println("Error occurred while parsing: " + e.getMessage());
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("Input/output error occurred: " + e.getMessage());
            e.printStackTrace();
        }

    }

    public void lexerTest(String s) {
        try (FileInputStream input = new FileInputStream(s)) {
            Lexer lexer = new Lexer(input);
            Lexer.Token tmp;
            while ((tmp = lexer.nextToken()) != Lexer.Token.EOF) {
                System.out.println(tmp + (tmp == Lexer.Token.IDENT ? " " + lexer.getData() : ""));
            }
            System.out.println(Lexer.Token.EOF);
        } catch (IOException e) {
            System.err.println("Error occurred while reading the file: " + e.getMessage());
            e.printStackTrace();
        } catch (ParseException e) {
            System.err.println("Error occurred while parsing: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
