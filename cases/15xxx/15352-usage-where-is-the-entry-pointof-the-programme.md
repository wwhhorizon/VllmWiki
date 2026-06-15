# vllm-project/vllm#15352: [Usage]: Where is the entry pointof the programme

| 字段 | 值 |
| --- | --- |
| Issue | [#15352](https://github.com/vllm-project/vllm/issues/15352) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Where is the entry pointof the programme

### Issue 正文摘录

### Your current environment When I start a backend service using ` VLLM_USE_V1=1 vllm serve meta-llama/Llama-3.1-8B-Instruct \ --max-model-len $MAX_MODEL_LEN \ --gpu-memory-utilization 0.31 \ --enforce-eager \ --enable-prefix-caching \ --max-num-seqs 1 ` I want to know where the entry point of flash attention is I modified `vllm/attention/backends/flash_attn.py` but nothing happens.It seems that the kernal is not here QAQ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pointof the programme usage ### Your current environment When I start a backend service using ` VLLM_USE_V1=1 vllm serve meta-llama/Llama-3.1-8B-Instruct \ --max-model-len $MAX_MODEL_LEN \ --gpu-memory-utilization 0.31...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: AQ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: When I start a backend service using ` VLLM_USE_V1=1 vllm serve meta-llama/Llama-3.1-8B-Instruct \ --max-model-len $MAX_MODEL_LEN \ --gpu-memory-utilization 0.31 \ --enforce-eager \ --enable-prefix-caching \ --max-num-s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
