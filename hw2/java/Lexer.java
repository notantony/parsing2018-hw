import java.io.IOException;
import java.io.InputStream;
import java.text.ParseException;


public class Lexer {
    private InputStream is;
    private int i, sz, pos;
    private byte[] buffer;
    private String data;

    public Lexer(InputStream is) throws IOException {
        this.is = is;
        sz = pos = 0;
        i = -1;
        buffer = new byte[4096];
        readChar();
    }

    private int getChar() {
        if (sz == -1) {
            return -1;
        }
        return buffer[i] & 0xFF;
    }

    private void readChar() throws IOException {
        if (i + 1 == sz) {
            pos += sz;
            sz = is.read(buffer);
            i = -1;
        }
        i++;
    }

    public Token nextToken() throws ParseException, IOException {
        data = null;
        int c;
        while ((c = getChar()) != -1 && Character.isWhitespace(c)) {
            readChar();
        }
        switch (c) {
            case -1:
                return Token.EOF;
            case '(':
                readChar();
                return Token.LBRACKET;
            case ')':
                readChar();
                return Token.RBRACKET;
            case '*':
                readChar();
                return Token.PTR;
            case ';':
                readChar();
                return Token.SEMICOLON;
            case ',':
                readChar();
                return Token.COMMA;
            case '&':
                readChar();
                return Token.AMPERSAND;
        }
        if (Character.isLetter((char) c) || c == '_') {
            StringBuilder sb = new StringBuilder();
            while ((c = getChar()) != -1 && (Character.isLetterOrDigit(c) || c == '_')) {
                sb.append((char) c);
                readChar();
            }
            data = sb.toString();
            return Token.IDENT;
        }
        throw new ParseException("Unexpected symbol: " + ((char) c), getPosition());
    }

    public String getData() {
        String tmp = data;
        data = null;
        return tmp;
    }

    public int getPosition() {
        return pos + i;
    }

    public enum Token {
        IDENT, PTR, LBRACKET, RBRACKET, SEMICOLON, COMMA, EOF, AMPERSAND;

        @Override
        public String toString() {
            switch (this) {
                case PTR:
                    return "*";
                case LBRACKET:
                    return "(";
                case RBRACKET:
                    return ")";
                case SEMICOLON:
                    return ";";
                case COMMA:
                    return ",";
                case EOF:
                    return "$";
                case AMPERSAND:
                    return "&";
            }
            return "Id:";
        }
    }
}
