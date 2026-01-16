document.addEventListener("DOMContentLoaded", function() {
    const passwordOutput = document.getElementById("passwordOutput");
    const entropyOutput = document.getElementById("entropyOutput"); // optional, only for random format
    const lengthInput = document.getElementById("lengthInput");     // random format input
    const amountInput = document.getElementById("amountInput");     // chunked format input
    const sizeInput = document.getElementById("sizeInput");         // chunked format input

    window.generatePassword = async function() {
        let url, body;

        if (lengthInput) {
            // Random password format
            url = "/generate";
            body = { length: parseInt(lengthInput.value) };
        } else if (amountInput && sizeInput) {
            // Chunked password format
            url = "/generate_v2";
            body = { chunk_length: parseInt(amountInput.value), chunk_size: parseInt(sizeInput.value) };
        } else {
            console.error("No input found for password generation!");
            return;
        }

        try {
            const response = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(body)
            });

            const data = await response.json();
            passwordOutput.textContent = data.password;

            if (entropyOutput && data.entropy) {
                entropyOutput.textContent = data.entropy + " bits";
            } else if (entropyOutput) {
                entropyOutput.textContent = ""; // clear entropy if not provided
            }
        } catch (err) {
            console.error("Error generating password:", err);
            passwordOutput.textContent = "Error generating password";
        }
    }

    window.copyPassword = function() {
        const text = passwordOutput.textContent;
        if (text) {
            navigator.clipboard.writeText(text)
                .then(() => alert("Password copied!"))
                .catch(err => console.error("Copy failed:", err));
        } else {
            alert("No password to copy!");
        }
    }
});
