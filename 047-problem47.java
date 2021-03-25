package project_euler;

public class problem47 {
	public static void main(String[] args) {

		int count = 10;
		int bulundumu = 0;
		while(bulundumu == 0) {
			if(asal_bolen_sayisi(count) == 4) {
				if(asal_bolen_sayisi(count+1) == 4) {
					if(asal_bolen_sayisi(count+2) == 4) {
						if(asal_bolen_sayisi(count+3) == 4) {
							bulundumu =1;
							break;
						}
					}
				}
			}
			count++;
		}
		System.out.print(count);
		
	}
	public static int asal_bolen_sayisi(int x) {
		int count =3;
		int uzunluk = (int) x/2;
		int bolen_sayisi = 0;
		if(x%2 == 0) {
			bolen_sayisi=1;
		}
		while(count < uzunluk) {
			if(x%count == 0) {
				if(prime(count) == 1) {
					bolen_sayisi++;
				}
			}
			count++;
		}
		return bolen_sayisi; 
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
	
}
