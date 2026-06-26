package db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Database {
    private static final String DB_NAME = "expenses_system_db.db";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection("jdbc:sqlite:" + getDatabasePath());
    }

    private static String getDatabasePath() {
        Path currentDirectoryPath = Paths.get(DB_NAME);
        if (Files.exists(currentDirectoryPath)) {
            return currentDirectoryPath.toString();
        }

        Path parentDirectoryPath = Paths.get("..", DB_NAME);
        if (Files.exists(parentDirectoryPath)) {
            return parentDirectoryPath.toString();
        }

        return currentDirectoryPath.toString();
    }
}
