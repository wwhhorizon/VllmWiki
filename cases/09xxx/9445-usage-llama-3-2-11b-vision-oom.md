# vllm-project/vllm#9445: [Usage]: Llama-3.2-11B-Vision OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#9445](https://github.com/vllm-project/vllm/issues/9445) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Llama-3.2-11B-Vision OOM

### Issue 正文摘录

### Your current environment vllm version 0.6.3 A100 80GB ### How would you like to use vllm I want to serve Llama-3.2-11B-Vision, but it OOMs. Command is: ``` vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --chat-template /workspace/llama_process/chat_template.jinja --max-model-len 1024 ``` I tested the same command on llava-hf/llava-1.5-7b-hf and it works fine. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Llama-3.2-11B-Vision OOM usage ### Your current environment vllm version 0.6.3 A100 80GB ### How would you like to use vllm I want to serve Llama-3.2-11B-Vision, but it OOMs. Command is: ``` vllm serve meta-lla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .2-11B-Vision OOM usage ### Your current environment vllm version 0.6.3 A100 80GB ### How would you like to use vllm I want to serve Llama-3.2-11B-Vision, but it OOMs. Command is: ``` vllm serve meta-llama/Llama-3.2-11B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sage]: Llama-3.2-11B-Vision OOM usage ### Your current environment vllm version 0.6.3 A100 80GB ### How would you like to use vllm I want to serve Llama-3.2-11B-Vision, but it OOMs. Command is: ``` vllm serve meta-llama...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Llama-3.2-11B-Vision OOM usage ### Your current environment vllm version 0.6.3 A100 80GB ### How would you like to use vllm I want to serve Llama-3.2-11B-Vision, but it OOMs. Command is: ``` vllm serve meta-lla...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /workspace/llama_process/chat_template.jinja --max-model-len 1024 ``` I tested the same command on llava-hf/llava-1.5-7b-hf and it works fine. ### Before submitting a new issue... - [X] Make sure you already searched fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
