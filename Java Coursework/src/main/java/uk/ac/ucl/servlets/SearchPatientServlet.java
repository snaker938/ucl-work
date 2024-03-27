package uk.ac.ucl.servlets;

import java.util.List;

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


@WebServlet("/searchPatient")
public class SearchPatientServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String searchQuery = request.getParameter("searchQuery");
        String searchCategory = request.getParameter("searchCategory");

        Model model = ModelFactory.getModel();

        // Perform the search using searchQuery and searchCategory
        List<String[]> searchResults = model.searchPatients(searchCategory, searchQuery);

        
        request.setAttribute("patientData", searchResults);


        // Invoke the JSP.
        // A JSP page is actually converted into a Java class, so behind the scenes everything is Java.
        ServletContext context = getServletContext();
        RequestDispatcher dispatch = context.getRequestDispatcher("/viewData.jsp");
        dispatch.forward(request, response);

    }
}
