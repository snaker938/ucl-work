<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>Edit Patient</title>
    <link rel="stylesheet" href="editPatient.css" />
    <style></style>
  </head>
  <body>
    <h2>Edit Patient Details</h2>
    <form action="/updatePatient" method="post">
      <% String[] details = (String[])request.getAttribute("patientDetails"); %>
      <% Boolean isEditingPatient =
      (Boolean)request.getAttribute("isEditingPatient"); %>
      <div class="form-group">
        <label for="id">ID:</label>
        <input type="text" id="id" name="ID" value="<%=details[0]%>" readonly />
      </div>
      <div class="form-group">
        <label for="birthdate">Birthdate:</label
        ><input
          type="date"
          id="birthdate"
          name="BIRTHDATE"
          value="<%=details[1]%>"
        />
      </div>
      <div class="form-group">
        <label for="deathdate">Deathdate:</label
        ><input
          type="date"
          id="deathdate"
          name="DEATHDATE"
          value="<%=details[2]%>"
        />
      </div>
      <div class="form-group">
        <label for="ssn">SSN:</label
        ><input type="text" id="ssn" name="SSN" value="<%=details[3]%>" />
      </div>
      <div class="form-group">
        <label for="drivers">Drivers:</label
        ><input
          type="text"
          id="drivers"
          name="DRIVERS"
          value="<%=details[4]%>"
        />
      </div>
      <div class="form-group">
        <label for="passport">Passport:</label
        ><input
          type="text"
          id="passport"
          name="PASSPORT"
          value="<%=details[5]%>"
        />
      </div>
      <div class="form-group">
        <label for="prefix">Prefix:</label
        ><input type="text" id="prefix" name="PREFIX" value="<%=details[6]%>" />
      </div>
      <div class="form-group">
        <label for="first">First:</label
        ><input type="text" id="first" name="FIRST" value="<%=details[7]%>" />
      </div>
      <div class="form-group">
        <label for="last">Last:</label
        ><input type="text" id="last" name="LAST" value="<%=details[8]%>" />
      </div>
      <div class="form-group">
        <label for="suffix">Suffix:</label
        ><input type="text" id="suffix" name="SUFFIX" value="<%=details[9]%>" />
      </div>
      <div class="form-group">
        <label for="maiden">Maiden:</label
        ><input
          type="text"
          id="maiden"
          name="MAIDEN"
          value="<%=details[10]%>"
        />
      </div>
      <div class="form-group">
        <label for="marital">Marital:</label
        ><input
          type="text"
          id="marital"
          name="MARITAL"
          value="<%=details[11]%>"
        />
      </div>
      <div class="form-group">
        <label for="race">Race:</label
        ><input type="text" id="race" name="RACE" value="<%=details[12]%>" />
      </div>
      <div class="form-group">
        <label for="ethnicity">Ethnicity:</label
        ><input
          type="text"
          id="ethnicity"
          name="ETHNICITY"
          value="<%=details[13]%>"
        />
      </div>
      <div class="form-group">
        <label for="gender">Gender:</label
        ><input
          type="text"
          id="gender"
          name="GENDER"
          value="<%=details[14]%>"
        />
      </div>
      <div class="form-group">
        <label for="birthplace">Birthplace:</label
        ><input
          type="text"
          id="birthplace"
          name="BIRTHPLACE"
          value="<%=details[15]%>"
        />
      </div>
      <div class="form-group">
        <label for="address">Address:</label
        ><input
          type="text"
          id="address"
          name="ADDRESS"
          value="<%=details[16]%>"
        />
      </div>
      <div class="form-group">
        <label for="city">City:</label
        ><input type="text" id="city" name="CITY" value="<%=details[17]%>" />
      </div>
      <div class="form-group">
        <label for="state">State:</label
        ><input type="text" id="state" name="STATE" value="<%=details[18]%>" />
      </div>
      <div class="form-group">
        <label for="zip">ZIP:</label
        ><input type="text" id="zip" name="ZIP" value="<%=details[19]%>" />
      </div>
      <div class="button-group">
        <input type="submit" value="Save Changes" />
        <button
          type="button"
          class="cancel-button"
          onclick="window.location.href='/viewData.html';"
        >
          Cancel
        </button>

        <% if(isEditingPatient) { %>
        <button
          type="button"
          class="delete-button"
          onclick="window.location.href='/deletePatient/<%=details[0]%>';"
        >
          Delete Patient
        </button>
        <% } %>
      </div>
    </form>
  </body>
</html>
```
