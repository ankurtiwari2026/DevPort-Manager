import React from 'react';
import { Container, Button } from 'react-bootstrap';

const Login = () => {
  const handleGitHubLogin = () => {
    window.location.href = 'http://localhost:8000/auth/login/github';
  };

  return (
    <Container>
      <h2>Login</h2>
      <Button variant="dark" onClick={handleGitHubLogin}>
        Login with GitHub
      </Button>
    </Container>
  );
};

export default Login;