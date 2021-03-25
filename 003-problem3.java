package project_euler;


public class problem3 {
	static long a = 600851475143L;
	public static void main(String[] args) {
			System.out.print(max_bolen(a));
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
	public static int max_bolen(long x) {
		int count = 1;
		int max_bolen = 1;
		int durak = (int) Math.sqrt(x);
		while(count <= durak) {
			if(x%count == 0) {
				if(prime(count) == 1) {
					max_bolen = count;
				}
			}
			count++;
		}
		
		return max_bolen;
	}
}
