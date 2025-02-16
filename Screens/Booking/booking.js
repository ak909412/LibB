document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".container .button");
  const formPopup = document.getElementById("bookingForm");
  const deskNumberInput = document.getElementById("deskNumber");
  const form = document.querySelector(".form-container");

  // Show the booking form when a desk button is clicked
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const deskNumber = this.getAttribute("data-desk-number");
      deskNumberInput.value = deskNumber;
      formPopup.style.display = "block";
    });
  });

  // Handle form submission
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const floor = document.getElementById("floor").value;
    const deskNumber = document.getElementById("deskNumber").value;
    const date = document.getElementById("date").value;
    const timeIn = document.getElementById("timeIn").value;
    const timeOut = document.getElementById("timeOut").value;

    // Validate the date to ensure it is within the next 2 days
    const currentDate = new Date();
    currentDate.setHours(0, 0, 0, 0); // Reset currentDate time to 00:00
    const selectedDate = new Date(date);
    selectedDate.setHours(0, 0, 0, 0); // Reset selectedDate time to 00:00

    const diffInDays = (selectedDate - currentDate) / (1000 * 3600 * 24); // Difference in days

    if (diffInDays < 0 || diffInDays > 2) {
      alert(
        "You can only book a desk for today, tomorrow, or the day after tomorrow."
      );
      return;
    }

    // Validate the time: Time Out should be after Time In and have a minimum 30 minute difference
    const timeInDate = new Date(`1970-01-01T${timeIn}:00`);
    const timeOutDate = new Date(`1970-01-01T${timeOut}:00`);

    if (timeOutDate <= timeInDate) {
      alert("Time Out must be later than Time In.");
      return;
    }

    // Ensure there is at least a 30-minute difference
    const timeDifference = (timeOutDate - timeInDate) / 60000; // Convert to minutes
    if (timeDifference < 30) {
      alert("Time Out must be at least 30 minutes after Time In.");
      return;
    }

    // Validate that the time is not between 11 PM and 8 AM
    const hourIn = timeInDate.getHours();
    if (hourIn >= 23 || hourIn < 8) {
      alert("Desk bookings cannot be made between 11 PM and 8 AM.");
      return;
    }

    // Send data to the server using fetch API
    const formData = {
      floor,
      deskNumber,
      date,
      timeIn,
      timeOut,
    };

    fetch("http://localhost:3000/save-booking", {
      // Update with your server URL
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.text()) // Handle the server's response
      .then((data) => {
        alert(data); // Show success message
        closeForm(); // Close the booking form after successful submission
      })
      .catch((error) => {
        console.error("Error:", error); // Handle any errors
      });
  });
});

// Fetch and display current bookings
fetch("http://localhost:3000/view-bookings")
  .then((response) => response.json())
  .then((data) => {
    const reservationCount = data.length;
    const reservedDeskNumbers = data
      .map((booking) => booking.deskNumber)
      .join(", ");

    document.getElementById(
      "reservationCount"
    ).textContent = `Desks Reserved: ${reservationCount}`;
    document.getElementById(
      "reservedDeskNumbers"
    ).textContent = `Reserved Desks: ${reservedDeskNumbers || "None"}`;
  })
  .catch((err) => {
    console.error("Error fetching reservations:", err);
  });

// Function to close the booking form
function closeForm() {
  document.getElementById("bookingForm").style.display = "none";
}

// Function to close the booking form
function closeForm() {
  document.getElementById("bookingForm").style.display = "none";
}
