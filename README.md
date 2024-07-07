<h1 align="center">
  <br>
  <a href="https://github.com/Mozzo1000/auth-server">
    <img src="assets/logo.svg" height="120px" width="120px"/>
    </a>
  <br>
  Auth Server
  <br>
</h1>

<h4 align="center">A JWT token authentication and user management server.</h4>
<p align="center">
  <a href="https://github.com/Mozzo1000/auth-server/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="Apache 2.0 License">
  </a>
</p>

## About the project
`Auth Server` provides you with an opinionated authentication server meant to be able to integrate with numerous different projects. With the easy to use endpoints you will be able to handle login, registration, verification (email) and OAuth login without building your own backend for authentication.

### Why?
This project started out when I noticied I rebuilt the same functionality over and over again across different projects. With time, these projects slowly drifted away in terms of functionality and how the authentication flow worked, leaving me with harder to maintain projects. `Auth Server` is a combination of all those efforts so I can easily get the same authentication functionality across all my projects just by spinning up a docker container.

## Usage

### Run with docker
Run `docker compose up` to spin up the API and accompanying postgres database.
By default the database is configured to be listening on port `5433` and the API on port `5001`. This can be changed in the `docker-compose.yml` file.

### Examples
You can find example projects that utilize the functionality of `Auth Server` in the [example](example) folder.

## License
`Auth Server` is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.