# vllm-project/vllm#11337: [Usage]: How to expand inference context length to longer (such as 128k, 256k) on multi modality models.

| 字段 | 值 |
| --- | --- |
| Issue | [#11337](https://github.com/vllm-project/vllm/issues/11337) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to expand inference context length to longer (such as 128k, 256k) on multi modality models.

### Issue 正文摘录

### Your current environment * environment torch: 2.5.0 vllm: 0.6.3.post2.dev171+g890ca360 * problem Now I have several A100 and a Qwen2-VL-7B model, I'm trying expanding this model during inference time to 128k, but cause oom. I have tried: 1. https://github.com/vllm-project/vllm/issues/10537 Set max_num_seqs = 1 or 2, cause oom again. 2. https://github.com/vllm-project/vllm/issues/10474 Set tensor_parallel_size=2, find the same issue, which have't solved yet. 3. https://github.com/vllm-project/vllm/issues/5496 Set enable_chunked_prefill=True, max_num_batched_tokens=8192, cause oom again. ### How would you like to use vllm I want to run inference of Qwen2-VL-7B on longer context(exceed 128k) based on my current working environment(several A100 80G). ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : 2.5.0 vllm: 0.6.3.post2.dev171+g890ca360 * problem Now I have several A100 and a Qwen2-VL-7B model, I'm trying expanding this model during inference time to 128k, but cause oom. I have tried: 1. https://github.com/vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nference context length to longer (such as 128k, 256k) on multi modality models. usage ### Your current environment * environment torch: 2.5.0 vllm: 0.6.3.post2.dev171+g890ca360 * problem Now I have several A100 and a Q...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: I'm trying expanding this model during inference time to 128k, but cause oom. I have tried: 1. https://github.com/vllm-project/vllm/issues/10537 Set max_num_seqs = 1 or 2, cause oom again. 2. https://github.com/vllm-pro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: . 3. https://github.com/vllm-project/vllm/issues/5496 Set enable_chunked_prefill=True, max_num_batched_tokens=8192, cause oom again. ### How would you like to use vllm I want to run inference of Qwen2-VL-7B on longer co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
