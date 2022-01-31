var topic = "JavaScript";
if (topic) {
    var topic = "React";
    console.log("block", topic);
}

console.log("global", topic);

var topic = "JavaScript";
if (topic) {
    let topic = "React";
    console.log("block", topic);
}

console.log("global", topic);

var div, container = document.getElementById("container");

for (var i = 0; i < 5; i++) {
    div = document.createElement("div");
    div.onclick = function() {
        alert("This is box #" + i);
    };
    container.appendChild(div);
}