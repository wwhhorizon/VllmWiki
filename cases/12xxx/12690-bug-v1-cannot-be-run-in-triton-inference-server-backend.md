# vllm-project/vllm#12690: [Bug]: V1 cannot be run in Triton Inference Server Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#12690](https://github.com/vllm-project/vllm/issues/12690) |
| 状态 | closed |
| 标签 | bug;v1 |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 cannot be run in Triton Inference Server Backend

### Issue 正文摘录

### Your current environment . NA ### Model Input Dumps _No response_ ### 🐛 Describe the bug When attempting to use the `VLLM_USE_V1=1` feature in triton inference server backend the models fail to start up due to signal handling being attempted outside of the main thread. The following error occurs in startup. ```text model.py:244] "[vllm] Failed to start engine: signal only works in main thread of the main interpreter" pb_stub.cc:366] "Failed to initialize Python stub: ValueError: signal only works in main thread of the main interpreter At: /usr/lib/python3.12/signal.py(58): signal /app/.venv/lib/python3.12/site-packages/vllm/v1/engine/core_client.py(160): __init__ /app/.venv/lib/python3.12/site-packages/vllm/v1/engine/core_client.py(252): __init__ /app/.venv/lib/python3.12/site-packages/vllm/v1/engine/core_client.py(53): make_client /app/.venv/lib/python3.12/site-packages/vllm/v1/engine/async_llm.py(79): __init__ /app/.venv/lib/python3.12/site-packages/vllm/v1/engine/async_llm.py(107): from_engine_args /app/.venv/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py(162): build_async_engine_client_from_engine_args /usr/lib/python3.12/contextlib.py(211): __aenter__...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: V1 cannot be run in Triton Inference Server Backend bug;v1 ### Your current environment . NA ### Model Input Dumps _No response_ ### 🐛 Describe the bug When attempting to use the `VLLM_USE_V1=1` feature in triton...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py(162): build_async_engine_client_from_engine_args /usr/lib/python3.12/contextlib.py(211): __aenter__ /opt/tritonserver/backends/vllm/model.py(289): _run_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ad? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Inference Server Backend bug;v1 ### Your current environment . NA ### Model Input Dumps _No response_ ### 🐛 Describe the bug When attempting to use the `VLLM_USE_V1=1` feature in triton inference server backend the mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
