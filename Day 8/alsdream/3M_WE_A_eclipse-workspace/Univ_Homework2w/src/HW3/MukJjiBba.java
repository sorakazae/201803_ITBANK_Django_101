package HW3;
import java.util.Scanner;
import java.util.Random;
public class MukJjiBba {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random ran = new Random();
		
		int com = ran.nextInt(3);
		
		System.out.println("묵찌빠 게임");
		System.out.print("주먹은 0, 보는 1, 가위는 2 를 입력해주세요 : ");
		int usr = sc.nextInt();

		if(usr>2 || usr<0) {
			System.out.println("옳바른 값을 입력해주세요");
		}
		else if(com == usr) {
			System.out.println("비겼습니다");
			System.out.println("컴퓨터가 낸 값 : "+ com);
		}
		else if((com==1&&usr==0)||(com==2&&usr==1)||(com==0&&usr==2)) {
			System.out.println("졌습니다");
			System.out.println("컴퓨터가 낸 값 : "+ com);
		}
		else {
			System.out.println("이겼습니다");
			System.out.println("컴퓨터가 낸 값 : "+ com);
			
		}
	}

}
