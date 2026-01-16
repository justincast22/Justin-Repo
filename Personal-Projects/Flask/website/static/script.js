async function generatePassword() {
    const length = document.getElementById("lengthInput").value;

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ length: parseInt(length) })
    });

    const data = await response.json();

    document.getElementById("passwordOutput").textContent = data.password;
    document.getElementById("entropyOutput").textContent = data.entropy + " bits";
}

function copyPassword() {
    const text = document.getElementById("passwordOutput").textContent;

    if (!text) {
        alert("No password to copy!");
        return;
    }

    navigator.clipboard.writeText(text);
    alert("Password copied!");
}
