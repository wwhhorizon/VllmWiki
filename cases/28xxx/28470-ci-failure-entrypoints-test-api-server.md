# vllm-project/vllm#28470: [CI Failure]: Entrypoints Test (API Server)

| 字段 | 值 |
| --- | --- |
| Issue | [#28470](https://github.com/vllm-project/vllm/issues/28470) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Entrypoints Test (API Server)

### Issue 正文摘录

### Name of failing test `tests/entrypoints/openai/test_response_api_with_harmony.py::test_function_call_with_previous_input_messages` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test - Unable to repro locally - Failure in CI (https://buildkite.com/vllm/ci/builds/38411#019a720f-6a70-4c10-86eb-146aa029d6ef) ```bash [2025-11-11T09:29:32Z] entrypoints/openai/test_response_api_with_harmony.py::test_function_call_with_previous_input_messages[openai/gpt-oss-20b] (APIServer pid=10560) INFO 11-11 01:29:32 [gptoss_reasoning_parser.py:162] Builtin_tool_list: ['python'] -- | [2025-11-11T09:29:32Z] (APIServer pid=10560) INFO: 127.0.0.1:38432 - "POST /v1/responses HTTP/1.1" 200 OK | [2025-11-11T09:29:32Z] [2025-11-11 01:29:32] INFO _client.py:1786: HTTP Request: POST http://127.0.0.1:40217/v1/responses "HTTP/1.1 200 OK" | [2025-11-11T09:29:33Z] (APIServer pid=10560) ERROR: Exception in ASGI application | [2025-11-11T09:29:33Z] (APIServer pid=10560) Traceback (most recent call last): | [2025-11-11T09:29:33Z] (APIServer pid=10560) File "/usr/local/lib/python3.12/dist-packages/starlet...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: r pid=10560) \| File "/usr/local/lib/python3.12/dist-packages/anyio/_backends/_asyncio.py", line 763, in __aexit__ | [2025-11-11T09:29:33Z] (APIServer pid=10560) \| raise BaseExceptionGroup( | [2025-11-11T09:29:33Z] (AP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Entrypoints Test (API Server) ci-failure ### Name of failing test `tests/entrypoints/openai/test_response_api_with_harmony.py::test_function_call_with_previous_input_messages` ### Basic information - [x]
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: armony.py::test_function_call_with_previous_input_messages` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: vious_input_messages` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test - Unable to repro locally - Failur...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: =10560) \| File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 714, in __call__ | [2025-11-11T09:29:33Z] (APIServer pid=10560) \| await self.middleware_stack(scope, receive, send) | [2025-11-11T09:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
