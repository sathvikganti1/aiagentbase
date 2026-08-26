const input = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const messages = document.getElementById("messages");
const newChatButton = document.getElementById("newChat");


async function sendMessage() {

    const message = input.value.trim();

    if (!message) {
        return;
    }


    // Remove welcome message
    const welcome = document.querySelector(".welcome");

    if (welcome) {
        welcome.remove();
    }


    // Display user message
    addMessage("You", message, "user-message");


    // Clear input
    input.value = "";


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (data.error) {
            addMessage("AI", data.error, "ai-message");
            return;
        }


        // Display AI response
        addMessage(
            "AI",
            data.response,
            "ai-message"
        );

    }

    catch (error) {

        addMessage(
            "AI",
            "Something went wrong.",
            "ai-message"
        );

        console.error(error);

    }

}


function addMessage(sender, text, className) {

    const messageDiv =
        document.createElement("div");

    messageDiv.className =
        `message ${className}`;


    messageDiv.innerHTML = `
        <strong>${sender}</strong>
        <p>${text}</p>
    `;


    messages.appendChild(messageDiv);


    // Scroll to bottom
    messages.scrollTop =
        messages.scrollHeight;
}


/* Send button */

sendButton.addEventListener(
    "click",
    sendMessage
);


/* Enter key */

input.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    }
);


/* New chat */

newChatButton.addEventListener(
    "click",
    function() {

        messages.innerHTML = `
            <div class="welcome">
                <h2>Hello 👋</h2>
                <p>How can I help you today?</p>
            </div>
        `;

    }
);