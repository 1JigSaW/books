const colors = [
    {
        id: '-xekare',
        title: "rad red",
        rating: 3
    },
    {
        id: '-jbwsof',
        title: "big blue",
        rating: 2
    },
    {
        id: '-prigbj',
        title: "grizzly grey",
        rating: 5
    },
    {
        id: '-ryhbhsl',
        title: "banana",
        rating: 1
    }
]

const hashColors = colors.reduce(
    (hash, {id, title, rating}) => {
        hash[id] = {title, rating}
        return hash
    },
    {}
)

console.log(hashColors)

const colors2 = ["red", "red", "green", "blue", "green"];

const distinctColors = colors2.reduce(
    (distinct, color) =>
        (distinct.indexOf(color) !== -1) ?
            distinct :
            [...distinct, color],
    []
)

console.log(distinctColors)