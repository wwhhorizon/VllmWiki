# vllm-project/vllm#2370: How to use Splitwise(from microsoft) in vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#2370](https://github.com/vllm-project/vllm/issues/2370) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to use Splitwise(from microsoft) in vllm?

### Issue 正文摘录

Microsoft have claimed that ”Splitwise“ is supported in vLLM, see https://www.microsoft.com/en-us/research/blog/splitwise-improves-gpu-usage-by-splitting-llm-inference-phases/ ![image](https://github.com/vllm-project/vllm/assets/58217233/7835c241-f22c-4ffc-a510-1238f4a5d770) So how to use it in vLLM? I could not find keyword about ”Splitwise“.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Splitwise“ is supported in vLLM, see https://www.microsoft.com/en-us/research/blog/splitwise-improves-gpu-usage-by-splitting-llm-inference-phases/ ![image](https://github.com/vllm-project/vllm/assets/58217233/7835c241-f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to use Splitwise(from microsoft) in vllm? stale Microsoft have claimed that ”Splitwise“ is supported in vLLM, see https://www.microsoft.com/en-us/research/blog/splitwise-improves-gpu-usage-by-splitting-llm-inference...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
