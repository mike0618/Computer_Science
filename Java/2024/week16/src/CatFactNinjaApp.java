/*
 Filename: CatFactNinjaApp.java
 Author: Mikhail Zubko
 Created: 2024/12/08
 Purpose: Get Cat Facts from API endpoint
*/

import java.util.Scanner;
// Handle any Input Output exceptions
import java.io.IOException;
// Create a URL object
import java.net.URI;
import java.net.URL;
// Import Jackson JSON libs
import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class CatFactNinjaApp {
  private static Scanner keyboard = new Scanner(System.in);
  // API endpoint URL
  private final static String API = "https://catfact.ninja/fact";
  // Create CatData object
  private static CatFactNinjaData fact;
  private static String menu = "y";

  public static void main(String[] args) {
    while (!menu.equals("n")) {
      getData();
      // Display a Fact at the console
      System.out.println(fact.toString());
      System.out.print("Another Cat Fact? (y, n): ");
      menu = keyboard.nextLine();
    }
    System.out.println("Thanks for using Cat Fact Ninja!");
  }

  // Get data from the API endpoint
  public static void getData() {
    try {
      URI uri = new URI(API);// create URI obj
      URL url = uri.toURL();// create URI obj from URI
      // create Jackson JSON obj to read the raw JSON data into POJO
      ObjectMapper objectMapper = new ObjectMapper();
      // read JSON into CatData Object
      fact = objectMapper.readValue(url, CatFactNinjaData.class);
    } catch (JsonGenerationException | JsonMappingException e) {
      // JSON Exception handling
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
