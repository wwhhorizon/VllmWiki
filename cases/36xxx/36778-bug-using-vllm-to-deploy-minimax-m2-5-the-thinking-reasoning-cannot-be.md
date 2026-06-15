# vllm-project/vllm#36778: [Bug]: Using vLLM to deploy Minimax m2.5, the thinking/reasoning cannot be disable.

| 字段 | 值 |
| --- | --- |
| Issue | [#36778](https://github.com/vllm-project/vllm/issues/36778) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using vLLM to deploy Minimax m2.5, the thinking/reasoning cannot be disable.

### Issue 正文摘录

### Your current environment vllm 0.14.1 ### 🐛 Describe the bug Using vLLM to deploy Minimax m2.5, the thinking/reasoning cannot be disable. 1）don't set the --reasoning-parser 2）chat_template_kwargs": {"enable_thinking": false} 3）"enable_thinking": false None of the above methods work; the thinking mode cannot be disabled. is it a bug？ how to disable thinking ？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g ？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: et the --reasoning-parser 2）chat_template_kwargs": {"enable_thinking": false} 3）"enable_thinking": false None of the above methods work; the thinking mode cannot be disabled. is it a bug？ how to disable thinking ？ ### B...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
