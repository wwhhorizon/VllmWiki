# vllm-project/vllm#6970: [Feature]: Add security scheme to server

| 字段 | 值 |
| --- | --- |
| Issue | [#6970](https://github.com/vllm-project/vllm/issues/6970) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add security scheme to server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi there! I'd be happy to submit a PR for this, but wanted to open an issue for discussion first. The current method for authenticating with the server API key is undocumented in the auto-generated `openapi.json`. This breaks the Swagger `/docs` page because there is no functionality to login or otherwise provide the authorization header. As a solution, FastAPI has some out-of-the-box functionality for adding a security scheme (namely `fastapi.security.HTTPBearer`) which, once included in an app/router/route, is automatically applied to the OpenAPI spec. This fixes the Swagger docs as well. My suggested approach is: - Create a function which receives the credentials and validates them - Create two `APIRouter`s - One which never has authentication applied to it (e.g. `/health`) - Another which _may_ have authentication applied to it, depending on if `VLLM_API_KEY` or `--api_key` are provided - Apply these routers to the existing routes. Based on the existing code [here](https://github.com/g-parki/vllm/blob/40c27a7cbb496ede63da9d636c07a1f315fd36e1/vllm/entrypoints/openai/api_server.py#L188-L200) the authentication is only applied to `/v1/` rou...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add security scheme to server feature request;stale ### 🚀 The feature, motivation and pitch Hi there! I'd be happy to submit a PR for this, but wanted to open an issue for discussion first. The current method...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: me (namely `fastapi.security.HTTPBearer`) which, once included in an app/router/route, is automatically applied to the OpenAPI spec. This fixes the Swagger docs as well. My suggested approach is: - Create a function whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
