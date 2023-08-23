const Router = require("koa-router");
const router = new Router();
const _v = require("./v");
const { pyNodeManager } = require("./pynode");

const validApiKey = require("./appwrite");



function isJsonString(str) {
  try {
    JSON.parse(str);
  } catch (e) {
    return false;
  }
  return true;
}

router.all("/app/api/:uuid/:key/:file", async (ctx, next) => {
   
  try {
    _v(`{r} -> api -> uuid ${ctx.params.uuid}`);
    if (!ctx.params.uuid) ctx.throw(500, "Missing UUID");
    if (!ctx.params.key) ctx.throw(500, "Missing Key");
    if (!ctx.params.file) ctx.throw(500, "Missing File Query");

    const _uuid = ctx.params.uuid;
    const _key = ctx.params.key;

    const _valid = await validApiKey(_uuid, _key);

    if(!_valid) {
      ctx.throw(500, "API Key invalid");
    }
    

    const _file = ctx.params.file;
    let _json = "";
    if (ctx.query.json) {
      try {
        //_json = JSON.stringify((ctx.query.json).replace(/[^a-zA-Z0-9 -]/g, ''));
        _json = JSON.parse(ctx.query.json);
      } catch (error) {
        ctx.throw(500, "JSON Formatting Error");
      }
    }

    const __pyN = await pyNodeManager(
      _file.toLowerCase().replace(/[^a-z]/g, ""),
      JSON.stringify(_json).substring(0, 2500)
    );

    let _pyN = await __pyN._process();
    if (_pyN) {
      ctx.body = _pyN;
    } else {
      ctx.throw(500, "Issue with PyNode");
    }
  } catch (error) {
    _v(error);
    ctx.body = {
      status: 500,
      message: error,
    };
  }
});



router.all("/app/api/blueprint/:token", async (ctx, next) => {
  try {
    _v(`{r} -> blueprint -> token ${ctx.params.token}`);
  } catch (error) {
    _v(error);
    ctx.body = {
      status: 500,
      message: error,
    };
  }
});

router.get("/docs", (ctx, next) => {
  ctx.status = 301;
  ctx.redirect("https://kbve.com/project/");
});

router.get("/login", async (ctx, next) => {});

module.exports = router;
