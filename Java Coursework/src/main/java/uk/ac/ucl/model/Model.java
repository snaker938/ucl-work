package uk.ac.ucl.model;

import java.io.IOException;
import java.util.List;

public class Model {
    private DataFrame dataFrame;

    public Model() {
        this.dataFrame = new DataFrame();
    }

    public void loadData(String filePath) throws IOException {
        DataLoader dataLoader = new DataLoader();
        this.dataFrame = dataLoader.loadDataFromFile(filePath);
    }

    public String[] getAllPatientNames() {
        String[] fullNames = new String[dataFrame.getRowCount()];
    
        for (int i = 0; i < dataFrame.getRowCount(); i++) {
            String firstName = dataFrame.getValue("FIRST", i);
            String lastName = dataFrame.getValue("LAST", i);
            fullNames[i] = (firstName != null ? firstName : "") + " " + (lastName != null ? lastName : "");
        }
    
        return fullNames;
    }

    // Create a function getPaitentStateFrequency to get the frequency of each patient state
    public int getPatientStateFrequency(String state) {
        int count = 0;
        for (int i = 0; i < dataFrame.getRowCount(); i++) {
            if (dataFrame.getValue("STATE", i).equals(state)) {
                count++;
            }
        }
        return count;
    }

    // Create a function to get all the patient states
    public String[] getAllPatientStates() {
        String[] patientStates = new String[dataFrame.getRowCount()];
        for (int i = 0; i < dataFrame.getRowCount(); i++) {
            patientStates[i] = dataFrame.getValue("STATE", i);
        }
        return patientStates;
    }

    // Method to get column names
    public List<String> getColumnNames() {
        return dataFrame.getColumnNames();
    }
}
