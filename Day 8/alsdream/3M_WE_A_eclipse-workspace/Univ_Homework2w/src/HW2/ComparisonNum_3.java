package HW2;
import java.util.Scanner;
public class ComparisonNum_3 {

	public static void main(String[] args) {
		System.out.println("���� �� ���α׷�");
		Scanner sc = new Scanner(System.in);
		System.out.print("ù��° ���ڸ� �Է����ּ��� : ");
		int a = sc.nextInt();
		System.out.print("�ι�° ���ڸ� �Է����ּ��� : ");
		int b = sc.nextInt();
		
		if(a>b) {
			System.out.println("ù��° ������ "+a+" �� Ů�ϴ�");
		}
		else if(a==b) {
			System.out.println("�� ���� �����ϴ�");
		}
		else {
			System.out.println("�ι�° ������ "+b+" �� Ů�ϴ�");
		}

	}

}
