package uk.ac.ucl.servlets;

import uk.ac.ucl.model.Model;
import uk.ac.ucl.model.ModelFactory;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
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

@WebServlet("/deletePatient/*")
public class DeletePatientServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        ModelFactory.reloadData(); // Ensure the latest data is loaded

        // Extract patientID from the URL
        String pathInfo = request.getPathInfo(); // This should be "/{patientID}"
        String patientID = pathInfo.substring(1); // Remove the leading '/'


        String baseDir = "data";
        File directory = new File(baseDir);
        if (!directory.exists()) directory.mkdirs();
        String newFileName = generateFileName(baseDir);


        // Save the data to a new file
        saveData(patientID, baseDir + File.separator + newFileName);

        // Get the data from the model
        Model model = ModelFactory.getModel();

        model.reloadData();


        // Invoke the getAllPatientData method in the model and get the data
        List<String[]> patientData = model.getAllPatientData();
        request.setAttribute("patientData", patientData);


        // Invoke the JSP.
        // A JSP page is actually converted into a Java class, so behind the scenes everything is Java.
        ServletContext context = getServletContext();
        RequestDispatcher dispatch = context.getRequestDispatcher("/viewData.jsp");
        dispatch.forward(request, response);
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

    private void saveData(String patientDetails, String filePath) throws IOException {
        String baseDir = filePath.substring(0, filePath.lastIndexOf(File.separator));
        String latestFileName = findLatestFileName(baseDir);
        List<String> lines = Files.readAllLines(Paths.get(baseDir, latestFileName));

        Boolean patientFound = false;
    
        // Process existing data, update if patient ID matches
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);
            String[] details = line.split(",");
            if (details.length > 0 && details[0].equals(patientDetails)) { // Check if ID matches
                // Remove the line with the patient details
                lines.remove(i);

                // Flag the patient as found
                patientFound = true;

                break; // Stop searching once we've found and updated the patient
            }
        }

        // Write to a new file if the patient was found

        if (patientFound) {
            Files.write(Paths.get(filePath), lines);
        }
    }
}