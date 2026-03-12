// localStorage lets you save data in the browser that persists across
//  page reloads and even after the tab is closed.
//  It stores everything as strings, so objects and arrays
//  must be converted using JSON.stringify() and JSON.parse().

// Saving data
localStorage.setItem("username", "Alice");
localStorage.setItem("scores", JSON.stringify([10, 20, 30]));

// Reading data
const name   = localStorage.getItem("username");        // "Alice"
const scores = JSON.parse(localStorage.getItem("scores")); // [10, 20, 30]

// Removing data
localStorage.removeItem("username");

// If getItem is called for a key that does not exist, it returns null
//  — always check for this before calling JSON.parse.