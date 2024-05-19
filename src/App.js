import logo from './logo.svg';
import './App.css';
import Editor from '@monaco-editor/react';
import { useState } from 'react';
import { useEffect } from 'react';

function App() {
  const [code, setCode] = useState('// code here');
  const [language, setLanguage] = useState('javascript');
  const submitCode = async () => {
    try {
      const response = await fetch('https://api.jdoodle.com/v1/execute', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          clientId: 'a4f1f2b6d
          clientSecret: 'f3b7e9e8d
          script: code,
          language: language,
          versionIndex: '0',
        }),
      });
      const data = await response.json();
      console.log(data);
    }
    catch (error) {
      console.error(error);
    }
  }


  useEffect(() => {
    // Update the document title using the browser API
    console.log(code);
  }, [code]);

  return (
    <div className="App">
      <button style={{ background: language === 'python' ? 'black' : 'white', color: language === 'python' ? 'white' : 'black'}} onClick={() => { setLanguage('python') }}>Python</button>
      <button style={{ background: language === 'java' ? 'black' : 'white', color: language === 'java' ? 'white' : 'black'}} onClick={() => { setLanguage('java') }}>Java</button>
      <button style={{ background: language === 'cpp' ? 'black' : 'white', color: language === 'cpp' ? 'white' : 'black'}} onClick={() => { setLanguage('cpp') }}>C++</button>
      
      <button onClick={() => {
        submitCode();
      }}>Run</button>
      <Editor onChange={(e) => {
        setCode(e);
      }} value={code}  height="90vh" theme="vs-dark" defaultLanguage="python" defaultValue="// some comment" />;
    </div>
  );
}

export default App;
