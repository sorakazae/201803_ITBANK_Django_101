package HW2;
import java.util.Scanner;
public class ComparisonNum_3 {

	public static void main(String[] args) {
		System.out.println("숫자 비교 프로그램");
		Scanner sc = new Scanner(System.in);
		System.out.print("첫번째 숫자를 입력해주세요 : ");
		int a = sc.nextInt();
		System.out.print("두번째 숫자를 입력해주세요 : ");
		int b = sc.nextInt();
		
		if(a>b) {
			System.out.println("첫번째 숫자인 "+a+" 가 큽니다");
		}
		else if(a==b) {
			System.out.println("두 수가 같습니다");
		}
		else {
			System.out.println("두번째 숫자인 "+b+" 가 큽니다");
		}

	}

}
