import React, { useReducer } from "react";

// function Checkbox() {
//   const [checked, setChecked] = useState(false);

//   function toggle() {
//     setChecked(checked => !checked);
//   }

//   return (
//     <>
//       <input type="checkbox" value={checked} onChange={toggle} />
//       {checked ? "checked" : "not checked"}
//     </>
//   );
// }


function Numbers() {
  const [number, setNumber] = useReducer(
    (number, newNumber) => number + newNumber,
    0
  );

  return <h1 onClick={() => setNumber(1)}>{number}</h1>;
}

export default function App() {
  return <Numbers />;
}
