//?         [Cloud Function -> LoL Python]
//*         [IMPORT]
const axios = require("axios").default;

module.exports = async function (req, res) {
  let champion = "";

  if (req.payload) {
    try {
      champion = JSON.parse(req.payload).champion;
    } catch (error) {
      throw new Error(`Missing Champion Variable`);
    }
  }

  const response = await axios.get(
    `https://lolpython.kbve.com/api/v1/champion/${champion}`
  );

  if (response.status !== 200) {
    throw new Error(`Status code: ${response.status}, Data: ${response.data}`);
  }

  const dataJson = response.data;
  let _result = dataJson;
  try {
    _result = JSON.parse(_result);
  } catch (error) {}

  res.json({
    data: _result,
  });
};
