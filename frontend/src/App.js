import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

function Notification(text){
  return (
    <div className='notification_wrapper'>
      <h4>{text}</h4>
    </div>
  )
}

function Files() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    async function fetchFiles() {
      const response = await fetch("/getFiles", {
        method: "POST"
      });

      if (response.status == 200) {
        const data = await response.json();
        setFiles(data);
      }
    }

    fetchFiles();
  }, []); // Пустой массив зависимостей гарантирует, что запрос выполнится только один раз

  const deleteFile = (path) => {
    fetch("/deleteFile/" + path, {
      method: "DELETE"
    }
    ).then(() => {
      let files_copy = [...files];

      for (const file in files_copy) {
        if (files_copy.at(file).path === path) {
          files_copy.splice(file, 1);

          break;
        }
      }
      setFiles(files_copy)
    })
  }

  const sendFile = (event) => {
    event.preventDefault()

    const input = document.querySelector(".file_input");
    const files = input.files;

    if (!input || !files.length) {
      return;
    }

    const formData = new FormData();
    for (const file of files) {
      formData.append('file', file);
    }

    fetch("uploadFile", {
      method: "POST",
      body: formData
    }).then(async response => {
      if (response.status === 200) {
        let file_atr = await response.json();
        setFiles(prevFiles => [
          ...prevFiles,
          { path: file_atr.path, filename: file_atr.filename }
        ]);
      }
    }).catch(error => {
      console.error('Error:', error);
      alert('Error uploading file.');
    });
  }

  return (
    <div className="files_input">
      <div className="files_wrapper">
        {files.map((file, index) => (
          <div className="item">
            <a href={file["path"]}>{file["filename"]}</a>

            <button
              className='deleteFile fas fa-trash-alt'
              onClick={() => { deleteFile(file.path) }}
            >
            </button>
          </div>
        ))}
      </div>
      {Notification("Notification (1)")}
      <div className="Form">
        <form>
          <div className="file_input_wrapper">
            <input
              type="file"
              className="file_input"
              multiple
              required
            ></input>
          </div>
          <button className="send_file"
            onClick={sendFile}
            type="button">
            Отправить
          </button>
        </form>
      </div>
    </div>
  );
}

async function checkAuth(login, pwd) {
  let response;
  if (!isNaN(login) || !isNaN(pwd)) {
    response = await fetch("login", {
      method: "POST",
      headers: {
        "Content-type": "application/json"
      },
      body: JSON.stringify({
        "login": login,
        "password": pwd
      })
    })
  }
  else {
    response = await fetch("login", {
      method: "GET"
    })
  }

  if (response.status == 200) {
    return true;
  }
  return false;
}

function validateAndGetAuthData(){
  const login_input = document.querySelector(".login");
  const pwd_input = document.querySelector(".pwd");

  const login = login_input.value;
  const pwd = pwd_input.value;

  if (login === "" || pwd === "") {
    if (login_input.value === "") {
      login_input.style.color = "red";
    }
    if (pwd_input.value === "") {
      pwd_input.style.color = "red";
    }
    return;
  }

  login_input.style.color = "black";
  pwd_input.style.color = "black";
  return [login, pwd]
}

async function register() {
  const pwd_retype_input = document.querySelector(".pwdRetype");
  login, password = validateAndGetAuthData()
  if (password !== pwd_retype_input){
    return;
  }
  
  

}

async function login_confirm() {
  
  const status = await checkAuth(login, pwd);
  if (!status) {
    alert("Не верный логин или пароль")
  }
  return status;
}

function Login_form() {
  const [renderFiles, setRenderFiles] = useState(false);
  const [registration, setIsRegistration] = useState(false);

  useEffect(() => {
    const fetchAuthStatus = async () => {
      const status = await checkAuth(NaN, NaN);
      setRenderFiles(status);
    };

    fetchAuthStatus();
  }, []);

  return (
    <div>
      {!renderFiles && (
        <div className="login_wrapper">

          <h3>{registration ? "Регистрация" : "Вход"}</h3>

          <div className="inputs">
            <div className="input_wrapper">
              <p>Логин: </p>
              <input
                className="login"
                placeholder='type login here'
                type="email" />
            </div>

            <div className="input_wrapper">
              <p>Пароль: </p>
              <input placeholder='type password here'
                className="pwd"
                type="password" />
            </div>

            {registration ? <div className="input_wrapper">
              <p>Повтор пароля: </p>
              <input placeholder='retype password here'
                className="pwd pwdRetype"
                type="password" />
            </div> : ""}
          </div>

          <button className="submit btn" onClick={async () => {
            const status = await login_confirm();
            setRenderFiles(status);
          }}>Войти</button>

          <button
            className="btn mt-4 text-sm text-blue-600 hover:underline"
            onClick={() => { setIsRegistration(!registration) }}
          >

            {registration ? "Есть аккаунт?" : "Регистрация"}
          </button>
        </div>
      )}
      {renderFiles && <Files />}
    </div>
  );
}

function Header() {
  return (
    <div className="header_wrapper">
      <div className="header">
        <div className="item">
          <p>data storage</p>
        </div>

        <div className="item">
          <a href='/about'>о проекте</a>
        </div>

        <div className="item">
          <a href='/'>profile</a>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <div>
      <Header />
      <div className="main">
        <Login_form />
      </div>
    </div>
  );
}

export default App;