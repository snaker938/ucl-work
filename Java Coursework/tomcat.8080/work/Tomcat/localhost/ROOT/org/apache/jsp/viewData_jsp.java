/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/9.0.45
 * Generated at: 2024-03-27 15:41:00 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.util.List;

public final class viewData_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("javax.servlet");
    _jspx_imports_packages.add("javax.servlet.http");
    _jspx_imports_packages.add("javax.servlet.jsp");
    _jspx_imports_classes = new java.util.HashSet<>();
    _jspx_imports_classes.add("java.util.List");
  }

  private volatile javax.el.ExpressionFactory _el_expressionfactory;
  private volatile org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public java.util.Set<java.lang.String> getPackageImports() {
    return _jspx_imports_packages;
  }

  public java.util.Set<java.lang.String> getClassImports() {
    return _jspx_imports_classes;
  }

  public javax.el.ExpressionFactory _jsp_getExpressionFactory() {
    if (_el_expressionfactory == null) {
      synchronized (this) {
        if (_el_expressionfactory == null) {
          _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        }
      }
    }
    return _el_expressionfactory;
  }

  public org.apache.tomcat.InstanceManager _jsp_getInstanceManager() {
    if (_jsp_instancemanager == null) {
      synchronized (this) {
        if (_jsp_instancemanager == null) {
          _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
        }
      }
    }
    return _jsp_instancemanager;
  }

  public void _jspInit() {
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

    if (!javax.servlet.DispatcherType.ERROR.equals(request.getDispatcherType())) {
      final java.lang.String _jspx_method = request.getMethod();
      if ("OPTIONS".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        return;
      }
      if (!"GET".equals(_jspx_method) && !"POST".equals(_jspx_method) && !"HEAD".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "JSPs only permit GET, POST or HEAD. Jasper also permits OPTIONS");
        return;
      }
    }

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("<head>\n");
      out.write("    <meta charset=\"UTF-8\">\n");
      out.write("    <title>Patient Data App</title>\n");
      out.write("    <link rel=\"stylesheet\" href=\"viewData.css\">\n");
      out.write("\n");
      out.write("    <script>\n");
      out.write("    window.addEventListener('DOMContentLoaded', (event) => {\n");
      out.write("        const tableRows = document.querySelectorAll('.main table tr:not(:first-child)'); // Exclude header row\n");
      out.write("        tableRows.forEach(row => {\n");
      out.write("            row.addEventListener('click', function() {\n");
      out.write("                // Directly use the textContent since it's already a string\n");
      out.write("                const patientID = this.cells[0].textContent.trim(); // Added trim() to remove any potential whitespace\n");
      out.write("\n");
      out.write("                const url = \"/editPatient/\" + patientID\n");
      out.write("\n");
      out.write("                window.location.href = url;\n");
      out.write("            });\n");
      out.write("        });\n");
      out.write("    });\n");
      out.write("    </script>\n");
      out.write("\n");
      out.write("\n");
      out.write("</head>\n");
      out.write("\n");
      out.write("<body>\n");
      out.write("\n");
      out.write("    <div class=\"navbar\">\n");
      out.write("        <a href=\"index.html\">Home</a>\n");
      out.write("    </div>\n");
      out.write("\n");
      out.write("    <div class=\"main\">\n");
      out.write("\n");
      out.write("    <p style=\"font-size: 20px; text-align: left; margin-bottom: 20px;\">To modify a patient's details, or remove them, click on them.</p>\n");
      out.write("    <p style=\"font-size: 20px; text-align: left; margin-bottom: 20px;\">\n");
      out.write("        To add a new patient, click here:\n");
      out.write("        <button onclick=\"window.location.href='/addPatient.html';\" class=\"addButton\">Add New Patient</button>\n");
      out.write("    </p>\n");
      out.write("    <div style=\"font-size: 20px; text-align: left; margin-bottom: 20px; display: flex; align-items: center;\">\n");
      out.write("        <span style=\"margin-right: 10px;\">To save the patient data to a JSON file, click here:</span>\n");
      out.write("        <form action=\"");
      out.write((java.lang.String) org.apache.jasper.runtime.PageContextImpl.proprietaryEvaluate("${pageContext.request.contextPath}", java.lang.String.class, (javax.servlet.jsp.PageContext)_jspx_page_context, null));
      out.write("/saveToJson\" method=\"post\" style=\"margin: 0;\">\n");
      out.write("            <input type=\"submit\" value=\"Save to JSON\" style=\"background-color: #d17a61; border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer;\"/>\n");
      out.write("        </form>\n");
      out.write("    </div>\n");
      out.write("    \n");
      out.write("    \n");
      out.write("    \n");
      out.write("    <p style=\"font-size: 20px; text-align: left; margin-bottom: 20px;\">\n");
      out.write("        Search for specific patient:\n");
      out.write("        <form action=\"/searchPatient\" method=\"get\" style=\"display: inline;\">\n");
      out.write("            <input type=\"text\" name=\"searchQuery\" placeholder=\"Enter search term\" class=\"search-input\">\n");
      out.write("            <select name=\"searchCategory\" class=\"search-select\">\n");
      out.write("                <option value=\"ID\">ID</option>\n");
      out.write("                <option value=\"Birthdate\">Birthdate</option>\n");
      out.write("                <option value=\"Deathdate\">Deathdate</option>\n");
      out.write("                <option value=\"SSN\">SSN</option>\n");
      out.write("                <option value=\"Drivers\">Drivers</option>\n");
      out.write("                <option value=\"Passport\">Passport</option>\n");
      out.write("                <option value=\"Prefix\">Prefix</option>\n");
      out.write("                <option value=\"First\">First</option>\n");
      out.write("                <option value=\"Last\">Last</option>\n");
      out.write("                <option value=\"Suffix\">Suffix</option>\n");
      out.write("                <option value=\"Maiden\">Maiden</option>\n");
      out.write("                <option value=\"Marital\">Marital</option>\n");
      out.write("                <option value=\"Race\">Race</option>\n");
      out.write("                <option value=\"Ethnicity\">Ethnicity</option>\n");
      out.write("                <option value=\"Gender\">Gender</option>\n");
      out.write("                <option value=\"Birthplace\">Birthplace</option>\n");
      out.write("                <option value=\"Address\">Address</option>\n");
      out.write("                <option value=\"City\">City</option>\n");
      out.write("                <option value=\"State\">State</option>\n");
      out.write("                <option value=\"ZIP\">ZIP</option>\n");
      out.write("            </select>\n");
      out.write("            <input type=\"submit\" value=\"Search\" class=\"search-button\">\n");
      out.write("        </form>\n");
      out.write("    </p>\n");
      out.write("\n");
      out.write("    <table>\n");
      out.write("        <tr>\n");
      out.write("            <th>ID</th>\n");
      out.write("            <th>Birthdate</th>\n");
      out.write("            <th>Deathdate</th>\n");
      out.write("            <th>SSN</th>\n");
      out.write("            <th>Drivers</th>\n");
      out.write("            <th>Passport</th>\n");
      out.write("            <th>Prefix</th>\n");
      out.write("            <th>First</th>\n");
      out.write("            <th>Last</th>\n");
      out.write("            <th>Suffix</th>\n");
      out.write("            <th>Maiden</th>\n");
      out.write("            <th>Marital</th>\n");
      out.write("            <th>Race</th>\n");
      out.write("            <th>Ethnicity</th>\n");
      out.write("            <th>Gender</th>\n");
      out.write("            <th>Birthplace</th>\n");
      out.write("            <th>Address</th>\n");
      out.write("            <th>City</th>\n");
      out.write("            <th>State</th>\n");
      out.write("            <th>ZIP</th>\n");
      out.write("        </tr>\n");
      out.write("        ");

            List<String[]> patientData = (List<String[]>) request.getAttribute("patientData");
            for (String[] patient : patientData) {
                
      out.write("<tr>");

                for (int i = 0; i < patient.length; i++) {
                    
      out.write("<td>");
      out.print( patient[i].isEmpty() ? " " : patient[i] );
      out.write("</td>");

                }
                
      out.write("</tr>");

            }
        
      out.write("\n");
      out.write("    </table>\n");
      out.write("    </div>\n");
      out.write("</body>\n");
      out.write("</html>\n");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try {
            if (response.isCommitted()) {
              out.flush();
            } else {
              out.clearBuffer();
            }
          } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
