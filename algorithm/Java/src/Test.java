public class Test {

    public static void main(String[] args) {
        String str = "1234";
        StringBuffer buffer = new StringBuffer(str);
        String result = buffer.reverse().toString();
        System.out.println(result);
    }
}
