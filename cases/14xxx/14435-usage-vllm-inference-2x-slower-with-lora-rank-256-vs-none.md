# vllm-project/vllm#14435: [Usage]: VLLM Inference - 2x slower with LoRA rank=256 vs none.

| 字段 | 值 |
| --- | --- |
| Issue | [#14435](https://github.com/vllm-project/vllm/issues/14435) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: VLLM Inference - 2x slower with LoRA rank=256 vs none.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I've noticed that using LoRA with rank=256 significantly slows down inference by 4x, as shown below. However, reducing the rank to 8 or 16 brings performance closer to that of no LoRA. I'm currently using two fully-utilized GPUs, without the enforce_eager flag, and have set the maximum LoRA rank accordingly. Interestingly, adjusting the maximum model length had no impact on performance. What steps can I take to optimize performance? **No Lora** **Processed prompts**: 0%|▏ | 5/2430 [01:28<6:58:39, 10.36s/it, est. speed input: 3.71 toks/s, output: 2.34 toks/s]Processed prompts: 10%|█████▊ | 240/2430 [05:09<44:09, 1.21s/it, est. speed input: 87.79 toks/s, output: 90.18 toks/s]WARNING 03-06 17:12:30 scheduler.py:1754] Sequence group 352 is preempted by PreemptionMode.RECOMPUTE mode because there is not enough KV cache space. This can affect the end-to-end performance. Increase gpu_memory_utilization or tensor_parallel_size to provide more KV cache memory. total_num_cumulative_preemption=51 **Processed prompt**s: 20%|███████████▏ | 476/2430 [09:38<39:30, 1.21s/it, est. spee...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: VLLM Inference - 2x slower with LoRA rank=256 vs none. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I've noticed that using LoRA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 6 significantly slows down inference by 4x, as shown below. However, reducing the rank to 8 or 16 brings performance closer to that of no LoRA. I'm currently using two fully-utilized GPUs, without the enforce_eager flag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /s] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: s preempted by PreemptionMode.RECOMPUTE mode because there is not enough KV cache space. This can affect the end-to-end performance. Increase gpu_memory_utilization or tensor_parallel_size to provide more KV cache memor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: the maximum LoRA rank accordingly. Interestingly, adjusting the maximum model length had no impact on performance. What steps can I take to optimize performance? **No Lora** **Processed prompts**: 0%|▏ | 5/2430 [01:28<6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
