import React from 'react'
import { useGoogleLogin } from '@react-oauth/google';
import { FaGoogle } from "react-icons/fa";
import { useNavigate } from 'react-router-dom';
import { Button } from 'flowbite-react';
import AuthService from '../services/auth.service';

function GoogleLoginButton(props) {
    let navigate = useNavigate();

    const handleLoginGoogle = useGoogleLogin({
        flow: 'auth-code',
        ux_mode: 'popup',
        onSuccess: (codeResponse) => {
            console.log(codeResponse.code)
            AuthService.loginGoogle(codeResponse.code).then(
            response => {
                navigate("/")
            },
            error => {
                console.log(error.response)
            }
        )
        },
    });

    return (
        <Button color="light" onClick={() => handleLoginGoogle()}><FaGoogle className="mr-2 h-5 w-5" />Sign in with Google</Button>
    )
}

export default GoogleLoginButton