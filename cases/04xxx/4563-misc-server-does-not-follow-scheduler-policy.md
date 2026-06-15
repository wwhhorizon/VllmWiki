# vllm-project/vllm#4563: [Misc]: Server Does Not Follow Scheduler Policy

| 字段 | 值 |
| --- | --- |
| Issue | [#4563](https://github.com/vllm-project/vllm/issues/4563) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Server Does Not Follow Scheduler Policy

### Issue 正文摘录

### Anything you want to discuss about vllm. I was testing out vLLM on Colab and notices something weird. It seems from the code that vLLM is using first come first serve order policy: https://github.com/vllm-project/vllm/blob/7038e8b80303bf6128acbe508dec910183a1be56/vllm/core/scheduler.py#L729 https://github.com/vllm-project/vllm/blob/7038e8b80303bf6128acbe508dec910183a1be56/vllm/core/policy.py#L29-L36 However, When I was running the OpenAI compatible vLLM server, I sent in orders in sequence and found the server to not follow the first come first serve policy. Instead, they seemed random? Here is a example jupyter notebook replicating the issue: https://colab.research.google.com/drive/1mMPTZiKJoQEsvjBjNUGttsbp9L1F9zXm?usp=sharing Is there some optimization I missed that optimized the order of inputs? I am a bit confused on what controls the server's output order. Any advice would be appreciated, thanks!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sed on what controls the server's output order. Any advice would be appreciated, thanks!
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e is a example jupyter notebook replicating the issue: https://colab.research.google.com/drive/1mMPTZiKJoQEsvjBjNUGttsbp9L1F9zXm?usp=sharing Is there some optimization I missed that optimized the order of inputs? I am a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Server Does Not Follow Scheduler Policy ### Anything you want to discuss about vllm. I was testing out vLLM on Colab and notices something weird. It seems from the code that vLLM is using first come first serve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: low Scheduler Policy ### Anything you want to discuss about vllm. I was testing out vLLM on Colab and notices something weird. It seems from the code that vLLM is using first come first serve order policy: https://githu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
