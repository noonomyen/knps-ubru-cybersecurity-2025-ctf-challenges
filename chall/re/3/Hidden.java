public class Hidden {
    private static final byte[] secret = new byte[] {
            0x16, 0x01, 0x1f, 0x1c, 0x54, 0x56, 0x3b, 0x50, 0x5d, 0x50, 0x55, 0x0a, 0x3b, 0x5c, 0x11, 0x53, 0x3b, 0x0e,
            0x50, 0x12, 0x50, 0x19
    };

    public static void main(String[] args) {
        System.out.println("Access Denied.");
    }

    private static void func710n() {
        StringBuilder b = new StringBuilder();
        for (byte s : secret) {
            b.append((char) (s ^ 0x64));
        }
        System.out.println("Flag: " + b.toString());
    }
}
