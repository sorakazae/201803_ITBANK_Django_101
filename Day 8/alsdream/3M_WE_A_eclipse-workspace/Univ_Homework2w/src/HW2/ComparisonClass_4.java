package HW2;
import java.util.Scanner;

import javax.swing.plaf.synth.SynthSpinnerUI;
public class ComparisonClass_4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("������ �Է��� �ּ��� : ");
		int Clss = sc.nextInt();
		if(Clss > 100) {
			System.out.println("������ 100�� ���� �� �����ϴ�");
		}
		else if(Clss >= 90) {
			System.out.println("����� ������ A �Դϴ�");
		}
		else if(Clss >= 80) {
			System.out.println("����� ������ B �Դϴ�");
		}
		else if(Clss >= 70) {
			System.out.println("����� ������ C �Դϴ�");
		}
		else if(Clss >= 60) {
			System.out.println("����� ������ D �Դϴ�");
		}
		else if(Clss >= 0) {
			System.out.println("���� �Դϴ�");
		}
		else {
			System.out.println("������ ������ �� �����ϴ�");
		}
	}

}
