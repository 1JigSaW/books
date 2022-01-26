function logCompliment() {
    console.log("You're doing great!");
};

logCompliment();

const logCompliment1 = function() {
    console.log("You're doing great!")
};

logCompliment1();

const logCompliment2 = function(firstName) {
    console.log(`You're doing great, ${firstName}`)
};

logCompliment2("jigsaw");

const logCompliment3 = function(firstName, message) {
    console.log(`${firstName}, ${message}`)
};

logCompliment3("jigsaw", "aasdasdasd");