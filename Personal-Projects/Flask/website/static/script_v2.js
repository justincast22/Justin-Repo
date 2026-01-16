document.addEventListener("DOMContentLoaded", function() {
    const amountInput = document.getElementById("amountInput");
    const sizeInput = document.getElementById("sizeInput");
    const passwordOutput = document.getElementById("passwordOutput");

    window.generatePassword = function() {
        const chunkLength = parseInt(amountInput.value);
        const chunkSize = parseInt(sizeInput.value);

        fetch("/generate_v2", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ chunk_length: chunkLength, chunk_size: chunkSize })
        })
        .then(response => response.json())
        .then(data => {
            passwordOutput.textContent = data.password;
        })
        .catch(err => {
            console.error(err);
            passwordOutput.textContent = "Error generating password";
        });
    }

    window.copyPassword = function() {
        const text = passwordOutput.textContent;
        if (text) {
            navigator.clipboard.writeText(text)
                .then(() => alert("Password copied!"))
                .catch(err => console.error("Copy failed:", err));
        }
    }
});
