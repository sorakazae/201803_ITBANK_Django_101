package HW2;
import java.util.Scanner;
public class CtoF_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("���� �µ��� �Է����ּ��� : ");
		float C = sc.nextFloat();
		double F = C* 1.8 + 32;
		System.out.println("ȭ�� �µ��� "+F+"F �Դϴ�");
	}

}
