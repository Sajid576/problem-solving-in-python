using System;
class HelloWorld {
  static void Main() {
      int limit=200;
    int divisor=3;
    
    int truncatedCount = limit / divisor;
    int highestMultiple = truncatedCount * divisor;
    
    for (int multiple = highestMultiple; multiple > 0; multiple -= divisor) {
         Console.WriteLine(multiple);
    }
   
  }
}