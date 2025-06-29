import { useState } from 'react';
import './App.css';

function App() {
const [inputs, setInputs] = useState({});

  const host = import.meta.env.VITE_BACKEND_URL;
  
  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({ ...values, [name]: value }));
  };

  const handleSubmit = async(event) => {
    event.preventDefault();
     const res = await fetch(`${host}/form`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: inputs.name, age: inputs.age }),
    })

    console.log(res)
  };
  return (
   <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" name="name" value={inputs.name || ''} onChange={handleChange} />
      </label>
      <label>
        Age:
        <input type="number" name="age" value={inputs.age || ''} onChange={handleChange} />
      </label>
      <button type="submit">Submit</button>
    </form>
  )
}

export default App
