<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title>Edit Patient</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
        color: #333;
        padding: 20px;
      }
      h2 {
        color: #4a4a4a;
        text-align: center; /* Center align the header */
      }
      form {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        max-width: 800px;
        margin: 20px auto;
      }
      .form-group {
        margin-bottom: 15px;
      }
      .form-group label {
        display: block;
        margin-bottom: 5px;
      }
      .form-group input[type='text'],
      .form-group input[type='date'],
      .form-group input[type='email'] {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
      }
      .form-group input[type='text'][readonly] {
        background-color: #e9e9e9; /* Different background for read-only */
        font-weight: bold; /* Make the font bold */
      }
      input[type='submit'],
      .cancel-button {
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-right: 10px; /* Spacing between buttons */
      }
      input[type='submit'] {
        background-color: #3a7bd5; /* Darkish blue */
        color: white;
      }
      input[type='submit']:hover {
        background-color: #2a5ca8; /* Darker blue on hover */
      }
      .cancel-button {
        background-color: #d9534f; /* Red */
        color: white;
      }
      .cancel-button:hover {
        background-color: #c9302c; /* Darker red on hover */
      }
    </style>
  </head>
  <body>
    <h2>Edit Patient Details</h2>
    <form action="/updatePatient" method="post">
      <% String[] details = (String[])request.getAttribute("patientDetails"); %>
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
      <input type="submit" value="Save Changes" />
      <button
        type="button"
        class="cancel-button"
        onclick="window.location.href='/viewData.html';"
      >
        Cancel
      </button>
    </form>
  </body>
</html>
```
