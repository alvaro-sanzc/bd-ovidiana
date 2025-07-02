const axios = require('axios');
const qs = require('qs'); // npm install qs

const endpoint = process.env.SPARQL_ENDPOINT;

async function executeQuery(query) {
  try {
    const response = await axios.post(
      endpoint,
      qs.stringify({ query }), // 👈 transforma a formato x-www-form-urlencoded
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Accept': 'application/sparql-results+json',
        }
      }
    );
    return response.data;
  } catch (err) {
    console.error('Error al consultar SPARQL:', err.message);
    throw err;
  }
}

module.exports = { executeQuery };
