const sandwich = {
    bread: "dutch crunch",
    meat: "tuna",
    cheese: "swiss",
    toppings: ["lettuce", "tomato", "mustard"]
};

// const { bread, meat } = sandwich;
// console.log(bread, meat);

let { bread, meat } = sandwich;
bread = "adsjhfgsd";
meat = "adasdasd";
console.log(bread);
console.log(meat);

console.log(sandwich.bread, sandwich.meat);

const lordify = regularPerson => {
    console.log(`${regularPerson.firstName} od Cenurabry`);
};

const regularPerson = {
    firstName: "Bill",
    lastName: "Wilson",
    spouse: {
        firstName: "Phil",
        lastName: "Wilson"
    }
};

const lordify2 = ({ spouse: {firstName}}) => {
    console.log(`${regularPerson.firstName} od Cenurabry`);
};

lordify2(regularPerson);

