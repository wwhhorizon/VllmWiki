# vllm-project/vllm#5302: [Bug]: speculative decoding with max-num-seqs <= 2 * num-speculative-tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#5302](https://github.com/vllm-project/vllm/issues/5302) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: speculative decoding with max-num-seqs <= 2 * num-speculative-tokens

### Issue 正文摘录

### Your current environment docker with vllm/vllm-openai:v0.4.3 （latest） ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model ./Qwen1.5-72B-Chat/ --max-model-len 24000 --tensor-parallel-size 8 --swap-space 20 --gpu-memory-utilization 0.9 --max-num-seqs 8(here change to 1) --speculative-model ./Qwen1.5-14B-Chat/ --num-speculative-tokens 4 --speculative-max-model-len 24000 --use-v2-block-manager when max-num-seqs == 1: it raises: INFO: ::1:42236 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__ return await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/fastapi/applications.py", line 1054, in __call__ await super().__call__(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/applications.py", line 123, in __call__ await self.middleware_stack(scope, rec...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: speculative decoding with max-num-seqs <= 2 * num-speculative-tokens bug;stale ### Your current environment docker with vllm/vllm-openai:v0.4.3 （latest） ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: qs <= 2 * num-speculative-tokens bug;stale ### Your current environment docker with vllm/vllm-openai:v0.4.3 （latest） ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model ./Qwen1.5-72B-Chat/ --max...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: t/ --num-speculative-tokens 4 --speculative-max-model-len 24000 --use-v2-block-manager when max-num-seqs == 1: it raises: INFO: ::1:42236 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model ./Qwen1.5-72B-Chat/ --max-model-len 24000 --tensor-parallel-size 8 --swap-space 20 --gpu-memory-utilization 0.9 --max-num-seqs 8(here change t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
