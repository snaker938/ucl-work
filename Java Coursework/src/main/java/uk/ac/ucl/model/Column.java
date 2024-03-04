package uk.ac.ucl.model;

import java.util.ArrayList;

public class Column {
    private String name;
    private ArrayList<String> rows;

    public Column(String name) {
        this.name = name;
        rows = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public int getSize() {
        return rows.size();
    }

    public String getRowValue(int row) {
        return rows.get(row);
    }

    public void setRowValue(int row, String value) {
        rows.set(row, value);
    }

    public void addRowValue(String value) {
        rows.add(value);
    }
}
