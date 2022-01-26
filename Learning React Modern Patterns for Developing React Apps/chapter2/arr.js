const [firstAnimal] = ["Horse", "Mouse", "Cat"];

console.log(firstAnimal);

const [, , thirdAnimal] = ["Horse", "Mouse", "Cat"];

console.log(thirdAnimal);

const name = "Tallac";
const elevation = 9738;

const funHike = {name, elevation};

console.log(funHike);

const print = function() {
    console.log(`Mt. ${this.name} is ${this.elevation} feet tail`);
};

const funHike2 = {name, elevation, print};

funHike2.print();

const peaks = ["Tallac", "ASdasd"];
const canyons = ["Ward", "Blackwood"];
const tahoe = [...peaks, ...canyons];

console.log(tahoe.join(", "));

const [last] = peaks.reverse();
console.log(last);
console.log(peaks.join(", "));
const [last2] = [...peaks].reverse();

console.log(last2);
console.log(peaks.join(", "));

const lakes = ["Donner", "Marlette", "Fallen"];
const [first, ...others] = lakes;
console.log(others.join(", "));

function directions(...args) {
    let [start, ...remaining] = args;
    let [finish, ...stops] = remaining.reverse();

    console.log(`drive through ${args.length} towns`);
    console.log(`start in  ${start} `);
    console.log(`the distination is ${finish}`);
    console.log(`stopping ${stops.length} times in between`);
}

directions("Truckee", "Tahoe City", "Sunnyside", "Homewood", "Tahoma");