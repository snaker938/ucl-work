<%@ page import="java.util.List" %> <%@ page
contentType="text/html;charset=UTF-8" language="java" %>

<!DOCTYPE html>
<html>
  <head>
    <title>List of Patients</title>
    <style>
      /* Overall styles */
      body {
        font-family: sans-serif;
        margin: 0;
        padding: 0;
      }

      /* Styles for the patient list container */

      .patient-list-container {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 20px;
        padding-bottom: 30px; /* Increased padding at the bottom */
        position: fixed;
        top: 0;
        left: 0;
        height: calc(
          100vh - 30px
        ); /* Adjusted height to account for added padding */
        width: 250px;
        overflow-y: auto;
        transition: width 0.3s ease-in-out;
      }

      /* Styles for the expanded state */
      .patient-list-container.expanded {
        width: 500px; /* Expanded width */
      }

      /* Styles for the patient list header */
      .patient-list-header {
        display: flex; /* Center title and toggle button horizontally */
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
      }

      /* Styles for the patient list title */
      .patient-list-title {
        font-size: 18px;
        font-weight: bold;
      }

      /* Styles for the toggle button */
      .toggle-button {
        background-color: transparent;
        border: none;
        cursor: pointer;
        outline: none; /* Remove default outline */
        transform: rotate(
          90deg
        ); /* Initial rotation to point the arrow in the correct direction */
      }

      /* SVG styles for the expand/collapse icon */
      .toggle-button svg {
        width: 20px;
        height: 20px;
        fill: #333; /* Adjust icon color if needed */
        transition: transform 0.3s ease-in-out; /* Smooth rotation animation */
      }

      .toggle-button.expanded svg {
        transform: rotate(
          180deg
        ); /* Correct this as needed to ensure it points in the desired direction */
      }

      /* Styles for individual patient names */
      .patient-name {
        margin-bottom: 5px;
      }
    </style>
  </head>
  <body>
    <div class="patient-list-container">
      <div class="patient-list-header">
        <h2 class="patient-list-title">List of Patients</h2>
        <button class="toggle-button expanded" onclick="togglePatientList()">
          <svg viewBox="0 0 24 24">
            <path d="M16.59 8.59L12 13.17L7.41 8.59L6 10l6 6l6-6z"></path>
          </svg>
        </button>
      </div>

      <% String[] patients = (String[]) request.getAttribute("patientNames"); if
      (patients != null && patients.length > 0) { for (int i = 0; i <
      patients.length; i++) { String patientName = patients[i]; %>
      <p class="patient-name"><%= patientName %></p>
      <% } } else { %>
      <p>No patient data found.</p>
      <% } %>
    </div>

    <script>
      function togglePatientList() {
        const container = document.querySelector('.patient-list-container');
        const button = document.querySelector('.toggle-button');
        container.classList.toggle('expanded');
        button.classList.toggle('expanded'); // Ensure this line is added to toggle the class on the button as well.
      }
    </script>
  </body>
</html>
