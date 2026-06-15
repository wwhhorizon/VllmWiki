# vllm-project/vllm#18431: [Bug]: Engine stuck with requests are blocked, running/waiting request count and KV cache usage remain constant.

| 字段 | 值 |
| --- | --- |
| Issue | [#18431](https://github.com/vllm-project/vllm/issues/18431) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine stuck with requests are blocked, running/waiting request count and KV cache usage remain constant.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running Qwen2.5-32B-Instruct model using vLLM in a Docker container. The /health API returns a 200 OK status, indicating the server is running, but incoming requests are getting stuck. The running request count and GPU KV cache utilization remain constant, suggesting the engine is not processing new requests or clearing completed ones. This issue persists even though KV cache utilization peaks at around 35%, Set up a vLLM container with the following command: ``` docker run -d \ --gpus '"device=6,7"' \ -v /mnt/models/:/workspace/models \ -p 8004:8000 \ --ipc=host \ vllm/vllm-openai:v0.8.5.post1 \ --model /workspace/models/Qwen2.5-32B-Instruct \ --port 8000 \ --tensor-parallel-size 2 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --max-model-len 32768 \ --guided-decoding-backend xgrammar \ --served-model-name Qwen2.5-32B-Instruct \ --gpu-memory-utilization 0.92 ``` I suspect this could be related to worker processes stalling, a request queue blockage, or a model-specific issue with Qwen2.5-32B-Instruct. Questions for Help 1. How can I debug this further when the health API indicates the server is fine but requests a...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Engine stuck with requests are blocked, running/waiting request count and KV cache usage remain constant. bug;stale ### Your current environment ### 🐛 Describe the bug I'm running Qwen2.5-32B-Instruct model using...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Describe the bug I'm running Qwen2.5-32B-Instruct model using vLLM in a Docker container. The /health API returns a 200 OK status, indicating the server is running, but incoming requests are getting stuck. The running r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ale ### Your current environment ### 🐛 Describe the bug I'm running Qwen2.5-32B-Instruct model using vLLM in a Docker container. The /health API returns a 200 OK status, indicating the server is running, but incoming re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -tool-call-parser hermes \ --max-model-len 32768 \ --guided-decoding-backend xgrammar \ --served-model-name Qwen2.5-32B-Instruct \ --gpu-memory-utilization 0.92 ``` I suspect this could be related to worker processes st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cy? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
