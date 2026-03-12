// In Lab 4 you fetched data using .then() chains.
//  async/await is another way to write the same thing
//   — it lets asynchronous code read like ordinary sequential code.

// .then() style 
url = "https://www.computing.dcu.ie/~mscriney/csc1040/labs/lab-5/";

fetch(url)
    .then(response => response.json)
    .then(data => console.log(data))
    .catch(error => console.error(error));

// async/await style
async function loadData() {
    try {
        // The await keyword pauses execution inside the function until the promise resolves.
        //  The try/catch block handles any errors
        //  — equivalent to .catch()
        //  — but it also catches runtime errors inside the block,
        //  making it more robust.
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
loadData();