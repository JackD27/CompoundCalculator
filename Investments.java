import java.text.NumberFormat;

public class Investments {
	static NumberFormat nf=NumberFormat.getCurrencyInstance();
	public static double investment(double value) {
		
		double value2 = value * 1.04;
		System.out.printf(nf.format(value2 - value));
		System.out.print("     ");
		return value2;
	}



	
	public static void main(String[] args) {
		double value = 2812;
		
		for (int i = 0; i < 245; i++) {
			  System.out.printf("%s%d   ", "Day: ", i + 1);
			  value = investment(value);		 
			  System.out.printf(nf.format(value));
			  System.out.println();
			}
	}

}
