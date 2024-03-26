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

    // Function to get all the patient data into an array in the form {ID,BIRTHDATE,DEATHDATE,SSN,DRIVERS,PASSPORT,PREFIX,FIRST,LAST,SUFFIX,MAIDEN,MARITAL,RACE,ETHNICITY,GENDER,BIRTHPLACE,ADDRESS,CITY,STATE,ZIP}, where each element is a string array.
    public List<String[]> getAllPatientData() {
        return dataFrame.getData();
    }

    // function to get all the patient names in the format "firstName lastName" with any numbers omitted
    // public List<String> getPatientNamesFormatted() {
    //     return dataFrame.getPatientNamesFormatted();
    // }


    public String[] getPatientNamesFormatted() {
        String[] fullNames = new String[dataFrame.getRowCount()];
      
        for (int i = 0; i < dataFrame.getRowCount(); i++) {
          String firstName = dataFrame.getValue("FIRST", i);
          String lastName = dataFrame.getValue("LAST", i);
      
          // Remove any numbers from the end of the names
          firstName = firstName != null ? removeTrailingNumbers(firstName) : "";
          lastName = lastName != null ? removeTrailingNumbers(lastName) : "";
      
          fullNames[i] = firstName + " " + lastName;
        }
      
        return fullNames;
      }
      
      private String removeTrailingNumbers(String name) {
        // Use a regular expression to remove numbers from the end
        return name.replaceAll("\\d+$", "");
      }
      

    // // Create a function getPaitentStateFrequency to get the frequency of each patient state
    // public int getPatientStateFrequency(String state) {
    //     int count = 0;
    //     for (int i = 0; i < dataFrame.getRowCount(); i++) {
    //         if (dataFrame.getValue("STATE", i).equals(state)) {
    //             count++;
    //         }
    //     }
    //     return count;
    // }

    // // Create a function to get all the patient states
    // public String[] getAllPatientStates() {
    //     String[] patientStates = new String[dataFrame.getRowCount()];
    //     for (int i = 0; i < dataFrame.getRowCount(); i++) {
    //         patientStates[i] = dataFrame.getValue("STATE", i);
    //     }
    //     return patientStates;
    // }

    // Method to get column names
    public List<String> getColumnNames() {
        return dataFrame.getColumnNames();
    }
}
