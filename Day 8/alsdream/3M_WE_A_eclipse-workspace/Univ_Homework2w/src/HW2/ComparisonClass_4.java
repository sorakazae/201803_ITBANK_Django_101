package HW2;
import java.util.Scanner;

import javax.swing.plaf.synth.SynthSpinnerUI;
public class ComparisonClass_4 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("점수를 입력해 주세요 : ");
		int Clss = sc.nextInt();
		if(Clss > 100) {
			System.out.println("점수는 100을 넘을 수 없습니다");
		}
		else if(Clss >= 90) {
			System.out.println("당신의 학점은 A 입니다");
		}
		else if(Clss >= 80) {
			System.out.println("당신의 학점은 B 입니다");
		}
		else if(Clss >= 70) {
			System.out.println("당신의 학점은 C 입니다");
		}
		else if(Clss >= 60) {
			System.out.println("당신의 학점은 D 입니다");
		}
		else if(Clss >= 0) {
			System.out.println("낙제 입니다");
		}
		else {
			System.out.println("점수는 음수일 수 없습니다");
		}
	}

}
