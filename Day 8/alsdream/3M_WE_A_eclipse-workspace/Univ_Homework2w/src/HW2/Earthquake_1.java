package HW2;
import java.util.Random;
public class Earthquake_1 {

	public static void main(String[] args) {
		Random ran = new Random();
		int E1 = ran.nextInt(9)+1;
		
		System.out.println("���� ���� : "+E1);
		
		if(E1<3) {
			System.out.println("�����迡 ���ؼ��� Ž���� �����ϸ� ��κ��� ����� ������ ������ ����");
		}
		else if(E1<4) {
			System.out.println("�ΰ��� ���� �������� ���ش� ������ ����");
		}
		else if(E1<5) {
			System.out.println("�� ���� ���ǵ��� ��鸮�� ���� �ѷ��� ������ �� ������ �ɰ��� ���ش� ������ ����");
		}
		else if(E1<6) {
			System.out.println("���� ������ ���� �ν��ϰ� ������ �ǹ��� ���� �ջ�");
		}
		else if(E1<7) {
			System.out.println("�ִ� 160km�� ���� �ǹ����� �ı��ϸ�, 1�⿡ �� 120�� �߻�");
		}
		else if(E1<8) {
			System.out.println("���� ������ ���� ���� ���ظ� ������, 1�⿡ �� 18�� ���� �߻�");
		}
		else if(E1<9) {
			System.out.println("����km ������ ���� ���� ���ظ� ������, 1�⿡ 1�� ���� �߻�");
		}
		else {
			System.out.println("��õkm ������ ������ �ı��ϴµ�, �� 20�⿡ 1�� �÷� �߻�");
		}
	}

}
