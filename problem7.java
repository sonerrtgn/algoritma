package project_euler;

public class problem7 {
	public static void main(String[] args) {
		System.out.print(prime_x(10001));
	}
	public static int prime(int x) {
		int bolen = 3;
		int kok = (int) (Math.sqrt(x));
		if(x %2 == 0) {
			return 0;
		}
		if(x == kok*kok) {
			return 0;
		}
		while(bolen < kok+1) {
			if(x%bolen == 0) {
				return 0;
			}
			bolen +=2;
		}
		return 1;
	}
	public static int prime_x(int kacinci_asal_olsun) {
		int count= 3;
		int asal_sira = 1;
		while(asal_sira < kacinci_asal_olsun) {
			if(prime(count) == 1) {
				asal_sira++;
			}
			count++;
		}

		return count-1;
	}
}
