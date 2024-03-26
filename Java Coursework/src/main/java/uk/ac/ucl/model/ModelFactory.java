package uk.ac.ucl.model;

import java.io.IOException;

public class ModelFactory {
    private static Model model;

    public static Model getModel() throws IOException {
        if (model == null) {
            model = new Model();
            model.loadData();
        }
        return model;
    }

    // Method to force reloading data in the model
    public static void reloadData() throws IOException {
        if (model != null) {
            model.reloadData();
        } else {
            getModel(); // This will initialize the model if it hasn't been already
        }
    }
}
