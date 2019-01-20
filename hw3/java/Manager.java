import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.ParseException;

public class Manager {
    public void parse(String path) {
        try (InputStream is = Files.newInputStream(Paths.get(path));
             Writer writer = Files.newBufferedWriter(Paths.get(path + ".out"))) {
            CharStream stream = CharStreams.fromStream(is);
            MainLexer lexer = new MainLexer(stream);
            CommonTokenStream tokenStream = new CommonTokenStream(lexer);
            MainParser parser = new MainParser(tokenStream);
            parser.addErrorListener(new BaseErrorListener() {
                @Override
                public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol, int line, int charPositionInLine, String msg, RecognitionException e) {
                    throw new RuntimeException("unexpected symbol \'" + offendingSymbol + "\' , line " + line + "position " + charPositionInLine);
                }
            });
            ParseTree tree = parser.start();
            MyVisitor visitor = new MyVisitor();
            visitor.visit(tree);
            writer.write(visitor.getOutput());
        } catch (IOException e) {
            System.err.println("Error occurred while reading/writing file: " + e.getMessage());
            e.printStackTrace();
        } catch (RuntimeException e) {
            System.err.println("Error occurred while parsing: " + e.getMessage());
            e.printStackTrace();
        }
    }
}

