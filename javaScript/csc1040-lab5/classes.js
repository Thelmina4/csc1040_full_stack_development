class Animal {
    constructor(name, sound) {
        this.name = name;
        this.sound = sound || "hi";
    }
    speak() {
        console.log(`${this.name} says ${this.sound}`);
    }
}
const dog = new Animal("Dog");
dog.speak();
// node classes.js