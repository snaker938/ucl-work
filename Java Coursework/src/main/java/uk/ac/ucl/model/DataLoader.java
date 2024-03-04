package uk.ac.ucl.model;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.List;

public class DataLoader {

    public DataFrame loadDataFromFile(String filePath) throws IOException {
        DataFrame dataFrame = new DataFrame();
        try (Reader in = new FileReader(filePath)) {
            CSVParser parser = CSVFormat.DEFAULT.withFirstRecordAsHeader().parse(in);
            List<String> columnNames = parser.getHeaderNames();

            for (String columnName : columnNames) {
                dataFrame.addColumn(new Column(columnName));
            }

            for (CSVRecord record : parser) {
                for (int i = 0; i < columnNames.size(); i++) {
                    String value = record.get(i);
                    dataFrame.addValue(columnNames.get(i), value);
                }
            }
            return dataFrame;
        } catch (IOException e) {
            // Handle the error here, potentially logging the exception and forwarding to an error page with a modal
            throw new RuntimeException("Error parsing data file", e);
        }
    }
}
