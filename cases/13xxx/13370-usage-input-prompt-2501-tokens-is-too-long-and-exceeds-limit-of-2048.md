# vllm-project/vllm#13370: [Usage]:Input prompt (2501 tokens) is too long and exceeds limit of 2048

| 字段 | 值 |
| --- | --- |
| Issue | [#13370](https://github.com/vllm-project/vllm/issues/13370) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:Input prompt (2501 tokens) is too long and exceeds limit of 2048

### Issue 正文摘录

### Your current environment ```text env: 16*H800 model:deepseekr1 version:0.7.2 start scrpts:python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 80 --max-model-len 128000 --trust-remote-code --pipeline-parallel-size 2 --tensor-parallel-size 8 --gpu-memory-utilization 0.8 --served-model-name deepseek --model /mnt/workspace/models/public-models/llm/DeepSeek-R1 “WARNING 02-16 15:37:32 scheduler.py:947] Input prompt (2501 tokens) is too long and exceeds limit of 2048 INFO 02-16 15:37:32 metrics.py:453] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 9.3 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. ” ``` ### How would you like to use vllm Which parameter of the startup command can solve the problem ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: and exceeds limit of 2048 INFO 02-16 15:37:32 metrics.py:453] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 9.3 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sage ### Your current environment ```text env: 16*H800 model:deepseekr1 version:0.7.2 start scrpts:python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 80 --max-model-len 128000 --trust-remote-code --pipe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lem ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 9.3 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. ” ``` ### How would you like to use vllm Which parameter of the startup command can solve the prob...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s limit of 2048 usage ### Your current environment ```text env: 16*H800 model:deepseekr1 version:0.7.2 start scrpts:python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 80 --max-model-len 128000 --trust-r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
