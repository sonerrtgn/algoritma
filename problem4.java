package project_euler;

public class problem4 {
	public static void main(String[] args) {
		System.out.print(max_palindrom());
	}
	
	
	public static int palindrom(int x) {
		int koruma = x;
		int bssayi = 0;
		while(koruma > 0) {
			koruma = (int) koruma/10;
			bssayi++;
		}
		int[] basamaklar = new int[bssayi];
		int count = 0;

		while(count < bssayi) {
			basamaklar[count]  = x - ((int)x/10)*10;
			x =(int)x/10;
			count++;
		}
		count = 0;
		int uzunluk = bssayi/2;
		while(count < uzunluk) {
			if(basamaklar[count] != basamaklar[bssayi-1-count]) {
				return 0;
			}
			count++;
		}
		return 1;
	}
	public static int max_palindrom() {
		int a = 100;
		int b = 100;
		int max =0;
		while(b != 1000) {
			while(a<1000) {
				int carpim = a*b;
				if(palindrom(carpim) == 1) {
					if(max < carpim) {
						max =carpim;
					}
				}
				a++;
			}
			a=100;
			b=b+1;
		}
		return max;
	}
}
