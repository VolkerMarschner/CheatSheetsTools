# Axios Cheatsheet - HTTP Methoden & Authentifizierung

## Installation

```bash
npm install axios
```

```javascript
import axios from 'axios';
// oder
const axios = require('axios');
```

## HTTP Methoden

### GET Request
```javascript
// Einfacher GET
const response = await axios.get('https://api.example.com/users');

// GET mit Query Parametern
const response = await axios.get('https://api.example.com/users', {
  params: {
    page: 1,
    limit: 10
  }
});

// GET mit Headern
const response = await axios.get('https://api.example.com/users', {
  headers: {
    'Accept': 'application/json'
  }
});
```

### POST Request
```javascript
// POST mit JSON Body
const response = await axios.post('https://api.example.com/users', {
  name: 'John Doe',
  email: 'john@example.com'
});

// POST mit Custom Headers
const response = await axios.post('https://api.example.com/users', 
  { name: 'John', email: 'john@example.com' },
  {
    headers: {
      'Content-Type': 'application/json'
    }
  }
);

// POST mit FormData
const formData = new FormData();
formData.append('file', fileInput);
const response = await axios.post('https://api.example.com/upload', formData, {
  headers: {
    'Content-Type': 'multipart/form-data'
  }
});
```

### PUT Request
```javascript
// PUT für komplette Aktualisierung
const response = await axios.put('https://api.example.com/users/123', {
  id: 123,
  name: 'John Updated',
  email: 'john.updated@example.com'
});
```

### PATCH Request
```javascript
// PATCH für partielle Aktualisierung
const response = await axios.patch('https://api.example.com/users/123', {
  name: 'New Name Only'
});
```

### DELETE Request
```javascript
// DELETE Request
const response = await axios.delete('https://api.example.com/users/123');

// DELETE mit Body (falls nötig)
const response = await axios.delete('https://api.example.com/users/123', {
  data: { reason: 'User requested deletion' }
});
```

## Authentifizierung

### Bearer Token (JWT)
```javascript
// Mit Authorization Header
const response = await axios.get('https://api.example.com/protected', {
  headers: {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
  }
});

// Global für alle Requests setzen
axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
```

### API Key (Header)
```javascript
// API Key im Header
const response = await axios.get('https://api.example.com/data', {
  headers: {
    'X-API-Key': 'your-api-key-here',
    'Authorization': 'ApiKey your-api-key'
  }
});
```

### API Key (Query Parameter)
```javascript
// API Key als Query Parameter
const response = await axios.get('https://api.example.com/data', {
  params: {
    api_key: 'your-api-key-here',
    key: 'your-api-key-here'
  }
});
```

### Basic Authentication
```javascript
// Basic Auth mit Username/Password
const response = await axios.get('https://api.example.com/data', {
  auth: {
    username: 'your-username',
    password: 'your-password'
  }
});

// Oder manuell kodiert
const credentials = btoa('username:password');
const response = await axios.get('https://api.example.com/data', {
  headers: {
    'Authorization': `Basic ${credentials}`
  }
});
```

### OAuth 2.0
```javascript
// OAuth Bearer Token
const response = await axios.get('https://api.example.com/user', {
  headers: {
    'Authorization': 'Bearer ' + accessToken
  }
});

// Mit Refresh Token
const refreshResponse = await axios.post('https://auth.example.com/refresh', {
  refresh_token: refreshToken,
  grant_type: 'refresh_token'
});
```

### Custom Auth Headers
```javascript
// Verschiedene Custom Auth Patterns
const response = await axios.get('https://api.example.com/data', {
  headers: {
    'X-Auth-Token': 'your-token',
    'X-API-Secret': 'your-secret',
    'Authorization': 'Custom your-custom-auth'
  }
});
```

## Axios Instanzen mit Standard-Konfiguration

### Basis-Instanz
```javascript
const apiClient = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
  }
});

// Verwendung
const response = await apiClient.get('/users');
const createUser = await apiClient.post('/users', userData);
```

### Interceptors für automatische Auth
```javascript
// Request Interceptor für automatisches Token hinzufügen
axios.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => Promise.reject(error)
);

// Response Interceptor für Token Refresh
axios.interceptors.response.use(
  response => response,
  async error => {
    if (error.response?.status === 401) {
      // Token abgelaufen, refresh versuchen
      const newToken = await refreshToken();
      error.config.headers.Authorization = `Bearer ${newToken}`;
      return axios.request(error.config);
    }
    return Promise.reject(error);
  }
);
```

## Error Handling

```javascript
try {
  const response = await axios.get('https://api.example.com/data');
  console.log(response.data);
} catch (error) {
  if (error.response) {
    // Server antwortete mit Error Status
    console.log('Status:', error.response.status);
    console.log('Data:', error.response.data);
  } else if (error.request) {
    // Request wurde gesendet, keine Antwort erhalten
    console.log('No response:', error.request);
  } else {
    // Anderer Fehler
    console.log('Error:', error.message);
  }
}
```

## Nützliche Tipps

### Timeout setzen
```javascript
const response = await axios.get('https://api.example.com/slow', {
  timeout: 10000 // 10 Sekunden
});
```

### Response nur Data extrahieren
```javascript
const { data } = await axios.get('https://api.example.com/users');
// Direkt data verwenden statt response.data
```

### Gleichzeitige Requests
```javascript
const [users, posts, comments] = await Promise.all([
  axios.get('/users'),
  axios.get('/posts'),
  axios.get('/comments')
]);
```
