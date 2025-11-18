function updateCPU() {
    // CPU Usage
    fetch("/cpu_usage")
        .then(res => res.json())
        .then(usageData => {
            document.getElementById("cpu-usage-text").textContent =
                "Usage: " + usageData.cpu_usage + "%";
        });

    // CPU Temp
    fetch("/cpu_temp")
        .then(res => res.json())
        .then(tempData => {
            document.getElementById("cpu-temp-text").textContent =
                "Temp: " + tempData.cpu_temp;
        });

    fetch("/cpu_freq")
        .then(res => res.json())
        .then(freqData => {
             document.getElementById("cpu-freq-text").textContent =
            "Freq: " + freqData.cpu_freq[0].current.toFixed(0) + " MHz";
        });
}

function updateMemory() {
        // Memory Usage
    fetch("/memory_usage")
        .then(res => res.json())
        .then(data => {
            document.getElementById("memory-usage-text").textContent =
                "Usage: " + data.memory_usage + "%";
        })
        .catch(err => console.error("MEM ERROR:", err));
    }

setInterval(() => {
    updateCPU();
    updateMemory();
}, 2000);

updateCPU();
updateMemory();

