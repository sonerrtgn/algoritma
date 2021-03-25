package project_euler;

public class problem5 {
	public static void main(String[] args) {
		System.out.print(yirmiyede_bolunen());
	}
	public static int yirmiyede_bolunen() {
		int count = 20;
		int ilk_bolunen_sayi = 0;
		int bolundumu = 0;
		while(ilk_bolunen_sayi == 0) {
			int bolenler = 2;
			while(bolenler < 21) {
				if(count % bolenler !=0) {
					bolundumu = 1;
				}
				bolenler++;
			}
			if(bolundumu == 0) {
				return count;
			}
			bolundumu = 0;
			count++;
		}
		return 1;
	}

}
