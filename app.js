//?         [lolPython]
//*         [IMPORT]
const Koa = require("koa");
const parser = require("koa-bodyparser");
const router = require("./router");
const _v = require("./v");
const App = new Koa();
const port = 5000;

App.use(parser())
  .use(router.routes())
  .use(async (ctx, next) => {
    try {
      await next();
    } catch (err) {
      ctx.status = err.statusCode || err.status || 500;
      ctx.body = {
        message: err.message,
      };
    }
  })
  .listen(port, () => {
    _v(`Launching at http://127.0.0.1:${port}/ 🚀`);
  });
