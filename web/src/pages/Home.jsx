import React from 'react'
import AuthService from '../services/auth.service';
import { Button } from 'flowbite-react';
import { Link, useNavigate } from 'react-router-dom';

function Home() {
  let navigate = useNavigate();

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
            <Link to="/login" style={{display: 'inline-block'}}>
              <Button>Login</Button>
            </Link>

            </>
        )}
    </div>
  )
}

export default Home