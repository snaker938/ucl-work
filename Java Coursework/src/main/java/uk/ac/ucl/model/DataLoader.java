package uk.ac.ucl.model;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class DataLoader {

    public DataFrame loadDataFromFile() throws IOException {

        String latestFileName = findLatestDataFileName();
        String filePath = Paths.get(latestFileName).toString();

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

    private static String findLatestDataFileName() throws IOException {
        String directoryPath = "data"; // Adjust this path as necessary for your project structure
        File dir = new File(directoryPath);

        // Ensure the directory exists
        if (!dir.exists()) {
            dir.mkdirs();
            Path initialFilePath = Paths.get(dir.getPath(), "data.csv");
            createNewDataFileWithHeaders(initialFilePath);
            return initialFilePath.toString();
        }

        // Get all csv files starting with "data" and sort them to find the latest
        File[] files = dir.listFiles((d, name) -> name.startsWith("data") && name.endsWith(".csv"));
        if (files == null || files.length == 0) {
            Path filePath = Paths.get(dir.getPath(), "data.csv");
            createNewDataFileWithHeaders(filePath);
            return filePath.toString();
        } else {
            // Sort files by name to find the latest
            return Arrays.stream(files)
                .sorted(Comparator.comparing(File::getName).reversed())
                .findFirst()
                .map(File::getPath)
                .orElseThrow(() -> new IOException("Failed to find the latest data file."));
        }
    }

    private static void createNewDataFileWithHeaders(Path filePath) throws IOException {
        // Headers for the new CSV file
        String headers = "ID,BIRTHDATE,DEATHDATE,SSN,DRIVERS,PASSPORT,PREFIX,FIRST,LAST,SUFFIX,MAIDEN,MARITAL,RACE,ETHNICITY,GENDER,BIRTHPLACE,ADDRESS,CITY,STATE,ZIP";
        try (BufferedWriter writer = Files.newBufferedWriter(filePath)) {
            writer.write(headers);
            writer.newLine();
        }
    }
}
