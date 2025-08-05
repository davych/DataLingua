import axios from 'axios';

const http = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 1000000,
});

export default http;