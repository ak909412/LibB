const express = require("express");
const fs = require("fs");
const path = require("path");
const cors = require("cors");

const app = express();
const PORT = 3000;
const BOOKINGS_FILE = path.join(__dirname, "bookings.txt");

app.use(cors()); // Enable CORS for client access
app.use(express.json()); // Parse JSON bodies

// Route to save a booking
app.post("/save-booking", (req, res) => {
  const { floor, deskNumber, date, timeIn, timeOut } = req.body;
  const bookingData = `${new Date().toISOString()}, ${floor}, ${deskNumber}, ${date}, ${timeIn}, ${timeOut}\n`;

  // Append the booking data with a unique id (timestamp)
  fs.appendFile(BOOKINGS_FILE, bookingData, (err) => {
    if (err) {
      console.error("Error saving booking:", err);
      return res.status(500).send("Error saving booking");
    }
    res.send("Booking saved successfully");
  });
});

// Route to view bookings
app.get("/view-bookings", (req, res) => {
  fs.readFile(BOOKINGS_FILE, "utf8", (err, data) => {
    if (err) {
      console.error("Error reading bookings:", err);
      return res.status(500).json({ error: "Error reading bookings" });
    }

    // Convert each line to an object and add an ID (first part of the line)
    const bookings = data
      .trim()
      .split("\n")
      .filter((line) => line.length > 0)
      .map((line) => {
        const [id, floor, deskNumber, date, timeIn, timeOut] = line.split(", ");
        return {
          id,
          floor,
          deskNumber,
          date,
          timeIn,
          timeOut,
        };
      });

    res.json(bookings);
  });
});

// Route to delete all bookings
app.delete("/delete-bookings", (req, res) => {
  fs.writeFile(BOOKINGS_FILE, "", (err) => {
    if (err) {
      console.error("Error deleting bookings:", err);
      return res.status(500).send("Error deleting bookings");
    }
    res.send("All bookings deleted successfully");
  });
});

// Route to delete an individual booking by ID
app.delete("/delete-booking/:id", (req, res) => {
  const bookingId = req.params.id.trim(); // Ensure the ID is trimmed

  fs.readFile(BOOKINGS_FILE, "utf8", (err, data) => {
    if (err) {
      console.error("Error reading bookings:", err);
      return res.status(500).send("Error reading bookings");
    }

    // Split data into an array of lines and trim each line
    const bookings = data
      .trim()
      .split("\n")
      .map((line) => line.trim());

    // Find the index of the booking to delete
    const bookingIndex = bookings.findIndex((line) =>
      line.startsWith(bookingId)
    );

    if (bookingIndex === -1) {
      return res.status(404).send("Booking not found");
    }

    // Remove the booking from the array
    bookings.splice(bookingIndex, 1);

    // Write the updated bookings back to the file
    fs.writeFile(BOOKINGS_FILE, bookings.join("\n") + "\n", (err) => {
      if (err) {
        console.error("Error deleting booking:", err);
        return res.status(500).send("Error deleting booking");
      }
      res.send(`Booking with ID ${bookingId} deleted successfully`);
    });
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
