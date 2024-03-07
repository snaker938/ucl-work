<%@ page import="java.util.List" %> <%@ page
contentType="text/html;charset=UTF-8" language="java" %>

<!DOCTYPE html>
<html>
  <head>
    <title>List of Patients</title>
    <link rel="stylesheet" type="text/css" href="viewData.css" />
  </head>
  <body>
    <div
      class="patient-list-container"
      id="patientListContainer"
      style="display: none"
    >
      <div class="patient-list-header" id="myHeader">
        <h2 class="patient-list-title">List of Patients</h2>
        <button class="toggle-button expanded" onclick="togglePatientList()">
          <svg viewBox="0 0 24 24">
            <path d="M16.59 8.59L12 13.17L7.41 8.59L6 10l6 6l6-6z"></path>
          </svg>
        </button>
      </div>
    </div>

    <div class="patient-states-container">
      <% String[] patientStates = (String[])
      request.getAttribute("patientStates"); %>
      <ul class="bar-chart">
        <% for (String patientState : patientStates) { %>
        <li>
          <% String[] stateAndCount = patientState.split(":"); %>
          <span class="state-label"><%= stateAndCount[0] %></span>
          <span
            class="bar"
            style="width: <%= Integer.parseInt(stateAndCount[1]) * 10 %>%"
          ></span>
          <span class="count"><%= stateAndCount[1] %></span>
        </li>
        <% } %>
      </ul>
    </div>

    <script>
      function togglePatientList() {
        const container = document.querySelector('.patient-list-container');
        const button = document.querySelector('.toggle-button');
        container.classList.toggle('expanded');
        button.classList.toggle('expanded'); // Ensure this line is added to toggle the class on the button as well.
      }

      var patientListContainer = document.getElementById(
        'patientListContainer'
      );

      patientListContainer.onscroll = function () {
        myFunction();
      };
    </script>
  </body>
</html>
