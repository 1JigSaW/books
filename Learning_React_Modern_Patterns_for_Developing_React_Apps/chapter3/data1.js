const schools = ["Yorktown", "Washington", "Wakefield"]
console.log(schools.join(", "));

const wSchools = schools.filter(school => school[0] === "W");
console.log(wSchools);

const cutSchool = (cut, list) => list.filter(school => school !== cut);
console.log(cutSchool("Washington", schools).join(", "));

console.log(schools.join("\n"));

const highSchools = schools.map(school => `${school} High School`);
console.log(highSchools.join("\n"));
console.log(schools.join("\n"));

const highSchools2 = schools.map(school => ({ name: school }));
console.log(highSchools);

let schools2 = [
	{ name: "Yorktown" },
	{ name: "Stanford" },
	{ name: "Washington" }
]

const editName = (oldName, name, arr) =>
	arr.map(item => {
		if (item.name === oldName) {
			return {
				...item,
				name
			};
		} else {
			return item;
	}
});

let updateSchools = editName("Stanford", "HB Woodlawn", schools2);
console.log(updateSchools[1]);
console.log(schools2[1]);

const editName2 = (oldName, name, arr) =>
	arr.map(item => (item.name === oldName ? { ...item, name } : item));

const schools3 = {
	Yorktown: 10,
	Washington: 2,
	Wakefield: 5
};

const schoolArray = Object.keys(schools3).map(key => ({
	name: key,
	wins: schools3[key]
}));

console.log(schoolArray);

const ages = [21, 18, 42, 40, 64, 63, 34];
const maxAge = ages.reduce((max, age) => {
	console.log(`${age} > ${max} = ${age > max}`);
	if (age > max) {
		return age;
	} else {
		return max;
	}
}, 0)

console.log("maxAge", maxAge);

const max = ages.reduce((max, value) => (value > max ? value: max), 0)