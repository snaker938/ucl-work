package uk.ac.ucl.model;

import java.io.IOException;
import java.util.List;

public class Model {
    private DataFrame dataFrame;

    public Model() {
        this.dataFrame = new DataFrame();
    }

    public void reloadData() throws IOException {
        loadData(); // Simply re-call loadData to refresh data from the file
    }

    public void loadData() throws IOException {
        DataLoader dataLoader = new DataLoader();
        this.dataFrame = dataLoader.loadDataFromFile();
    }

    // Function to find all patients by a search category and query
    public List<String[]> searchPatients(String searchCategory, String searchQuery) {
        return dataFrame.searchPatients(searchCategory, searchQuery);
    }

    // Function to check if an ID exists in the data
    public boolean checkIfPatientExists(String patientID) {
        return dataFrame.checkIDExists(patientID);
    }

    // Function to get all the patient data into an array in the form {ID,BIRTHDATE,DEATHDATE,SSN,DRIVERS,PASSPORT,PREFIX,FIRST,LAST,SUFFIX,MAIDEN,MARITAL,RACE,ETHNICITY,GENDER,BIRTHPLACE,ADDRESS,CITY,STATE,ZIP}, where each element is a string array.
    public List<String[]> getAllPatientData() {
        return dataFrame.getData();
    }

    // Function to get patient data by ID
    public String[] getPatientData(String patientID) {
        return dataFrame.getPatientData(patientID);
    }


    // Method to get column names
    public List<String> getColumnNames() {
        return dataFrame.getColumnNames();
    }
}
