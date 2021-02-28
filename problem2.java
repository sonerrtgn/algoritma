package project_euler;

public class problem2 {
	
	public static void main(String[] args) {
		System.out.print(fibbon());
	}
	
	public static int fibbon() {
		int f1 = 1;
		int f2 = 2;
		int f = f1+f2;
		int toplam =2;
		while(f < 4000000) {
			f1 = f2;
			f2=f;
			f=f1+f2;
			if(f%2 == 0 && f<=4000000) {
				toplam += f;
			}
		}
		
		
		return toplam;
	}

}
