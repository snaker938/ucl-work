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
import java.util.List;


@WebServlet("/viewData.html")
public class DataViewServlet extends HttpServlet
{

  public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException
  {
    // Get the data from the model
    Model model = ModelFactory.getModel();



    // Invoke the getAllPatientData method in the model and get the data
    List<String[]> patientData = model.getAllPatientData();
    request.setAttribute("patientData", patientData);


    // Invoke the getPatientNamesFormatted method in the model and get the data
    String[] patientNamesFormatted = model.getPatientNamesFormatted();
    request.setAttribute("patientNamesFormatted", patientNamesFormatted);





    // Invoke the getAllPatientNames method in the model and get the data
    // String[] patientNames = model.getAllPatientNames();

    // Then add the data to the request object that will be sent to the Java Server Page, so that
    // the JSP can access the data (a Java data structure).
    // request.setAttribute("patientNames", patientNames);

    
    // Get the a Sring array of in the formm String[] of the patient states. Loopp through all the states and put the array into the format: "patientState:frequency"
    // String[] patientStates = model.getAllPatientStates();
    // String[] patientStatesFormatted = new String[47];
    // // for (int i = 0; i < patientStates.length; i++) {
    // //   patientStatesFormatted[i] = patientStates[i] + ":" + model.getPatientStateFrequency(patientStates[i]);
    // // }
    // patientStatesFormatted[0] = "Alabama:5000";
    // patientStatesFormatted[1] = "Alaska:3000";
    // patientStatesFormatted[2] = "Arizona:7000";
    // patientStatesFormatted[3] = "Arkansas:2000";
    // patientStatesFormatted[4] = "California:8000";
    // patientStatesFormatted[5] = "Colorado:4000";
    // patientStatesFormatted[6] = "Connecticut:6000";
    // patientStatesFormatted[7] = "Delaware:1000";
    // patientStatesFormatted[8] = "Florida:9000";
    // patientStatesFormatted[9] = "Georgia:10000";
    // patientStatesFormatted[10] = "Hawaii:0";
    // patientStatesFormatted[11] = "Idaho:11000";
    // patientStatesFormatted[12] = "Illinois:12000";
    // patientStatesFormatted[13] = "Indiana:13000";
    // patientStatesFormatted[14] = "Iowa:14000";
    // patientStatesFormatted[15] = "Kansas:15000";
    // patientStatesFormatted[16] = "Kentucky:16000";
    // patientStatesFormatted[17] = "Louisiana:17000";
    // patientStatesFormatted[18] = "Maine:18000";
    // patientStatesFormatted[19] = "Maryland:19000";
    // patientStatesFormatted[20] = "Massachusetts:20000";
    // patientStatesFormatted[21] = "Michigan:21000";
    // patientStatesFormatted[22] = "Minnesota:22000";
    // patientStatesFormatted[23] = "Mississippi:23000";
    // patientStatesFormatted[24] = "Missouri:24000";
    // patientStatesFormatted[25] = "Montana:25000";
    // patientStatesFormatted[26] = "Nebraska:26000";
    // patientStatesFormatted[27] = "Nevada:27000";
    // patientStatesFormatted[28] = "New Hampshire:28000";
    // patientStatesFormatted[29] = "New Jersey:29000";
    // patientStatesFormatted[30] = "New Mexico:30000";
    // patientStatesFormatted[31] = "New York:31000";
    // patientStatesFormatted[32] = "North Carolina:32000";
    // patientStatesFormatted[33] = "North Dakota:33000";
    // patientStatesFormatted[34] = "Ohio:34000";
    // patientStatesFormatted[35] = "Oklahoma:35000";
    // patientStatesFormatted[36] = "Oregon:36000";
    // patientStatesFormatted[37] = "Pennsylvania:37000";
    // patientStatesFormatted[38] = "Rhode Island:38000";
    // patientStatesFormatted[39] = "South Carolina:39000"; 
    // patientStatesFormatted[40] = "South Dakota:40000";
    // patientStatesFormatted[41] = "Tennessee:41000";
    // patientStatesFormatted[42] = "Texas:42000";
    // patientStatesFormatted[43] = "Utah:43000";
    // patientStatesFormatted[44] = "Vermont:44000";
    // patientStatesFormatted[45] = "Virginia:45000";
    // patientStatesFormatted[46] = "Washington:46000";


    
    // request.setAttribute("patientStates", patientStatesFormatted);


    // Invoke the JSP.
    // A JSP page is actually converted into a Java class, so behind the scenes everything is Java.
    ServletContext context = getServletContext();
    RequestDispatcher dispatch = context.getRequestDispatcher("/viewData.jsp");
    dispatch.forward(request, response);
  }
}


