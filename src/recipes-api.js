import {
  collection,
  deleteDoc,
  doc,
  getDocs,
  onSnapshot,
  query,
  setDoc
} from "https://www.gstatic.com/firebasejs/12.7.0/firebase-firestore.js";
import { db } from "./firebase.js";
import { normalizeRecipe, normalizeRecipes } from "./recipe-schema.js";

const RECIPES_COLLECTION = "recipes";

function recipesCollection() {
  return collection(db, RECIPES_COLLECTION);
}

function recipeDoc(id) {
  return doc(recipesCollection(), String(id));
}

export async function listRecipes() {
  const snap = await getDocs(recipesCollection());
  return normalizeRecipes(snap.docs.map((entry) => ({ id: entry.id, ...entry.data() })));
}

export function subscribeRecipes(onData) {
  return onSnapshot(query(recipesCollection()), (snap) => {
    const list = snap.docs.map((entry) => ({ id: entry.id, ...entry.data() }));
    onData(normalizeRecipes(list));
  });
}

export async function createRecipe(recipe) {
  const normalized = normalizeRecipe(recipe);
  if (!normalized.id) throw new Error("Missing recipe id");
  await setDoc(recipeDoc(normalized.id), normalized);
  return normalized;
}

export async function updateRecipe(recipe) {
  const normalized = normalizeRecipe(recipe);
  if (!normalized.id) throw new Error("Missing recipe id");
  await setDoc(recipeDoc(normalized.id), normalized);
  return normalized;
}

export async function deleteRecipeById(recipeId) {
  if (!recipeId) throw new Error("Missing recipe id");
  await deleteDoc(recipeDoc(recipeId));
}
