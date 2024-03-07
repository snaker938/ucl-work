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


@WebServlet("/viewData.html")
public class DataViewServlet extends HttpServlet
{

  public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException
  {
    // Get the data from the model
    // Model model = ModelFactory.getModel();

    // Invoke the getAllPatientNames method in the model and get the data
    // String[] patientNames = model.getAllPatientNames();

    // Then add the data to the request object that will be sent to the Java Server Page, so that
    // the JSP can access the data (a Java data structure).
    // request.setAttribute("patientNames", patientNames);

    
    // Get the a Sring array of in the formm String[] of the patient states. Loopp through all the states and put the array into the format: "patientState:frequency"
    // String[] patientStates = model.getAllPatientStates();
    String[] patientStatesFormatted = new String[2];
    // for (int i = 0; i < patientStates.length; i++) {
    //   patientStatesFormatted[i] = patientStates[i] + ":" + model.getPatientStateFrequency(patientStates[i]);
    // }
    patientStatesFormatted[0] = "Alabama:5";
    patientStatesFormatted[1] = "Alaska:3";
    request.setAttribute("patientStates", patientStatesFormatted);


    // Invoke the JSP.
    // A JSP page is actually converted into a Java class, so behind the scenes everything is Java.
    ServletContext context = getServletContext();
    RequestDispatcher dispatch = context.getRequestDispatcher("/viewData.jsp");
    dispatch.forward(request, response);
  }
}


