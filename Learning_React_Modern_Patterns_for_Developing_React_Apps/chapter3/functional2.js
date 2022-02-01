// imperative

const string = "Restaurants in Hanalei";
let urlFriendly = "";

for (var i = 0; i < string.length; i++) {
	if (string[i] === " ") {
		urlFriendly += "-";
	} else {
		urlFriendly += string[i];
	}
}

console.log(urlFriendly);

// declarative

const string1 = "Restaurants in Hanalei";
let urlFriendly1 = string1.replace(/ /g, "-");
console.log(urlFriendly1);

const { render } = ReactDOM;

const Welcome = () => (
	<div id='welcome'>
		<h1>Hello World</h1>
	</div>
);

render(<Welcome />, document.getElementById("target"))