# vllm-project/vllm#26555: [Bug]: Highly concurrent calls to the vllm service can cause graphics card crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#26555](https://github.com/vllm-project/vllm/issues/26555) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Highly concurrent calls to the vllm service can cause graphics card crashes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Implementation steps: First, use vllm to deploy a large Qwen3-32B model service in a Docker container. Two 4090 GPUs are used. The command is: nohup vllm serve Qwen3-32B --dtype auto --api-key token-abc123 --tensor-parallel-size 2 --disable-log-stats --gpu-memory-utilization 0.8 --max-num-batched-tokens 8192 --port 8888 > llm_server_928.log 2>&1 & Deploy two FastAPI services for sentiment analysis and automatic labeling. Both tasks involve short text generation. Both services call the large model service deployed by vllm. After a period of high concurrency, the second GPU may crash, displaying an error. Initially, I thought it was a hardware issue with the GPU, but each time the issue occurs, the GPU recovers after restarting the server, making it difficult to determine if the issue is with the GPU. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n steps: First, use vllm to deploy a large Qwen3-32B model service in a Docker container. Two 4090 GPUs are used. The command is: nohup vllm serve Qwen3-32B --dtype auto --api-key token-abc123 --tensor-parallel-size 2 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: PU. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: scribe the bug Implementation steps: First, use vllm to deploy a large Qwen3-32B model service in a Docker container. Two 4090 GPUs are used. The command is: nohup vllm serve Qwen3-32B --dtype auto --api-key token-abc12...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: concurrent calls to the vllm service can cause graphics card crashes bug;stale ### Your current environment ### 🐛 Describe the bug Implementation steps: First, use vllm to deploy a large Qwen3-32B model service in a Doc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
