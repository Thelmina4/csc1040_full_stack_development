let names = ["Jogn", "Paul", 'ringo', 'george'];
names.forEach(x => console.log(x));

console.log("Hello");
console.log(42);

// this prints out as 0, 1, 2, 3 not the string name
for (let i = 0; i < names.length; i++) {
    console.log("Name: ", names[i]);
}

for (let name of names) {
    console.log(name);
}
names.forEach(function(name) {
    console.log(name)
})
names.forEach(name => console.log(name));


let score = 0;
score = 10;
console.log(score);
score++;
console.log(score);
score--;
console.log(score);
console.log(score/3);
console.log(score=="10");       // true
console.log(score==="10");      // false
console.log(score===10);        // true
console.log(score!="10");       // false
console.log(score!=="10");      // true
console.log(score>=5);          // true
console.log(score<=5);          // false


// if (x > 0 && x < 10) { }   // and
// if (x === 5 || y === 5) { } // or
// if (!(x === y)) { }         // not

/*  If you want to convert a string to a number, 
    use Number("42") or parseInt("42") rather 
    than relying on JavaScript to figure it out. */

let temperature = 10;
if (temperature > 30) {
    console.log("Ai, que calore!");
} else if (temperature > 15) {
    console.log("Hmm, it's ok. \nMight need a jumper though.");
} else {
    console.log("Brr, it's cold enough to freeze the balls off a brass monkey!");
}

let day = new Date().getDay();
console.log(day);
switch (day) {
    case 0:
        console.log("Monday");
        break;
    case 1:
        console.log("Tuesday");
        break;
    case 2:
        console.log("Wednesday");
        break;
    case 3:
        console.log("Thursday");
        break;
    case 4:
        console.log("Friday");
        break;
    case 5:
        console.log("Saturday");
        break;
    case 6:
        console.log("Sunday");
        break;
}
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// for ... of ...
// for arrays (loops over values).
for (let name of names) {
    console.log(name);
}

let person = {
    "Name": "michael",
    "Age": 42,
    "title": "Dr"
};
// for ... in ...
//  for objects (loops over keys)
for (let key in person) {
    console.log(key, person[key]);
}

// functions
function greet(name) {
    console.log("Hello " + name);
}
greet("Anne");

function add(x, y) {
    return x + y;
}
let result = add(4, 5)
console.log(add(1, 3));
console.log(result);

// arrow function
const add1 = (x, y) => {
    return x + y;
}
console.log(add1(13, 3));

// arrow function - short form(single expression)
const add2 = (x, y) => x+y;
console.log(add2(1, 35));

let numbers = [1, 2, 3, 4, 5];
// double each number
let doubled = numbers.map(n=>n*2);
console.log(doubled);

// Keep only even nos
let evens = numbers.filter(n=>n%2==0);
console.log(evens);

// functions as values
const greet1 = (name) => console.log("hello " + name);
greet1("sdf");

// This is called a function expression 
const sayHello = function(name) {
    console.log("Hello, " + name);
};

sayHello("Alice");  // Hello, Alice

function shout(name) {
    console.log(name.toUpperCase() + "!");
}

const shout1 = (name) => console.log(name.toUpperCase())
// Notice that we wrote forEach(shout), not forEach(shout()). 
// The parentheses make all the difference:
// shout — the function itself (a value we're passing)
// shout() — calls the function immediately and passes its return value

names.forEach(shout);
names.forEach(shout1);