const apiUrl = "http://127.0.0.1:5000";

// Stage 1: Generate Updated Materials
document.getElementById("generateMaterials").addEventListener("click", () => {
    fetch(`${apiUrl}/generate-materials`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("generatedMaterials").innerText = data.materials;
        })
        .catch(error => console.error("Error fetching materials:", error));
});

// Stage 2: Update Materials Based on Feedback
document.getElementById("updateMaterials").addEventListener("click", () => {
    const feedback = document.getElementById("feedbackInput").value;
    fetch(`${apiUrl}/update-materials`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ feedback })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("updatedMaterials").innerText = data.materials;
        })
        .catch(error => console.error("Error updating materials:", error));
});

// Stage 3: Personalized Materials
document.getElementById("personalizeMaterials").addEventListener("click", () => {
    const feedback = document.getElementById("personalFeedback").value;
    fetch(`${apiUrl}/personalize-materials`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ feedback })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("personalizedMaterials").innerText = data.materials;
        })
        .catch(error => console.error("Error personalizing materials:", error));
});
