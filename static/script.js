function checkPassword() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let resultText = document.getElementById("result-text");
    let suggestionBox = document.getElementById("suggestion-box");
    let copyBtn = document.getElementById("copy-btn");

    fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.strong) {
            resultText.style.color = "green";
            resultText.innerText = "✅ This password is secure and ready to use!";
            suggestionBox.style.display = "none";
        } else {
            resultText.style.color = "red";
            resultText.innerHTML = "❌ <strong>Issues:</strong><br>" + data.feedback.join("<br>");
            suggestionBox.style.display = "block";
            copyBtn.style.display = "none"; // Hide copy button if manual pass is weak
        }
    });
}

function generateNew() {
    fetch("/generate")
    .then(res => res.json())
    .then(data => {
        let passwordInput = document.getElementById("password");
        
        // 1. Fill the value
        passwordInput.value = data.password;
        
        // 2. IMPORTANT: Change type to 'text' so user can SEE it
        passwordInput.type = "text"; 
        
        // 3. Show the Copy Button
        document.getElementById("copy-btn").style.display = "block";

        // 4. Automatically re-verify to show green checkmark
        checkPassword();
    });
}

function togglePassword() {
    let passwordInput = document.getElementById("password");
    passwordInput.type = passwordInput.type === "password" ? "text" : "password";
}

function copyPassword() {
    let passwordInput = document.getElementById("password");
    passwordInput.select();
    document.execCommand("copy");
    alert("Password copied to clipboard!");
}