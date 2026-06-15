# vllm-project/vllm#21563: [Usage]: Disable the FlashInfer 0.2.3+ does not support per-request generators warning

| 字段 | 值 |
| --- | --- |
| Issue | [#21563](https://github.com/vllm-project/vllm/issues/21563) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Disable the FlashInfer 0.2.3+ does not support per-request generators warning

### Issue 正文摘录

### Your current environment ```text vLLM 0.9.2 ``` ### How would you like to use vllm I am using vllm 0.9.2 with Qwen2.5-VL, and the log is bloated with these warnings: ``` (VllmWorker rank=3 pid=324) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer 0.2.3+ does not support per-request generators. Falling back to PyTorch-native implementation. (VllmWorker rank=1 pid=322) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer 0.2.3+ does not support per-request generators. Falling back to PyTorch-native implementation. (VllmWorker rank=2 pid=323) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer 0.2.3+ does not support per-request generators. Falling back to PyTorch-native implementation. (VllmWorker rank=0 pid=321) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer 0.2.3+ does not support per-request generators. Falling back to PyTorch-native implementation. (VllmWorker rank=3 pid=324) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer 0.2.3+ does not support per-request generators. Falling back to PyTorch-native implementation. (VllmWorker rank=1 pid=322) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer 0.2.3+ does not...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Disable the FlashInfer 0.2.3+ does not support per-request generators warning usage;stale ### Your current environment ```text vLLM 0.9.2 ``` ### How would you like to use vllm I am using vllm 0.9.2 with Qwen2....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: Disable the FlashInfer 0.2.3+ does not support per-request generators warning usage;stale ### Your current environment ```text vLLM 0.9.2 ``` ### How would you like to use vllm I am using vllm 0.9.2 with Qwen2....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .9.2 ``` ### How would you like to use vllm I am using vllm 0.9.2 with Qwen2.5-VL, and the log is bloated with these warnings: ``` (VllmWorker rank=3 pid=324) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: these warnings: ``` (VllmWorker rank=3 pid=324) WARNING 07-24 18:08:58 [topk_topp_sampler.py:100] FlashInfer 0.2.3+ does not support per-request generators. Falling back to PyTorch-native implementation. (VllmWorker ran...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
