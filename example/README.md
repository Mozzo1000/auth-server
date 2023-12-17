# example
This is an example project that utilizes the `auth-server` and testing if it works.

## Usage
1. Set the env variable `AUTH_SECRET_KEY` to the same one as the `auth-server` is using.
2. Run `py app.py`
3. Test the routes
   1. `GET /` should work even when no token has been supplied.
   2. `GET /protected` should only work when a valid token from the `auth-server` has been providedf.