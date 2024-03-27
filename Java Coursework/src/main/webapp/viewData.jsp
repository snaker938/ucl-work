<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Patient Data App</title>
    <link rel="stylesheet" href="viewData.css">

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
        <a href="index.html">Home</a>
    </div>

    <div class="main">

    <!-- Create a paragraph with modern in-line CSS -->
    <p style="font-size: 20px; text-align: left; margin-bottom: 20px;">To modify a patient's details, click on them.</p>
    <p style="font-size: 20px; text-align: left; margin-bottom: 20px;">
        To add a new patient, click here:
        <button onclick="window.location.href='/addPatient.html';" class="addButton">Add New Patient</button>
    </p>
    <p style="font-size: 20px; text-align: left; margin-bottom: 20px;">
        Search for specific patient:
        <form action="/searchPatient" method="get" style="display: inline;">
            <input type="text" name="searchQuery" placeholder="Enter search term" class="search-input">
            <select name="searchCategory" class="search-select">
                <option value="ID">ID</option>
                <option value="Birthdate">Birthdate</option>
                <option value="Deathdate">Deathdate</option>
                <option value="SSN">SSN</option>
                <option value="Drivers">Drivers</option>
                <option value="Passport">Passport</option>
                <option value="Prefix">Prefix</option>
                <option value="First">First</option>
                <option value="Last">Last</option>
                <option value="Suffix">Suffix</option>
                <option value="Maiden">Maiden</option>
                <option value="Marital">Marital</option>
                <option value="Race">Race</option>
                <option value="Ethnicity">Ethnicity</option>
                <option value="Gender">Gender</option>
                <option value="Birthplace">Birthplace</option>
                <option value="Address">Address</option>
                <option value="City">City</option>
                <option value="State">State</option>
                <option value="ZIP">ZIP</option>
            </select>
            <input type="submit" value="Search" class="search-button">
        </form>
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
