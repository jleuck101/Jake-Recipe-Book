import {
  browserLocalPersistence,
  onAuthStateChanged,
  setPersistence,
  signInWithPopup,
  signOut
} from "https://www.gstatic.com/firebasejs/12.7.0/firebase-auth.js";
import { auth, provider } from "./firebase.js";

const OWNER_UID = "";
const OWNER_EMAIL = "jakeleuck101@gmail.com";

let currentUser = null;
let authInitDone = false;
let authInitResolve;

export const authInit = new Promise((resolve) => {
  authInitResolve = resolve;
});

setPersistence(auth, browserLocalPersistence).catch(console.warn);

function userEmail(user) {
  return String(user?.email || user?.providerData?.[0]?.email || "").toLowerCase();
}

export function isOwnerUser(user) {
  if (!user) return false;
  if (OWNER_UID) return user.uid === OWNER_UID;
  return userEmail(user) === OWNER_EMAIL.toLowerCase();
}

export function getCurrentUser() {
  return currentUser;
}

export async function signIn() {
  return signInWithPopup(auth, provider);
}

export async function signOutUser() {
  return signOut(auth);
}

export function subscribeToAuth(callback) {
  return onAuthStateChanged(auth, (user) => {
    currentUser = user || null;

    if (!authInitDone) {
      authInitDone = true;
      authInitResolve(currentUser);
    }

    if (callback) callback(currentUser);
  });
}
