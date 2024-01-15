import './App.css'
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [result, setResult] = useState('');

    const executeScript = async () => {
        try {
            const response = await axios.post('http://localhost:5000/execute-script', {
                index: 'ams-nitahs',
                addon: 'your_addon_data',
            });
            setResult(response.data.result);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1 className='font-bold p-4'>ReactJS App</h1>
            <button className=' rounded-lg bg-green-400' onClick={executeScript}>Execute</button>
            <div>Result: {result}</div>
        </div>
    );
};

export default App;
