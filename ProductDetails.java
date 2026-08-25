public class ProductDetails {
    public static void main(String[] args) {

        
        String ProductName ="iPhone";
double Price=79999.5;
int Quantity =2;
 boolean In=true;
double Discount = 10.5;
double D=((Price*Quantity)*Discount/100);
double F=((Price*Quantity)-D);




System.out.println("Product Name:"+ProductName);
System.out.println("Price Per Product:"+Price);
System.out.println("Quantity:"+Quantity);
System.out.println("Total Amount:"+Price*Quantity);
System.out.println("Discount:"+Discount);
System.out.println("Discount Amount:"+D);
System.out.println("Final Bill:"+F);
System.out.println("Discount feature completed");
    }
}





