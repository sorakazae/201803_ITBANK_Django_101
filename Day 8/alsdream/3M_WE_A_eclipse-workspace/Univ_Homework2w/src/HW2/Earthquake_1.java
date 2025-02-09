package HW2;
import java.util.Random;
public class Earthquake_1 {

	public static void main(String[] args) {
		Random ran = new Random();
		int E1 = ran.nextInt(9)+1;
		
		System.out.println("지진 강도 : "+E1);
		
		if(E1<3) {
			System.out.println("지진계에 의해서만 탐지가 가능하며 대부분의 사람이 진동을 느끼지 못함");
		}
		else if(E1<4) {
			System.out.println("인간은 자주 느끼지만 피해는 입히지 않음");
		}
		else if(E1<5) {
			System.out.println("방 안의 물건들이 흔들리는 것을 뚜렷이 관찰할 수 있지만 심각한 피해는 입히지 않음");
		}
		else if(E1<6) {
			System.out.println("좁은 면적에 걸쳐 부실하게 지어진 건물에 심한 손상");
		}
		else if(E1<7) {
			System.out.println("최대 160km에 걸쳐 건물들을 파괴하며, 1년에 약 120건 발생");
		}
		else if(E1<8) {
			System.out.println("넓은 지역에 걸쳐 심한 피해를 입히면, 1년에 약 18건 정도 발생");
		}
		else if(E1<9) {
			System.out.println("수백km 지역에 걸쳐 심한 피해를 입히며, 1년에 1건 정도 발생");
		}
		else {
			System.out.println("수천km 지역을 완전히 파괴하는데, 약 20년에 1건 꼴로 발생");
		}
	}

}
