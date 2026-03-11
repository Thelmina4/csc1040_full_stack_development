// ex1.js

// don't need to declare the variable types
// LET:
// With let: You are explicitly declaring a block-scoped variable.
//  The variable exists only within the pair of curly braces {}
//  where it was defined.
let subject = "Computer Science";
let year = 2;
let is_enrolled = true;

if (is_enrolled) {
    console.log(`${subject} - Year ${year}`);
    // print(f"{subject} - Year {year}")
} else {
    console.log("Not enrolled");
    // print("Not enrolled")
}

// LET:
// below: You are technically not "declaring" a variable; 
// you are assigning a value to a property of the global object
//  (usually window in browsers).
//  This makes the variable accessible everywhere,
//  which often leads to bugs and "naming collisions." 
// marks = [62, 45, 78, 91, 55, 83];
// total = 0;

let marks = [62, 45, 78, 91, 55, 83];
let total = 0;
for (let mark of marks) {
    total += mark;
}
let average = total / marks.length;
console.log(`Average Mark: ${average}`);
// print(f"Average Mark: {average}")

for (let mark of marks) {
    if (mark >= 40) {
        console.log(`${mark} - Pass`);
        // print(f"{mark} - Pass")
    } else {
        console.log(`{mark} - Fail`);
        // print(f"{mark} - Fail")
    }
}