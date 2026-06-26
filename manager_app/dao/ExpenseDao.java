package dao;

import db.Database;
import models.Expense;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ExpenseDao {
    public Expense findById(int id) throws SQLException {
        String sql = "SELECT * FROM expenses WHERE id = ?";

        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setInt(1, id);

            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    return mapExpense(resultSet);
                }
            }
        }

        return null;
    }

    public List<Expense> findAll() throws SQLException {
        String sql = "SELECT * FROM expenses";
        List<Expense> expenses = new ArrayList<>();

        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql);
             ResultSet resultSet = statement.executeQuery()) {
            while (resultSet.next()) {
                expenses.add(mapExpense(resultSet));
            }
        }

        return expenses;
    }

    public List<Expense> findByUserId(int userId) throws SQLException {
        String sql = "SELECT * FROM expenses WHERE user_id = ?";
        List<Expense> expenses = new ArrayList<>();

        try (Connection connection = Database.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setInt(1, userId);

            try (ResultSet resultSet = statement.executeQuery()) {
                while (resultSet.next()) {
                    expenses.add(mapExpense(resultSet));
                }
            }
        }

        return expenses;
    }

    private Expense mapExpense(ResultSet resultSet) throws SQLException {
        return new Expense(
            resultSet.getInt("id"),
            resultSet.getInt("user_id"),
            resultSet.getFloat("amount"),
            resultSet.getString("description"),
            resultSet.getString("date")
        );
    }
}
