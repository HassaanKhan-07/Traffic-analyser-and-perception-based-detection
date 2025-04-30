// Function to handle file upload and process traffic analysis
document.getElementById("uploadForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission behavior

    // Get form elements
    let fileInput = document.getElementById("fileInput");
    let responseText = document.getElementById("response");

    // Validate file selection
    if (fileInput.files.length === 0) {
        displayMessage("Please select a file!", "red");
        return;
    }

    // Prepare the form data
    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    // Send the image file to the backend for processing
    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the detected road for the green light
        displayMessage(`Green light for: ${data.green_light}`, "green");

        // If a road is given the green light, activate background change
        if (data.green_light) {
            activateGreenLight();
        }
    })
    .catch(error => {
        displayMessage("Error processing the image. Please try again.", "red");
    });
});
document.getElementById("fileInput").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.getElementById("uploadedImage");
            img.src = e.target.result;
            img.style.display = "block";  // Show the image
        };
        reader.readAsDataURL(file);
    }
});

// Function to display response messages with color indication
function displayMessage(message, color) {
    let responseText = document.getElementById("response");
    responseText.textContent = message;
    responseText.style.color = color;
}

// Function to change background color when green light is given
function activateGreenLight() {
    document.body.classList.add("green-light");

    // Revert back to normal after 5 seconds
    setTimeout(() => {
        document.body.classList.remove("green-light");
    }, 5000);
}

// Function to display response messages with color indication
function displayMessage(message, color) {
    let responseText = document.getElementById("response");
    responseText.textContent = message;
    responseText.style.color = color;
}

// Function to change background color when green light is given
function activateGreenLight() {
    document.body.classList.add("green-light");

    // Revert back to normal after 5 seconds
    setTimeout(() => {
        document.body.classList.remove("green-light");
    }, 5000);
}


