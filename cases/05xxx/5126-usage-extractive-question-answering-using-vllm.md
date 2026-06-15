# vllm-project/vllm#5126: [Usage]: extractive question answering using VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#5126](https://github.com/vllm-project/vllm/issues/5126) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: extractive question answering using VLLM

### Issue 正文摘录

### Your current environment vllm==0.2.7 ### How would you like to use vllm Is extractive question answering possible with VLLM batched inference? Here is an example: https://yonigottesman.github.io/2023/08/10/extractive-generative.html . I have seen logits_processor field in SampleParams in vllm 0.2.7 but I am not sure how to set it up to choose tokens only from the context for each prompt

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ssible with VLLM batched inference? Here is an example: https://yonigottesman.github.io/2023/08/10/extractive-generative.html . I have seen logits_processor field in SampleParams in vllm 0.2.7 but I am not sure how to s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: extractive question answering using VLLM usage;stale ### Your current environment vllm==0.2.7 ### How would you like to use vllm Is extractive question answering possible with VLLM batched inference? Here is an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
