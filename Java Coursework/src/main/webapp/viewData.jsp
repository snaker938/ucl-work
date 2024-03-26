<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Patient Data App</title>
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f7f7f7;
        margin: 0;
        padding: 20px;
        color: #333;
    }
    .navbar {
        background-color: #4A4A4A;
        overflow: hidden;
        top: 0;
        z-index: 1000;
    }
    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        font-size: 16px;
    }
    .navbar a:hover {
        background-color: #666;
    }
    .main {
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        padding: 20px;
        margin: 20px auto;
        width: fit-content;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }
    table, th, td {
        border: 1px solid #ddd;
    }
    th, td {
        text-align: left;
        padding: 12px 15px;
        font-size: 14px;
    }
    th {
        background-color: #585858;
        color: white;
        font-size: 16px;
    }

    .main table tr:not(:first-child):hover {
      cursor: pointer;
    }

    tr:nth-child(odd) {background-color: #f9f9f9;}
    tr:nth-child(even) {background-color: #e9e9e9;}
    tr:hover {
        background-color: #d3d3d3;
    }
    @media (max-width: 768px) {
        .main {
            margin: 10px;
            padding: 10px;
        }
        table, th, td {
            font-size: 12px;
        }
    }

    .addButton {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
</style>

<script>
  window.addEventListener('DOMContentLoaded', (event) => {
    const tableRows = document.querySelectorAll('.main table tr:not(:first-child)'); // Exclude header row
    tableRows.forEach(row => {
        row.addEventListener('click', function() {
            // Directly use the textContent since it's already a string
            const patientID = this.cells[0].textContent.trim(); // Added trim() to remove any potential whitespace

            const url = "/editPatient/" + patientID

            window.location.href = url;
        });
    });
  });
</script>


</head>
<body>

<div class="navbar">
    <a href="#home">Home</a>
</div>

<div class="main">

  <!-- Create a paragraph with modern in-line CSS -->
  <p style="font-size: 20px; text-align: left; margin-bottom: 20px;">To modify a patient's details, click on them.</p>
  <p style="font-size: 20px; text-align: left; margin-bottom: 20px;">
    To add a new patient, click here:
    <button onclick="window.location.href='/addPatient.html';" class="addButton">Add New Patient</button>
  </p>


    <h2>Patients:</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Birthdate</th>
            <th>Deathdate</th>
            <th>SSN</th>
            <th>Drivers</th>
            <th>Passport</th>
            <th>Prefix</th>
            <th>First</th>
            <th>Last</th>
            <th>Suffix</th>
            <th>Maiden</th>
            <th>Marital</th>
            <th>Race</th>
            <th>Ethnicity</th>
            <th>Gender</th>
            <th>Birthplace</th>
            <th>Address</th>
            <th>City</th>
            <th>State</th>
            <th>ZIP</th>
        </tr>
        <%
            List<String[]> patientData = (List<String[]>) request.getAttribute("patientData");
            for (String[] patient : patientData) {
                %><tr><%
                for (int i = 0; i < patient.length; i++) {
                    %><td><%= patient[i].isEmpty() ? " " : patient[i] %></td><%
                }
                %></tr><%
            }
        %>
    </table>
</div>
</body>
</html>
