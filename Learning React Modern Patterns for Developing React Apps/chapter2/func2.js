const createCompliment = function(firstName, message) {
    return `${firstName}, ${message}`;
};

console.log(createCompliment("jigsaw", "hot"));

function logActivity(name = "Shane McConkey", activity = "skiing") {
    console.log(`${name} loves ${activity}`);
}

logActivity();


const defaultPerson = {
    name: {
        first: "Shane",
        last: "McConkey"
    },
    favActivity: "skiing"
};

function logActivity(person = defaultPerson) {
    console.log(`${person.name.first} loves ${person.favActivity}`);
};

logActivity();