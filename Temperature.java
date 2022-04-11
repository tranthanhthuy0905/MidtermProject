import java.util.*; 
class Temperature{

   // attribute
   private double farenheit;
    
   Temperature(){
      farenheit = 32.0;
   }
         
   Temperature(double f){
      farenheit = f;
   } 
    
   /*Temperature(double t, String d){
      switch(d.charAt(0)):
         case 'C': case 'c':
            
      farenheit = f;
   } 
*/

   public String toString (){
      return("Temperature: " + farenheit +"F, " + getCelsius() +"C, " + getKelvin() + "K");
   }
  
   private double calc_f2c(double f){
   // this is a private function that uses f to calc celsius
      double celsius = (f-32.0)*5.0/9;
      return(celsius); 
   }
   
   private double calc_f2k(double f){
      // this is a private function that uses f to calc kelvin
      double kelvin =  calc_f2c(f)+273.0;
      return(kelvin); 
   }
   
   double getFarenheit(){
      return(farenheit);}
   
   double getCelsius(){
      double c = calc_f2c(farenheit); 
      return (c);}
   
   double getKelvin(){
      double k = calc_f2k(farenheit);
      return(k ); } 


}// Temperature class


/**************** cheating and putting in same file *******************/
/** remember to get the import java util line if you break this into 2 files */ 


class TempTestDriver{
   public static void main(String argv[]){
      Scanner keyb = new Scanner (System.in);
      
      System.out.println("What is the temp in Farenheit?");
      double ftemp = keyb.nextDouble(); 
      Temperature t1 = new Temperature(ftemp);
     
      System.out.println("that's " + t1.getKelvin() + " K"); 
   
   }
}