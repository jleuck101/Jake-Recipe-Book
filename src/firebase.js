import { initializeApp } from "https://www.gstatic.com/firebasejs/12.7.0/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/12.7.0/firebase-firestore.js";
import { getAuth, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/12.7.0/firebase-auth.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/12.7.0/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyAFgODyKQFacEO3xfslhTeeU4n2hKcAy2s",
  authDomain: "jake-recipes.firebaseapp.com",
  projectId: "jake-recipes",
  storageBucket: "jake-recipes.firebasestorage.app",
  messagingSenderId: "337488882837",
  appId: "1:337488882837:web:78b7ad6a163eaac4b3bf9c",
  measurementId: "G-1PQX8MWL3J"
};

export const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const auth = getAuth(app);
export const storage = getStorage(app);
export const provider = new GoogleAuthProvider();

provider.setCustomParameters({ prompt: "select_account" });
