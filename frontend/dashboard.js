const API = "http://127.0.0.1:8000";

const demoBtn = document.getElementById("demoBtn");
const awsBtn = document.getElementById("awsBtn");

demoBtn.addEventListener("click", () => {
    runScan("/api/demo-scan");
});

awsBtn.addEventListener("click", () => {
    runScan("/api/aws-scan");
});


async function runScan(endpoint) {

    const loading = document.getElementById("loading");

    loading.textContent = "Scanning...";

    try {

        const response = await fetch(API + endpoint);

        if (!response.ok) {
            throw new Error("Scan failed");
        }

        const data = await response.json();

        updateDashboard(data);

        loading.textContent = "Scan completed";

    } catch (error) {

        console.error(error);

        loading.textContent =
            "Unable to connect to CloudSentinel backend.";

    }
}


function updateDashboard(data) {

    const security = data.security;

    document.getElementById("score").textContent =
        security.score;

    document.getElementById("rating").textContent =
        security.rating;

    document.getElementById("critical").textContent =
        security.counts.CRITICAL;

    document.getElementById("high").textContent =
        security.counts.HIGH;

    document.getElementById("medium").textContent =
        security.counts.MEDIUM;

    document.getElementById("low").textContent =
        security.counts.LOW;

    document.getElementById("mode").textContent =
        data.mode;

    document.getElementById("total").textContent =
        security.total_findings;

    renderFindings(data.findings);
}


function renderFindings(findings) {

    const container =
        document.getElementById("findings");

    container.innerHTML = "";

    if (findings.length === 0) {

        container.innerHTML = `
            <div class="empty">
                No security findings detected.
            </div>
        `;

        return;
    }

    findings.forEach(finding => {

        const card = document.createElement("div");

        card.className = "finding";

        card.innerHTML = `

            <div class="finding-header">

                <div>

                    <h3>
                        ${escapeHTML(finding.title)}
                    </h3>

                    <p>
                        ${escapeHTML(finding.service)}
                        •
                        ${escapeHTML(finding.resource)}
                    </p>

                </div>

                <span class="badge ${finding.severity}">
                    ${finding.severity}
                </span>

            </div>

            <p style="margin-top:15px;">
                ${escapeHTML(finding.description)}
            </p>

            ${
                finding.port
                ?
                `<p style="margin-top:8px;">
                    Port: ${escapeHTML(finding.port)}
                </p>`
                :
                ""
            }

            <div class="recommendation">

                <strong>
                    Recommended Remediation
                </strong>

                ${escapeHTML(finding.recommendation)}

            </div>
        `;

        container.appendChild(card);
    });
}


function escapeHTML(value) {

    if (!value) {
        return "";
    }

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}