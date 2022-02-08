// fetch(`https://api.github.com/users/moonhighway`)
//   .then(response => response.json())
//   .then(console.log)
//   .catch(console.error);

// const fromData = new FormData();
// fromData.append("username", "moontahoe");
// fromData.append("fullname", "Alex Banks");
// fromData.append("avatar", 'imgFile');

// fetch("/create/user", {
//   method: "POST",
//   body: fromData
// })

fetch(`https://api.github.com/users/${login}`, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${token}`
  }
});

