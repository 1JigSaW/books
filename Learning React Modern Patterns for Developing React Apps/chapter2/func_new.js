const lordify = function(firstname) {
    return `${firstname} of Centerbury`;
};

console.log(lordify("Lary"));
console.log(lordify("Dale"));

const lordify2 = firstname => `${firstname} of Centerbury`;

console.log(lordify2("Dale"));

const lordify3 = (firstname, land) => `${firstname} of ${land}`;

console.log(lordify3('asd', 'asdsad'));

const lordify4 = (firstname, land) => {
    if (!firstname) {
        throw new Error("A firstname is required to lordify");
    }

    if (!land) {
        throw new Error("A lord must have a land");
    }

    return `${firstname} of ${land}`;
};

console.log(lordify4("Kelly", "Sanoma"));
console.log(lordify4("Kelly"));