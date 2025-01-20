/*
 Filename: CatFactNinjaData.java
 Author: Mikhail Zubko
 Created: 2024/12/08
 Purpose: 
*/

public class CatFactNinjaData {
  private String fact;
  private long length;

  public String getFact() {
    return fact;
  }

  public void setFact(String value) {
    this.fact = value;
  }

  public long getLength() {
    return length;
  }

  public void setLength(long value) {
    this.length = value;
  }

  @Override
  public String toString() {
    String output;
    output = String.format("\nCat Fact: %s \n", this.fact);
    return output;
  }
}
