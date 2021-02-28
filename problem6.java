package project_euler;

public class problem6 {
	public static void main(String[] args) {
		System.out.print(toplam_kare()-kare_toplam());
	}
	
	public static int toplam_kare() {
		int sonuc =  0;
		int count =1 ;
		while(count < 101) {
			sonuc = sonuc+count;
			count++;
		}
		
		return sonuc*sonuc;
	}
	public static int kare_toplam() {
		int sonuc =  0;
		int count =1 ;
		while(count < 101) {
			sonuc = sonuc+count*count;
			count++;
		}
		
		return sonuc;
	
	}
}
