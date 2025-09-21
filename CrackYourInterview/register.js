import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyBpYr0QNgFvAC4Rb4DtHJQ8wRY7q4pto",
  authDomain: "crackyourinterview-db541.firebaseapp.com",
  projectId: "crackyourinterview-db541",
  storageBucket: "crackyourinterview-db541.appspot.com",
  messagingSenderId: "218429102531",
  appId: "1:218429102531:web:9c6a32a78fdda26986c576",
  measurementId: "G-DF05KWK9ZH"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

window.signup = function () {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!email || !password) {
    alert("Please enter both email and password.");
    return;
  }

  createUserWithEmailAndPassword(auth, email, password)
    .then(userCredential => {
      alert("Signup successful!");
    })
    .catch(error => {
      alert("Signup error: " + error.message);
    });
};