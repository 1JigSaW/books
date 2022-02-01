var log = function(message) {
	console.log(message);
};

log("In Javascript, functions are variables");

const log3 = message => {
	console.log(message);
};

const obj = {
	message: "alallalal",
	log2(message) {
		console.log(message);
	}
};

obj.log2(obj.message);

const messages = [
	"They array",
	message => console.log(message),
	"like variables",
	message => console.log(message)
];
messages[1](messages[0]);
messages[3](messages[2]);

const insideFn = logger => {
	logger("They can be sent to other functions as arguments");
};

insideFn(message => console.log(message));

const createScream = function(logger) {
	return function(message) {
		logger(message.toUpperCase() + "!!!");
	};
};

const scream = createScream(message => console.log(message));
scream("asdasdas");
scream("asdfasfasfdasd");
scream("aljkdhaslkdhasdhaslkhd");