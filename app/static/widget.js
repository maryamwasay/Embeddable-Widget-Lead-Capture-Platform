(function () {

    console.log("===== FlyRank Widget Started =====");

    const script = document.currentScript ||
        document.querySelector("script[data-widget-id]");

    if (!script) {
        console.error("Script tag not found.");
        return;
    }

    const widgetId = script.getAttribute("data-widget-id");

    console.log("Widget ID:", widgetId);

    if (!widgetId) {
        console.error("Widget ID missing.");
        return;
    }

    const API_BASE = "http://127.0.0.1:8000";

    async function loadWidget() {

        console.log("Loading widget...");

        try {

            const response = await fetch(
                `${API_BASE}/public/widget/${widgetId}`
            );

            console.log("GET Status:", response.status);

            if (!response.ok) {
                throw new Error("Unable to load widget.");
            }

            const widget = await response.json();

            console.log("Widget:", widget);

            renderWidget(widget);

        } catch (err) {

            console.error(err);

        }

    }

    function renderWidget(widget) {

        console.log("Rendering widget...");

        const container =
            document.getElementById("widget-container");

        if (!container) {

            console.error("Container not found.");

            return;

        }

        container.innerHTML = "";

        const form = document.createElement("form");

        form.noValidate = true;

        form.style.border = "1px solid #ddd";
        form.style.padding = "20px";
        form.style.borderRadius = "8px";
        form.style.maxWidth = "450px";
        form.style.background = "#fff";

        const title = document.createElement("h2");
        title.textContent = widget.title;

        form.appendChild(title);

        if (widget.description) {

            const p = document.createElement("p");

            p.textContent = widget.description;

            form.appendChild(p);

        }

        widget.fields.forEach(field => {

            const label = document.createElement("label");

            label.textContent = field.name;

            label.style.display = "block";
            label.style.marginTop = "15px";

            const input = document.createElement("input");

            input.type = field.type || "text";
            input.name = field.name;
            input.required = field.required;

            input.style.width = "100%";
            input.style.padding = "10px";
            input.style.marginTop = "5px";

            form.appendChild(label);
            form.appendChild(input);

        });

        const honeypot = document.createElement("input");

        honeypot.type = "text";
        honeypot.name = "website";
        honeypot.style.display = "none";

        form.appendChild(honeypot);

        const button = document.createElement("button");

        button.type = "submit";
        button.textContent =
            widget.button_text || "Submit";

        button.style.marginTop = "20px";

        form.appendChild(button);

        form.addEventListener("submit", function (e) {

            console.log("SUBMIT EVENT FIRED");

            submitForm(e);

        });

        container.appendChild(form);

        console.log("Widget Rendered Successfully");

    }

    async function submitForm(event) {

        event.preventDefault();

        console.log("submitForm() called");

        const form = event.target;

        const data = {};

        Array.from(form.elements).forEach(element => {

            if (!element.name) return;

            data[element.name] = element.value;

        });

        console.log("Submitting Data:", data);

        try {

            const response = await fetch(

                `${API_BASE}/public/submit/${widgetId}`,

                {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"

                    },

                    body: JSON.stringify(data)

                }

            );

            console.log("POST Status:", response.status);

            const result = await response.json();

            console.log("Server Response:", result);

            if (response.ok) {

                alert(result.message);

                form.reset();

            } else {

                alert(result.detail || result.message);

            }

        }

        catch (err) {

            console.error(err);

            alert("Unable to connect to server.");

        }

    }

    loadWidget();

})();
