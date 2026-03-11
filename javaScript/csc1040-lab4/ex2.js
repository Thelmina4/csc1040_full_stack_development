// ex2.js

const students = [
    { name: "Alice", grade: 72 },
    { name: "Bob",   grade: 45 },
    { name: "Carol", grade: 88 },
    { name: "Dan",   grade: 35 },
    { name: "Eve",   grade: 91 },
    { name: "Sean",  grade: 11 },
];

for (let row of students) {
    console.log(`${row.name}: ${row.grade}`);
}
// filter out the students w grade 60 +
const passingStudents = students.filter(student => student.grade >= 60);
// now take those and use map to get the names
const passingNames = passingStudents.map(student => student.name);
console.log(`Passing students: ${passingStudents.length}`)
console.log(`Passing names: ${passingNames}`)

// let pass = 0;
// for (let row of students) {
//     if (row.grade >= 40) {
//         pass += 1
//     }
// }
// console.log(`Passing students: ${pass}`)

// .reduce() accumulates a single value across all elements. 
const total = students.reduce((sum, s) => sum + s.grade, 0);
// The second argument (0) is the starting value for sum. Divide the total by students.length to get the average.
console.log(`Class average: ${total/students.length}`);