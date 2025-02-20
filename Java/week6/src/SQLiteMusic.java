/*
 Filename: SQLiteMusic.java
 Author: Mikhail Zubko
 Created: 2025/02/20
 Purpose: create and connect to SQLite DB
*/

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class SQLiteMusic {
  public static void main(String[] args) {
    try {
      String url = "jdbc:sqlite:./db/music.db";
      // create the connection to the DB (will be created if does not exists)
      Connection conn = DriverManager.getConnection(url);
      System.out.println("Databese connected");
      Statement statement = conn.createStatement(); // cursor
      String SQL = "DROP TABLE IF EXISTS track"; // try to drop the table for testing
      statement.execute(SQL);
      SQL = """
          CREATE TABLE IF NOT EXISTS track (
          track_id INTEGER PRIMARY KEY,
          track_name TEXT,
          track_time REAL
          )
          """;
      statement.execute(SQL);
      System.out.println("Table created.");
      String SQLInsert = """
          INSERT INTO track (track_id, track_name, track_time)
          VALUES(?,?,?)
          """;
      PreparedStatement ps = conn.prepareStatement(SQLInsert);
      // PreparedStatement is better for security
      ps.setInt(1, 0);
      ps.setString(2, "Stairway to Heaven");
      ps.setDouble(3, 5.25);
      ps.executeUpdate();
      ps.setInt(1, 1);
      ps.setString(2, "Old Time Rock and Roll");
      ps.setDouble(3, 3.25);
      ps.executeUpdate();
      ps.setInt(1, 2);
      ps.setString(2, "Bailando");
      ps.setDouble(3, 4.25);
      ps.executeUpdate();
      ps.setInt(1, 3);
      ps.setString(2, "Ramblin' Man");
      ps.setDouble(3, 2.35);
      ps.executeUpdate();
      System.out.println("Records created.");
      String SELECT = "SELECT * FROM track";
      statement.execute(SELECT);
      ResultSet results = statement.getResultSet();
      while (results.next()) {
        System.out.println(
            results.getInt("track_id") + " " +
                results.getString("track_name") + " " +
                results.getDouble("track_time"));
      }
      String UPDATE = "UPDATE track SET track_name='Bad Moon Rising' WHERE track_id=3";
      statement.execute(UPDATE);
      System.out.println("Records updated.");
      String DELETE = "DELETE FROM track WHERE track_id=2";
      statement.execute(DELETE);
      System.out.println("Records deleted.");
      statement.execute(SELECT);
      results = statement.getResultSet();
      while (results.next()) {
        System.out.println(
            results.getInt("track_id") + " " +
                results.getString("track_name") + " " +
                results.getDouble("track_time"));
      }
      // close db resources
      results.close();
      statement.close();
      ps.close();
      conn.close();
    } catch (SQLException e) {
      System.out.println("Something went wrong: " + e.getMessage());
      e.printStackTrace();
    }
  }
}
