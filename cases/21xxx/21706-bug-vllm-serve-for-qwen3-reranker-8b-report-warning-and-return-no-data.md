# vllm-project/vllm#21706: [Bug]: vllm serve for Qwen3-Reranker-8B, report warning and return no data.

| 字段 | 值 |
| --- | --- |
| Issue | [#21706](https://github.com/vllm-project/vllm/issues/21706) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm serve for Qwen3-Reranker-8B, report warning and return no data.

### Issue 正文摘录

### Your current environment vLLM API server version 0.10.1.dev73+g7728dd77b ### 🐛 Describe the bug Running cmd: VLLM_CPU_OMP_THREADS_BIND="36-47" VLLM_USE_MODELSCOPE=1 VLLM_USE_V1=1 VLLM_CPU_KVCACHE_SPACE=32 vllm serve ~/Qwen3-Reranker-8B/ --served-model-name Qwen3-Reranker-8B --port 8080 --trust-remote-code ``` INFO: Started server process [5675] INFO: Waiting for application startup. INFO: Application startup complete. INFO: 10.112.41.17:10649 - "GET /v1/models HTTP/1.1" 200 OK WARNING 07-28 04:05:12 [logger.py:71] To indicate that the rerank API is not part of the standard OpenAI API, we have located it at `/rerank`. Please update your client accordingly. (Note: Conforms to JinaAI rerank API) INFO: 10.112.41.17:10900 - "POST /v1/rerank HTTP/1.1" 200 OK INFO: 10.112.41.17:10941 - "POST /v1/rerank HTTP/1.1" 200 OK INFO: 10.112.41.17:10950 - "POST /v1/rerank HTTP/1.1" 200 OK ``` VLLM reports the warning, and returns no data of reranked result. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of fr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm serve for Qwen3-Reranker-8B, report warning and return no data. bug ### Your current environment vLLM API server version 0.10.1.dev73+g7728dd77b ### 🐛 Describe the bug Running cmd: VLLM_CPU_OMP_THREADS_BIND=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng and return no data. bug ### Your current environment vLLM API server version 0.10.1.dev73+g7728dd77b ### 🐛 Describe the bug Running cmd: VLLM_CPU_OMP_THREADS_BIND="36-47" VLLM_USE_MODELSCOPE=1 VLLM_USE_V1=1 VLLM_CPU_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: trust-remote-code ``` INFO: Started server process [5675] INFO: Waiting for application startup. INFO: Application startup complete. INFO: 10.112.41.17:10649 - "GET /v1/models HTTP/1.1" 200 OK WARNING 07-28 04:05:12 [lo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
