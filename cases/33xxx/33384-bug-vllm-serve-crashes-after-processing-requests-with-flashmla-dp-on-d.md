# vllm-project/vllm#33384: [Bug]: vLLM serve crashes after processing requests with FlashMLA + DP on DeepSeek

| 字段 | 值 |
| --- | --- |
| Issue | [#33384](https://github.com/vllm-project/vllm/issues/33384) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM serve crashes after processing requests with FlashMLA + DP on DeepSeek

### Issue 正文摘录

### Your current environment **Environment** - GPU: NVIDIA H20 - Model: DeepSeek-R1 - vLLM: 0.14.0 - Backend: FlashMLA - TP: 4 - DP: 2 When serving DeepSeek-R1-0528 with vLLM FlashMLA backend on H20 GPUs, vllm serve crashes after requests are sent and processed if DP is enabled. ### 🐛 Describe the bug vllm serve /workspace/models3/DeepSeek-R1-0528/ --port 25539 -tp 4 -dp 2 --trust-remote-code --no-enable-prefix-caching --swap-space 16 --max-model-len 8192 --cudagraph-capture-sizes 32 --gpu-memory-utilization 0.8 vllm bench serve --model /workspace/models3/DeepSeek-R1-0528/ --dataset-name random --num-prompts 32 --max-concurrency 32 --random-input-len 2048 --random-output-len 2048 --ignore-eos --port 25539 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --no-enable-prefix-caching --swap-space 16 --max-model-len 8192 --cudagraph-capture-sizes 32 --gpu-memory-utilization 0.8 vllm bench serve --model /workspace/models3/DeepSeek-R1-0528/ --dataset-name random --num-prompts...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: **Environment** - GPU: NVIDIA H20 - Model: DeepSeek-R1 - vLLM: 0.14.0 - Backend: FlashMLA - TP: 4 - DP: 2 When serving DeepSeek-R1-0528 with vLLM FlashMLA backend on H20 GPUs, vllm serve crashes after requests are sent...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: k bug ### Your current environment **Environment** - GPU: NVIDIA H20 - Model: DeepSeek-R1 - vLLM: 0.14.0 - Backend: FlashMLA - TP: 4 - DP: 2 When serving DeepSeek-R1-0528 with vLLM FlashMLA backend on H20 GPUs, vllm ser...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vLLM serve crashes after processing requests with FlashMLA + DP on DeepSeek bug ### Your current environment **Environment** - GPU: NVIDIA H20 - Model: DeepSeek-R1 - vLLM: 0.14.0 - Backend: FlashMLA - TP: 4 - DP:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
