
const faceInput = document.getElementById("face");
const videoInput = document.getElementById("video");
const consentInput = document.getElementById("consent");
const form = document.getElementById("uploadForm");
const button = document.getElementById("generateBtn");
const statusText = document.getElementById("status");
const jobDetails = document.getElementById("jobDetails");

let faceURL = null;
let videoURL = null;

function updateButton() {
    button.disabled = !(
        faceInput.files.length &&
        videoInput.files.length &&
        consentInput.checked
    );
}

function showPreview(input, previewId, nameId, type) {
    const file = input.files[0];

    if (!file) return;

    const maxSize = type === "image" ? 10 : 100;

    if (file.size > maxSize * 1024 * 1024) {
        alert(`File must be under ${maxSize} MB.`);
        input.value = "";
        updateButton();
        return;
    }

    const url = URL.createObjectURL(file);

    const preview = document.getElementById(previewId);
    const name = document.getElementById(nameId);

    if (type === "image") {
        if (faceURL) URL.revokeObjectURL(faceURL);
        faceURL = url;
    } else {
        if (videoURL) URL.revokeObjectURL(videoURL);
        videoURL = url;
    }

    preview.src = url;
    preview.style.display = "block";
    name.textContent = file.name;

    updateButton();
}

faceInput.addEventListener("change", () => {
    showPreview(faceInput, "facePreview", "faceName", "image");
});

videoInput.addEventListener("change", () => {
    showPreview(videoInput, "videoPreview", "videoName", "video");
});

consentInput.addEventListener("change", updateButton);

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (!faceInput.files[0] || !videoInput.files[0]) return;

    button.disabled = true;
    button.textContent = "Uploading...";
    statusText.textContent = "Uploading your files...";
    jobDetails.textContent = "";

    const data = new FormData();

    data.append("face", faceInput.files[0]);
    data.append("video", videoInput.files[0]);
    data.append("consent", "yes");

    try {
        const response = await fetch("/api/jobs", {
            method: "POST",
            body: data
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Upload failed.");
        }

        statusText.textContent = result.message;

        jobDetails.textContent =
            "Project ID: " + result.job_id +
            " | Status: " + result.status;

    } catch (error) {
        statusText.textContent = error.message;
    } finally {
        button.textContent = "Upload & Prepare Project →";
        updateButton();
    }
});

updateButton();
