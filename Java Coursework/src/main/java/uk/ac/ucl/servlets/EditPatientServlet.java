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
import java.io.IOException;

@WebServlet("/editPatient/*")
public class EditPatientServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {


        ModelFactory.reloadData(); // Ensure the latest data is loaded

        // Extract patientID from the URL
        String pathInfo = request.getPathInfo(); // This should be "/{patientID}"
        String patientID = pathInfo.substring(1); // Remove the leading '/'

        // Get the model
        Model model = ModelFactory.getModel();

        // Ideally, fetch the patient data by ID from your model
        String[] patientDetails = model.getPatientData(patientID);
        request.setAttribute("patientDetails", patientDetails);

        // Forward to the JSP page for editing patient details
        ServletContext context = getServletContext();
        RequestDispatcher dispatcher = context.getRequestDispatcher("/editPatient.jsp");
        dispatcher.forward(request, response);
    }
}