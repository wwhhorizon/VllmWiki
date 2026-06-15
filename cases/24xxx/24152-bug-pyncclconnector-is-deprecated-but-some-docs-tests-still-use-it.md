# vllm-project/vllm#24152: [Bug]: PyNcclConnector is deprecated, but some docs/tests still use it

| 字段 | 值 |
| --- | --- |
| Issue | [#24152](https://github.com/vllm-project/vllm/issues/24152) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PyNcclConnector is deprecated, but some docs/tests still use it

### Issue 正文摘录

### Your current environment main branch code ### 🐛 Describe the bug It's no longer registered in https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/factory.py and now P2pNcclConnector is the only in-tree NCCL implementation of kv-connector now. https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/v1/p2p/p2p_nccl_connector.py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: PyNcclConnector is deprecated, but some docs/tests still use it bug ### Your current environment main branch code ### 🐛 Describe the bug It's no longer registered in https://github.com/vllm-project/vllm/blob/main...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
