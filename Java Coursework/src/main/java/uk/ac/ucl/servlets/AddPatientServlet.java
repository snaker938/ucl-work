package uk.ac.ucl.servlets;

import uk.ac.ucl.model.Model;
import uk.ac.ucl.model.ModelFactory;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.SecureRandom;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@WebServlet("/addPatient.html")
public class AddPatientServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        ModelFactory.reloadData(); // Ensure the latest data is loaded

        Model model = ModelFactory.getModel();
        
        String newPatientID = generateUniquePatientID(model);

        request.setAttribute("isEditingPatient", false);
        
        String[] patientDetails = new String[]{newPatientID, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""};

        request.setAttribute("patientDetails", patientDetails);
        request.getRequestDispatcher("/editPatient.jsp").forward(request, response);
    }

    private String generateUniquePatientID(Model model) {
        String id;
        SecureRandom random = new SecureRandom();
        do {
            id = IntStream.of(8, 4, 4, 4, 12)
                    .mapToObj(len -> generateRandomString(len, random))
                    .collect(Collectors.joining("-"));
        } while (model.checkIfPatientExists(id));
        return id;
    }

    private String generateRandomString(int length, SecureRandom random) {
        String characters = "0123456789abcdef"; // Use only hexadecimal characters
        return random.ints(length, 0, characters.length())
                     .mapToObj(i -> String.valueOf(characters.charAt(i)))
                     .collect(Collectors.joining());
    }
}
