
package uk.ac.ucl.servlets;

import uk.ac.ucl.model.Model;
import uk.ac.ucl.model.ModelFactory;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;


import java.io.PrintWriter;

@WebServlet("/saveToJson")
public class SaveToJsonServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        ModelFactory.reloadData(); // Ensure the latest data is loaded

        // Get the data from the model
        Model model = ModelFactory.getModel();
        String jsonData = model.getAllPatientDataJson();

        response.setContentType("application/json");
        response.setHeader("Content-Disposition","attachment;filename=patientData.json");
        
        try (PrintWriter out = response.getWriter()) {
            out.print(jsonData);
            out.flush();
        }
    }
}
