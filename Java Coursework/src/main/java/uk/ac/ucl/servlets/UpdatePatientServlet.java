package uk.ac.ucl.servlets;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;


@WebServlet("/updatePatient")
public class UpdatePatientServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Assuming patient details are sent as form parameters with the same names as the CSV columns
        String[] patientDetails = new String[]{
            request.getParameter("ID"),
            request.getParameter("BIRTHDATE"),
            request.getParameter("DEATHDATE"),
            request.getParameter("SSN"),
            request.getParameter("DRIVERS"),
            request.getParameter("PASSPORT"),
            request.getParameter("PREFIX"),
            request.getParameter("FIRST"),
            request.getParameter("LAST"),
            request.getParameter("SUFFIX"),
            request.getParameter("MAIDEN"),
            request.getParameter("MARITAL"),
            request.getParameter("RACE"),
            request.getParameter("ETHNICITY"),
            request.getParameter("GENDER"),
            request.getParameter("BIRTHPLACE"),
            request.getParameter("ADDRESS"),
            request.getParameter("CITY"),
            request.getParameter("STATE"),
            request.getParameter("ZIP")
        };

        String baseDir = "data"; // Note the addition of "data"
        File directory = new File(baseDir);
        if (!directory.exists()) directory.mkdirs();
        String newFileName = generateFileName(baseDir);

        // Save the data to a new file
        saveData(patientDetails, baseDir + File.separator + newFileName);

        // Redirect to a confirmation page
        response.sendRedirect("viewData.html"); // Adjust the redirect to match the correct path
    }

    private String generateFileName(String baseDir) {
        int incrementNumber = 0;
        String fileName;
        do {
            incrementNumber++;
            fileName = "data" + (incrementNumber == 1 ? "" : incrementNumber) + ".csv";
        } while (new File(baseDir, fileName).exists());
        return fileName;
    }

    private String findLatestFileName(String baseDir) {
        File dir = new File(baseDir);
        File[] files = dir.listFiles((d, name) -> name.startsWith("data") && name.endsWith(".csv"));
        if (files == null || files.length == 0) return "data.csv";

        String latestFileName = files[0].getName();
        for (File file : files) {
            if (file.getName().compareTo(latestFileName) > 0) {
                latestFileName = file.getName();
            }
        }
        return latestFileName;
    }

    private void saveData(String[] patientDetails, String filePath) throws IOException {
        String baseDir = filePath.substring(0, filePath.lastIndexOf(File.separator));
        String latestFileName = findLatestFileName(baseDir);
        List<String> lines = Files.readAllLines(Paths.get(baseDir, latestFileName));
    
        // Prepare the updated patient data as a CSV line
        String updatedPatientData = String.join(",", patientDetails);
    
        // Flag to track if the patient ID was found and updated
        boolean patientFound = false;
    
        // Process existing data, update if patient ID matches
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            String[] details = line.split(",");
            if (details.length > 0 && details[0].equals(patientDetails[0])) { // Check if ID matches
                lines.set(i, updatedPatientData); // Update the line with new patient details
                patientFound = true;
                break; // Stop searching once we've found and updated the patient
            }
        }
    
        // If patient was not found in existing data, add them
        if (!patientFound) {
            lines.add(updatedPatientData);
        }
    
        // Write to a new file
        Files.write(Paths.get(filePath), lines);
    }
    
}
