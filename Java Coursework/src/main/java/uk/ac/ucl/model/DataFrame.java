package uk.ac.ucl.model;

import java.util.ArrayList;
import java.util.List;

public class DataFrame {
    private List<Column> columns;

    public DataFrame() {
        columns = new ArrayList<>();
    }

    public void addColumn(Column column) {
        columns.add(column);
    }

    public List<String> getColumnNames() {
        List<String> names = new ArrayList<>();
        for (Column column : columns) {
            names.add(column.getName());
        }
        return names;
    }

    public int getRowCount() {
        if (columns.isEmpty()) {
            return 0;
        }
        return columns.get(0).getSize(); // Assuming all columns have the same number of rows
    }

    public String getValue(String columnName, int row) {
        for (Column column : columns) {
            if (column.getName().equals(columnName)) {
                return column.getRowValue(row);
            }
        }
        return null;
    }

    public void putValue(String columnName, int row, String value) {
        for (Column column : columns) {
            if (column.getName().equals(columnName)) {
                column.setRowValue(row, value);
            }
        }
    }

    public void addValue(String columnName, String value) {
        for (Column column : columns) {
            if (column.getName().equals(columnName)) {
                column.addRowValue(value);
            }
        }
    }

    // // Function getData to get all the patient data into an array in the form {ID,BIRTHDATE,DEATHDATE,SSN,DRIVERS,PASSPORT,PREFIX,FIRST,LAST,SUFFIX,MAIDEN,MARITAL,RACE,ETHNICITY,GENDER,BIRTHPLACE,ADDRESS,CITY,STATE,ZIP}, where each element is a string array.
    public List<String[]> getData() {
        List<String[]> allData = new ArrayList<>();
        int numRows = getRowCount();
        
        // Define the expected columns in order
        String[] expectedColumns = {"ID", "BIRTHDATE", "DEATHDATE", "SSN", "DRIVERS", "PASSPORT", "PREFIX", "FIRST", "LAST", "SUFFIX", "MAIDEN", "MARITAL", "RACE", "ETHNICITY", "GENDER", "BIRTHPLACE", "ADDRESS", "CITY", "STATE", "ZIP"};
        
        for (int rowIndex = 0; rowIndex < numRows; rowIndex++) {
            String[] rowData = new String[expectedColumns.length];
            for (int colIndex = 0; colIndex < expectedColumns.length; colIndex++) {
                String columnName = expectedColumns[colIndex];
                String value = getValue(columnName, rowIndex);
                rowData[colIndex] = (value != null) ? value : " "; // Replace null values with a blank space
            }
            allData.add(rowData);
        }
        
        return allData;
    }
}
