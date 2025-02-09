package HW2;
import java.util.Scanner;
public class CtoF_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("섭씨 온도를 입력해주세요 : ");
		float C = sc.nextFloat();
		double F = C* 1.8 + 32;
		System.out.println("화씨 온도는 "+F+"F 입니다");
	}

}
