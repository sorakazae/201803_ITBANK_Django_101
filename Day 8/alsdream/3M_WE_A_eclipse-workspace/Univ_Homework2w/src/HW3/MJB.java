package HW3;

import java.util.Random;
import java.util.Scanner;

public class MJB {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random ran = new Random();
		
		int com = ran.nextInt(3);
		
		System.out.println("묵찌빠 게임");
		System.out.print("주먹은 0, 보는 1, 가위는 2 를 입력해주세요 : ");
		int usr = sc.nextInt();

		if(com == 0) {
			if(usr == 0) {
				System.out.println("비겼습니다");
				System.out.println("컴퓨터가 낸 것 : 주먹 / 사용자가 낸 것 : 주먹");
			}
			else if(usr == 1) {
				System.out.println("이겼습니다");
				System.out.println("컴퓨터가 낸 것 : 주먹 / 사용자가 낸 것 : 보");
			}
			else if(usr == 2) {
				System.out.println("졌습니다");
				System.out.println("컴퓨터가 낸 것 : 주먹 / 사용자가 낸 것 : 가위");
			}
			else {
				System.out.println("옳바른 값을 입력해주세요");
			}
		}
		else if(com == 1) {
			if(usr == 0) {
				System.out.println("졌습니다");
				System.out.println("컴퓨터가 낸 것 : 보 / 사용자가 낸 것 : 주먹");
			}
			else if(usr == 1) {
				System.out.println("비겼습니다");
				System.out.println("컴퓨터가 낸 것 : 보 / 사용자가 낸 것 : 보");
			}
			else if(usr == 2) {
				System.out.println("이겼습니다");
				System.out.println("컴퓨터가 낸 것 : 보 / 사용자가 낸 것 : 가위");
			}
			else {
				System.out.println("옳바른 값을 입력해주세요");
			}
		}
		else {
			if(usr == 0) {
				System.out.println("이겼습니다");
				System.out.println("컴퓨터가 낸 것 : 가위 / 사용자가 낸 것 : 주먹");
			}
			else if(usr == 1) {
				System.out.println("졌습니다");
				System.out.println("컴퓨터가 낸 것 : 가위 / 사용자가 낸 것 : 보");
			}
			else if(usr == 2) {
				System.out.println("비겼습니다");
				System.out.println("컴퓨터가 낸 것 : 가위 / 사용자가 낸 것 : 가위");
			}
			else {
				System.out.println("옳바른 값을 입력해주세요");
			}
		}
	}

}
