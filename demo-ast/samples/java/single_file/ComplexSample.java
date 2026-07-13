// File: ComplexSample.java
package com.example.parser;

// 1. Imports (Thường, tĩnh, và wildcard)
import java.util.List;
import java.util.ArrayList;
import java.io.IOException;
import static java.lang.Math.PI;

/**
 * ComplexSample: Bao phủ toàn diện các cú pháp (syntax) phức tạp của Java
 */
@SuppressWarnings("unchecked") // 2. Annotation cấp class
public abstract sealed class ComplexSample<T extends Number & Comparable<T>>
        extends Thread
        implements AutoCloseable
        permits ComplexSample.SubClass { // 3. Sealed class, Generics, Bounds, Extends, Implements

    // 4. Fields với nhiều modifier (static, final, volatile, transient), khai báo gộp, nhị phân/hexa
    private static final transient volatile int COMPLEX_CONSTANT = 0b1010_1010;
    protected T genericField;
    int x, y = 10, z; // Nhiều biến trên một dòng
    private @CustomAnnotation String annotatedField = "Test"; // Annotation cấp biến

    // 5. Khối khởi tạo (Initializers)
    static {
        System.out.println("Static initializer block: " + PI);
    }

    {
        System.out.println("Instance initializer block");
    }

    // 6. Hàm khởi tạo ném ngoại lệ (Throws clause)
    @Deprecated
    public ComplexSample(T value) throws IllegalArgumentException {
        super("ComplexThread");
        if (value == null) {
            throw new IllegalArgumentException("Giá trị không được null");
        }
        this.genericField = value;
    }

    // 7. Varargs, Generic Methods, Synchronized
    public synchronized <U> List<U> processElements(@CustomAnnotation final int count, U... elements) {
        List<U> result = new ArrayList<>();

        // 8. Vòng lặp với Labeled break/continue
        outerLabel:
        for (int i = 0; i < count; i++) {
            for (U element : elements) {
                if (element == null) continue;
                if (i == count - 1) break outerLabel;
                result.add(element);
            }
        }
        return result;
    }

    // 9. Java 16+ Pattern Matching & Java 14+ Switch Expression
    public String evaluateObject(Object obj) {
        // Pattern matching for instanceof
        if (obj instanceof String s && s.length() > 0) {
            return "String dài: " + s.length();
        }

        Day day = Day.MONDAY;
        // Switch expression (có trả về giá trị, sử dụng mũi tên -> và từ khóa yield)
        int dayScore = switch (day) {
            case MONDAY, FRIDAY -> 5;
            case TUESDAY -> {
                System.out.println("Xử lý đa dòng");
                yield 7; // Trả về giá trị trong khối block
            }
            default -> throw new IllegalStateException("Lỗi Enum: " + day);
        };

        return "Điểm: " + dayScore;
    }

    // 10. Try-with-resources, Multi-catch, Bitwise, Ternary Operator
    public void readFile() {
        // Try-with-resources tự động đóng file
        try (java.io.InputStream is = new java.io.FileInputStream("dummy.txt")) {
            int data = is.read();
            // Toán tử 3 ngôi (Ternary) và Toán tử thao tác bit (Bitwise)
            int processed = (data > 0) ? (data << 2) & 0xFF : ~data;
        } catch (java.io.FileNotFoundException | SecurityException e) { // Multi-catch
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("Lỗi IO");
        } finally {
            System.out.println("Luôn chạy ở cuối");
        }
    }

    // 11. Lambda Expressions & Method References
    public void executeLambdas() {
        Runnable r = () -> System.out.println("Chạy Lambda");
        List<String> names = List.of("A", "B");
        names.forEach(System.out::println); // Method reference
    }

    // 12. Records (Java 14+) - Lớp chứa dữ liệu siêu ngắn gọn
    public record DataRecord(int id, String name) {
        // Compact constructor (Hàm khởi tạo thu gọn)
        public DataRecord {// File: ComplexSample.java
package com.example.parser;// File: ComplexSample.java
package com.example.parser;

// 1. Imports (Thường, tĩnh, và wildcard)
import java.util.List;
import java.util.ArrayList;
import java.io.IOException;
import static java.lang.Math.PI;

/**
 * ComplexSample: Bao phủ toàn diện các cú pháp (syntax) phức tạp của Java
 */
@SuppressWarnings("unchecked") // 2. Annotation cấp class
public abstract sealed class ComplexSample<T extends Number & Comparable<T>>
        extends Thread
        implements AutoCloseable
        permits ComplexSample.SubClass { // 3. Sealed class, Generics, Bounds, Extends, Implements

    // 4. Fields với nhiều modifier (static, final, volatile, transient), khai báo gộp, nhị phân/hexa
    private static final transient volatile int COMPLEX_CONSTANT = 0b1010_1010;
    protected T genericField;
    int x, y = 10, z; // Nhiều biến trên một dòng
    private @CustomAnnotation String annotatedField = "Test"; // Annotation cấp biến

    // 5. Khối khởi tạo (Initializers)
    static {
        System.out.println("Static initializer block: " + PI);
    }

    {
        System.out.println("Instance initializer block");
    }

    // 6. Hàm khởi tạo ném ngoại lệ (Throws clause)
    @Deprecated
    public ComplexSample(T value) throws IllegalArgumentException {
        super("ComplexThread");
        if (value == null) {
            throw new IllegalArgumentException("Giá trị không được null");
        }
        this.genericField = value;
    }

    // 7. Varargs, Generic Methods, Synchronized
    public synchronized <U> List<U> processElements(@CustomAnnotation final int count, U... elements) {
        List<U> result = new ArrayList<>();

        // 8. Vòng lặp với Labeled break/continue
        outerLabel:
        for (int i = 0; i < count; i++) {
            for (U element : elements) {
                if (element == null) continue;
                if (i == count - 1) break outerLabel;
                result.add(element);
            }
        }
        return result;
    }

    // 9. Java 16+ Pattern Matching & Java 14+ Switch Expression
    public String evaluateObject(Object obj) {
        // Pattern matching for instanceof
        if (obj instanceof String s && s.length() > 0) {
            return "String dài: " + s.length();
        }

        Day day = Day.MONDAY;
        // Switch expression (có trả về giá trị, sử dụng mũi tên -> và từ khóa yield)
        int dayScore = switch (day) {
            case MONDAY, FRIDAY -> 5;
            case TUESDAY -> {
                System.out.println("Xử lý đa dòng");
                yield 7; // Trả về giá trị trong khối block
            }
            default -> throw new IllegalStateException("Lỗi Enum: " + day);
        };

        return "Điểm: " + dayScore;
    }

    // 10. Try-with-resources, Multi-catch, Bitwise, Ternary Operator
    public void readFile() {
        // Try-with-resources tự động đóng file
        try (java.io.InputStream is = new java.io.FileInputStream("dummy.txt")) {
            int data = is.read();
            // Toán tử 3 ngôi (Ternary) và Toán tử thao tác bit (Bitwise)
            int processed = (data > 0) ? (data << 2) & 0xFF : ~data;
        } catch (java.io.FileNotFoundException | SecurityException e) { // Multi-catch
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("Lỗi IO");
        } finally {
            System.out.println("Luôn chạy ở cuối");
        }
    }

    // 11. Lambda Expressions & Method References
    public void executeLambdas() {
        Runnable r = () -> System.out.println("Chạy Lambda");
        List<String> names = List.of("A", "B");
        names.forEach(System.out::println); // Method reference
    }

    // 12. Records (Java 14+) - Lớp chứa dữ liệu siêu ngắn gọn
    public record DataRecord(int id, String name) {
        // Compact constructor (Hàm khởi tạo thu gọn)
        public DataRecord {
            if (id < 0) throw new IllegalArgumentException("ID âm");
        }
    }

    // 13. Enums
    public enum Day {
        MONDAY, TUESDAY, FRIDAY
    }

    // 14. Lớp nội bộ (Inner Class)
    private class InnerClass {
        void display() {
            System.out.println("Hằng số outer: " + COMPLEX_CONSTANT);
        }
    }

    // 15. Lớp ẩn danh (Anonymous Class)
    Runnable anonymous = new Runnable() {
        @Override
        public void run() {
            System.out.println("Lớp ẩn danh");
        }
    };

    @Override
    public void close() throws Exception {
        // Implement AutoCloseable
    }

    // 16. Subclass để đáp ứng cấu trúc "sealed/permits"
    public static final class SubClass extends ComplexSample<Integer> {
        public SubClass(Integer value) {
            super(value);
        }
    }
}

// 17. Khai báo Custom Annotation
@interface CustomAnnotation {
    String value() default "Mặc định";
}

// 1. Imports (Thường, tĩnh, và wildcard)
import java.util.List;
import java.util.ArrayList;
import java.io.IOException;
import static java.lang.Math.PI;

/**
 * ComplexSample: Bao phủ toàn diện các cú pháp (syntax) phức tạp của Java
 */
@SuppressWarnings("unchecked") // 2. Annotation cấp class
public abstract sealed class ComplexSample<T extends Number & Comparable<T>>
        extends Thread
        implements AutoCloseable
        permits ComplexSample.SubClass { // 3. Sealed class, Generics, Bounds, Extends, Implements

    // 4. Fields với nhiều modifier (static, final, volatile, transient), khai báo gộp, nhị phân/hexa
    private static final transient volatile int COMPLEX_CONSTANT = 0b1010_1010;
    protected T genericField;
    int x, y = 10, z; // Nhiều biến trên một dòng
    private @CustomAnnotation String annotatedField = "Test"; // Annotation cấp biến

    // 5. Khối khởi tạo (Initializers)
    static {
        System.out.println("Static initializer block: " + PI);
    }

    {
        System.out.println("Instance initializer block");
    }

    // 6. Hàm khởi tạo ném ngoại lệ (Throws clause)
    @Deprecated
    public ComplexSample(T value) throws IllegalArgumentException {
        super("ComplexThread");
        if (value == null) {
            throw new IllegalArgumentException("Giá trị không được null");
        }
        this.genericField = value;
    }

    // 7. Varargs, Generic Methods, Synchronized
    public synchronized <U> List<U> processElements(@CustomAnnotation final int count, U... elements) {
        List<U> result = new ArrayList<>();

        // 8. Vòng lặp với Labeled break/continue
        outerLabel:
        for (int i = 0; i < count; i++) {
            for (U element : elements) {
                if (element == null) continue;
                if (i == count - 1) break outerLabel;
                result.add(element);
            }
        }
        return result;
    }

    // 9. Java 16+ Pattern Matching & Java 14+ Switch Expression
    public String evaluateObject(Object obj) {
        // Pattern matching for instanceof
        if (obj instanceof String s && s.length() > 0) {
            return "String dài: " + s.length();
        }

        Day day = Day.MONDAY;
        // Switch expression (có trả về giá trị, sử dụng mũi tên -> và từ khóa yield)
        int dayScore = switch (day) {
            case MONDAY, FRIDAY -> 5;
            case TUESDAY -> {
                System.out.println("Xử lý đa dòng");
                yield 7; // Trả về giá trị trong khối block
            }
            default -> throw new IllegalStateException("Lỗi Enum: " + day);
        };

        return "Điểm: " + dayScore;
    }

    // 10. Try-with-resources, Multi-catch, Bitwise, Ternary Operator
    public void readFile() {
        // Try-with-resources tự động đóng file
        try (java.io.InputStream is = new java.io.FileInputStream("dummy.txt")) {
            int data = is.read();
            // Toán tử 3 ngôi (Ternary) và Toán tử thao tác bit (Bitwise)
            int processed = (data > 0) ? (data << 2) & 0xFF : ~data;
        } catch (java.io.FileNotFoundException | SecurityException e) { // Multi-catch
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("Lỗi IO");
        } finally {
            System.out.println("Luôn chạy ở cuối");
        }
    }

    // 11. Lambda Expressions & Method References
    public void executeLambdas() {
        Runnable r = () -> System.out.println("Chạy Lambda");
        List<String> names = List.of("A", "B");
        names.forEach(System.out::println); // Method reference
    }

    // 12. Records (Java 14+) - Lớp chứa dữ liệu siêu ngắn gọn
    public record DataRecord(int id, String name) {
        // Compact constructor (Hàm khởi tạo thu gọn)
        public DataRecord {
            if (id < 0) throw new IllegalArgumentException("ID âm");
        }
    }

    // 13. Enums
    public enum Day {
        MONDAY, TUESDAY, FRIDAY
    }

    // 14. Lớp nội bộ (Inner Class)
    private class InnerClass {
        void display() {
            System.out.println("Hằng số outer: " + COMPLEX_CONSTANT);
        }
    }

    // 15. Lớp ẩn danh (Anonymous Class)
    Runnable anonymous = new Runnable() {
        @Override
        public void run() {
            System.out.println("Lớp ẩn danh");
        }
    };

    @Override
    public void close() throws Exception {
        // Implement AutoCloseable
    }

    // 16. Subclass để đáp ứng cấu trúc "sealed/permits"
    public static final class SubClass extends ComplexSample<Integer> {
        public SubClass(Integer value) {
            super(value);
        }
    }
}

// 17. Khai báo Custom Annotation
@interface CustomAnnotation {
    String value() default "Mặc định";
}
            if (id < 0) throw new IllegalArgumentException("ID âm");
        }
    }

    // 13. Enums
    public enum Day {
        MONDAY, TUESDAY, FRIDAY
    }

    // 14. Lớp nội bộ (Inner Class)
    private class InnerClass {
        void display() {
            System.out.println("Hằng số outer: " + COMPLEX_CONSTANT);
        }
    }

    // 15. Lớp ẩn danh (Anonymous Class)
    Runnable anonymous = new Runnable() {
        @Override
        public void run() {
            System.out.println("Lớp ẩn danh");
        }
    };

    @Override
    public void close() throws Exception {
        // Implement AutoCloseable
    }

    // 16. Subclass để đáp ứng cấu trúc "sealed/permits"
    public static final class SubClass extends ComplexSample<Integer> {
        public SubClass(Integer value) {
            super(value);
        }
    }
}

// 17. Khai báo Custom Annotation
@interface CustomAnnotation {
    String value() default "Mặc định";
}