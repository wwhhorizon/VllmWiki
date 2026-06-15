# vllm-project/vllm#11829: [Misc]: BlockHashType hash collision in v1 

| 字段 | 值 |
| --- | --- |
| Issue | [#11829](https://github.com/vllm-project/vllm/issues/11829) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: BlockHashType hash collision in v1 

### Issue 正文摘录

### Anything you want to discuss about vllm. https://github.com/vllm-project/vllm/blob/4d29e91be84d27ca313d657eee92c067439a4c23/vllm/v1/core/kv_cache_utils.py#L13 I think this still has the potential for hash collisions. Using token IDs merely reduces the likelihood of such collisions. For example, in two sequences, if their previous block hashes are the same and the current block token IDs are also identical, a collision can still occur, albeit with a low probability. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Misc]: BlockHashType hash collision in v1 ### Anything you want to discuss about vllm. https://github.com/vllm-project/vllm/blob/4d29e91be84d27ca313d657eee92c067439a4c23/vllm/v1/core/kv_cache_utils.py#L13 I think this...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
