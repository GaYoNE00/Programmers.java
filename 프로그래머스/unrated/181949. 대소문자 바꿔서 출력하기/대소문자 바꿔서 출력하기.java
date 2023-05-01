import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        char[] charArray = a.toCharArray();

        for (char c : charArray) {
        	if(Character.isUpperCase(c)) {
        		System.out.print(String.valueOf(c).toLowerCase());
        	}else {
        		System.out.print(String.valueOf(c).toUpperCase());        		
        	}
        }
    }
}