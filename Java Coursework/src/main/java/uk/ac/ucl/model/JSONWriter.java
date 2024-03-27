package uk.ac.ucl.model;

import org.json.JSONArray;
import org.json.JSONObject;
import java.util.List;

public class JSONWriter {

    public static String convertDataFrameToJson(DataFrame dataFrame) {
        JSONArray jsonArray = new JSONArray();
        List<String> columnNames = dataFrame.getColumnNames();
        int numRows = dataFrame.getRowCount();

        for (int rowIndex = 0; rowIndex < numRows; rowIndex++) {
            JSONObject rowObj = new JSONObject();
            for (String columnName : columnNames) {
                String value = dataFrame.getValue(columnName, rowIndex);
                rowObj.put(columnName, value);
            }
            jsonArray.put(rowObj);
        }

        return jsonArray.toString(4);
    }
}
