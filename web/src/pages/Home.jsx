import React from 'react'
import AuthService from '../services/auth.service';
import { Button } from 'flowbite-react';
import { Link, useNavigate } from 'react-router-dom';
import { useGoogleLogin } from '@react-oauth/google';

function Home() {
    let navigate = useNavigate();

    const login = useGoogleLogin({
      flow: 'auth-code',
      onSuccess: (codeResponse) => {
        console.log(codeResponse.code)
        var response = fetch(import.meta.env.VITE_API_URL + "/v1/authorize/google", { method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ "code": codeResponse.code }),
        }).then(response => {
          return response.json()
        }).then(response => {
          console.log(response)
          if (response.access_token) {
            localStorage.setItem("auth_user", JSON.stringify(response));
            navigate("/")
          }
        });
      },
    });

  return (
    <div>
        <h1>Home</h1>
        {AuthService.getCurrentUser() ? (
            <>
            <p>Logged in as {AuthService.getCurrentUser().name}</p>
            <Button color="failure" onClick={() => (AuthService.logout(), navigate("/"))}>Logout</Button>
            </>
        ):(
            <>
            <p>Not logged in</p>
            <Button as={Link} to="/login">Login</Button>
            </>
        )}
        <Button onClick={() => login()}>Sign in with Google</Button>

    </div>
  )
}

export default Home