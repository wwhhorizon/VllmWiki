# vllm-project/vllm#15758: [Bug]: deepseek reasoning parser bug

| 字段 | 值 |
| --- | --- |
| Issue | [#15758](https://github.com/vllm-project/vllm/issues/15758) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deepseek reasoning parser bug

### Issue 正文摘录

### Your current environment v0.8.2 ### 🐛 Describe the bug There is one bug scenarios: Assume the token vocabulary is: 1: ' ' ... 10000: ' ' # special token 10001: ' ' # specail token Issue: If the model generates raw text sequences like or without using their special tokens (e.g., via regular token combinations like [1,3,4] for ), the current extract_reasoning_content logic will incorrectly truncate the output. For example: If the model produces a token sequence [10000, 1, 2, 3, 4, 10001] during reasoning: Expected extracted reasoning_content: Current result is empty output due to flawed parsing logic. # Proposed Fix: Modify extract_reasoning_content to: Split token sequences based on think_end_token_id (e.g., 10001 for ). Re-decode the token IDs after splitting to ensure accuracy. # Drawback: This approach requires an additional decoding step, resulting in a slight computational overhead. Note: While the streaming method is also susceptible to this issue, both v1 and v0 versions of Multi-step Reasoning retain a probability of encountering the same errors. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: scenarios: Assume the token vocabulary is: 1: ' ' ... 10000: ' ' # special token 10001: ' ' # specail token Issue: If the model generates raw text sequences like or without using their special tokens (e.g., via regular...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: (e.g., 10001 for ). Re-decode the token IDs after splitting to ensure accuracy. # Drawback: This approach requires an additional decoding step, resulting in a slight computational overhead. Note: While the streaming met...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: (e.g., 10001 for ). Re-decode the token IDs after splitting to ensure accuracy. # Drawback: This approach requires an additional decoding step, resulting in a slight computational overhead. Note: While the streaming met...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . 10000: ' ' # special token 10001: ' ' # specail token Issue: If the model generates raw text sequences like or without using their special tokens (e.g., via regular token combinations like [1,3,4] for ), the current e...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
