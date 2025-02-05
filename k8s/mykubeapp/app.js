const express = require('express');
const app = express();
const PORT = 5002;

app.get('/', (req, res) => {
	res.send('Hello, World!! This is a node.js app running on port 5002 after update');
});

app.listen(PORT, () => {
	console.log(`Server is running on http://localhost:${PORT}`);
}); 
