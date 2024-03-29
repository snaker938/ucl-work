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
        return columns.get(0).getSize();
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
                rowData[colIndex] = (value != null) ? value : ""; // Replace null values with a blank space
            }
            allData.add(rowData);
        }
        
        return allData;
    }

    // Function to get patient data by ID
    public String[] getPatientData(String patientID) {
        int numRows = getRowCount();
        // Define the expected columns in order
        String[] expectedColumns = {"ID", "BIRTHDATE", "DEATHDATE", "SSN", "DRIVERS", "PASSPORT", "PREFIX", "FIRST", "LAST", "SUFFIX", "MAIDEN", "MARITAL", "RACE", "ETHNICITY", "GENDER", "BIRTHPLACE", "ADDRESS", "CITY", "STATE", "ZIP"};
        String[] patientData = new String[expectedColumns.length];
    
        for (int rowIndex = 0; rowIndex < numRows; rowIndex++) {
            // Check if the current row's ID matches the patientID we are looking for
            if (getValue("ID", rowIndex).equals(patientID)) {
                // Found the patient, now fetch their data
                for (int colIndex = 0; colIndex < expectedColumns.length; colIndex++) {
                    String columnName = expectedColumns[colIndex];
                    String value = getValue(columnName, rowIndex);
                    patientData[colIndex] = value != null ? value : ""; // Replace null with a blank space for consistency
                }
                break; // Break the loop once the patient data is found
            }
        }
    
        return patientData;
    }

    // Function to check if an ID exists in the data
    public boolean checkIDExists(String patientID) {
        int numRows = getRowCount();
        for (int rowIndex = 0; rowIndex < numRows; rowIndex++) {
            if (getValue("ID", rowIndex).equals(patientID)) {
                return true;
            }
        }
        return false;
    }

    // Function to find all patients by a search category and query
    public List<String[]> searchPatients(String searchCategory, String searchQuery) {
        List<String[]> searchResults = new ArrayList<>();
        int numRows = getRowCount();

        
        // Normalize the search query to lower case for case-insensitive comparison
        String normalizedSearchQuery = searchQuery.toLowerCase();
        String normalizedSearchCategory = searchCategory.toUpperCase();
        
        for (int rowIndex = 0; rowIndex < numRows; rowIndex++) {
            String value = getValue(normalizedSearchCategory, rowIndex);
            if (value != null && value.toLowerCase().contains(normalizedSearchQuery)) {
                // If the value contains the search query, add the row to the results
                String[] rowData = new String[columns.size()];
                for (int colIndex = 0; colIndex < columns.size(); colIndex++) {
                    rowData[colIndex] = getValue(columns.get(colIndex).getName(), rowIndex);
                }
                searchResults.add(rowData);
            }
        }
        return searchResults;
    }
}
