# vllm-project/vllm#11437: [Misc]: When encountering torch.OutOfMemoryError and the program fails to start, the following exception message should not be displayed, as it can be confusing: 

| 字段 | 值 |
| --- | --- |
| Issue | [#11437](https://github.com/vllm-project/vllm/issues/11437) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: When encountering torch.OutOfMemoryError and the program fails to start, the following exception message should not be displayed, as it can be confusing: 

### Issue 正文摘录

### Anything you want to discuss about vllm. Exception ignored in: Traceback (most recent call last): File "/root/vllm/vllm/entrypoints/llm.py", line 236, in __del__ if self.llm_engine and hasattr(self.llm_engine, "shutdown"): AttributeError: 'LLM' object has no attribute 'llm_engine' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
