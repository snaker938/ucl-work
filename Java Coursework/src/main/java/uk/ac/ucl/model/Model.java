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

    // Method to get column names
    public List<String> getColumnNames() {
        return dataFrame.getColumnNames();
    }
}
