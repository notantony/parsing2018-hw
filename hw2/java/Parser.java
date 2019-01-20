import java.io.IOException;
import java.io.InputStream;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;

public class Parser {
    private Lexer lexer;
    private Lexer.Token curToken;

    public Node parse(InputStream is) throws IOException, ParseException {
        lexer = new Lexer(is);
        curToken = lexer.nextToken();
        Node tmp = takeS();
        if (curToken != Lexer.Token.EOF) {
            throw unexpectedToken();
        }
        return tmp;
    }

    private Node eps() {
        return new Node("eps");
    }

    private ParseException unexpectedToken() {
        if (curToken == Lexer.Token.EOF) return new ParseException("Unexpected end of file", lexer.getPosition());
        return new ParseException("Unexpected token: " + curToken, lexer.getPosition());
    }

    private Node takeIdent() throws ParseException, IOException {
        if (curToken != Lexer.Token.IDENT) {
            throw unexpectedToken();
        }
        String tmp = lexer.getData();
        curToken = lexer.nextToken();
        return new Node("I: " + tmp);
    }


    private Node takeToken(Lexer.Token token) throws ParseException, IOException {
        if (curToken != token) {
            throw unexpectedToken();
        }
        String tmp = token.toString();
        curToken = lexer.nextToken();
        return new Node(tmp);
    }

    private Node takeS() throws IOException, ParseException {
        List<Node> children = new ArrayList<>();
        Node cur = new Node("S", children);
        switch (curToken) {
            case IDENT:
                children.add(takeT());
                children.add(takeIdent());
                children.add(takeToken(Lexer.Token.LBRACKET));
                children.add(takeA());
                children.add(takeToken(Lexer.Token.RBRACKET));
                children.add(takeToken(Lexer.Token.SEMICOLON));
                break;
            default:
                throw unexpectedToken();
        }
        return cur;
    }

    private Node takeT() throws ParseException, IOException {
        List<Node> children = new ArrayList<>();
        Node cur = new Node("T", children);
        switch (curToken) {
            case IDENT:
                children.add(takeIdent());
                children.add(takeM());
                break;
            default:
                throw unexpectedToken();
        }
        return cur;
    }

    private Node takeA() throws IOException, ParseException {
        List<Node> children = new ArrayList<>();
        Node cur = new Node("A", children);
        switch (curToken) {
            case RBRACKET:
                children.add(eps());
                break;
            case IDENT:
                children.add(takeT());
                children.add(takeIdent());
                children.add(takeA_());
                break;
            default:
                throw unexpectedToken();
        }
        return cur;
    }

    private Node takeA_() throws IOException, ParseException {
        List<Node> children = new ArrayList<>();
        Node cur = new Node("A'", children);
        switch (curToken) {
            case RBRACKET:
                children.add(eps());
                break;
            case COMMA:
                children.add(takeToken(Lexer.Token.COMMA));
                children.add(takeT());
                children.add(takeIdent());
                children.add(takeA_());
                break;
            default:
                throw unexpectedToken();
        }
        return cur;
    }

    private Node takeM() throws IOException, ParseException {
        List<Node> children = new ArrayList<>();
        Node cur = new Node("M", children);
        switch (curToken) {
            case IDENT:
                children.add(eps());
                break;
            case PTR:
                children.add(takeToken(Lexer.Token.PTR));
                children.add(takeM());
                break;
            case AMPERSAND:
                children.add(takeToken(Lexer.Token.AMPERSAND));
                break;
            default:
                throw unexpectedToken();
        }
        return cur;
    }

    public class Node {
        private List<Node> children;
        private String data;

        public Node(String data) {
            this.data = data;
        }

        public Node(String data, List<Node> children) {
            this.data = data;
            this.children = children;
        }

        public String getData() {
            return data;
        }

        public List<Node> getChildren() {
            return children;
        }
    }
}