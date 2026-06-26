package dao;

import db.Database;
import models.User;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class UserDao {
    public User findById(int id) throws SQLException {
        String sql = "SELECT * FROM users WHERE id = ?";

        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setInt(1, id);

            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return mapUser(resultSet);
                }
            }
        }

        return null;
    }

    public User findByUsername(String username) throws SQLException {
        String sql = "SELECT * FROM users WHERE username = ?";

        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, username);

            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return mapUser(resultSet);
                }
            }
        }

        return null;
    }

    public List<User> findAll() throws SQLException {
        String sql = "SELECT * FROM users";
        List<User> users = new ArrayList<>();

        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql);
             ResultSet resultSet = statement.executeQuery()) {
            while (resultSet.next()) {
                users.add(mapUser(resultSet));
            }
        }

        return users;
    }

    public boolean validateManagerLogin(String username, String password) throws SQLException {
        String sql = """
            SELECT 1
            FROM users
            WHERE username = ?
              AND password = ?
              AND role = 'Manager'
            """;

        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, username);
            statement.setString(2, password);

            try (ResultSet resultSet = statement.executeQuery()) {
                return resultSet.next();
            }
        }
    }

    private User mapUser(ResultSet resultSet) throws SQLException {
        return new User(
            resultSet.getInt("id"),
            resultSet.getString("username"),
            resultSet.getString("password"),
            resultSet.getString("role")
        );
    }
}
