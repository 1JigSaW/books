const person = (firstName, lastName) =>
    ({
        first: firstName,
        last: lastName
    })
console.log(person("Brad", "Janson"));

const tahoe = {
    mountains: ["Freel", "Rose", "Tallac", "Robicon", "Silver"],
    print: function(delay = 1000) {
        setTimeout(() => {
            console.log(this.mountains.join(", "));
        }, delay);
    }
};

tahoe.print();
console.log(this);