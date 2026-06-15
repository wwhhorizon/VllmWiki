# vllm-project/vllm#29171: [Feature Request]: Add JSON response format to /health endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#29171](https://github.com/vllm-project/vllm/issues/29171) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request]: Add JSON response format to /health endpoint

### Issue 正文摘录

## Summary The `/health` endpoint currently returns an empty response body. Some monitoring tools and API clients expect JSON responses for health checks. **Current:** `HTTP 200` with empty body **Proposed:** `HTTP 200` with `{"status": "pass"}` ## Suggested Implementation (Backwards Compatible) Add optional `?format=json` query parameter: ```python @router.get("/health") async def health(raw_request: Request, format: str = None) -> Response: try: await engine_client(raw_request).check_health() if format == "json": return JSONResponse({"status": "pass"}, status_code=200) return Response(status_code=200) except EngineDeadError: if format == "json": return JSONResponse({"status": "fail"}, status_code=503) return Response(status_code=503) ``` Alternatively, a CLI flag like `--health-response-format json` could enable JSON globally. ## References - [IETF Health Check Response Format](https://datatracker.ietf.org/doc/html/draft-inadarei-api-health-check) - Related: #6073, #24897 Happy to contribute a PR if there's interest.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature Request]: Add JSON response format to /health endpoint stale ## Summary The `/health` endpoint currently returns an empty response body. Some monitoring tools and API clients expect JSON responses for health ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature Request]: Add JSON response format to /health endpoint stale ## Summary The `/health` endpoint currently returns an empty response body. Some monitoring tools and API clients expect JSON responses for health ch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ds Compatible) Add optional `?format=json` query parameter: ```python @router.get("/health") async def health(raw_request: Request, format: str = None) -> Response: try: await engine_client(raw_request).check_health() i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
