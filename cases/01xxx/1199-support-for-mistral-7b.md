# vllm-project/vllm#1199: Support for Mistral 7B

| 字段 | 值 |
| --- | --- |
| Issue | [#1199](https://github.com/vllm-project/vllm/issues/1199) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for Mistral 7B

### Issue 正文摘录

Hi, will vLLM need additional changes to make Mistral 7B work? They use sliding window attention which I think would require small modification on the vLLM side. mistralai/Mistral-7B-Instruct-v0.1 Thank you

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l 7B work? They use sliding window attention which I think would require small modification on the vLLM side. mistralai/Mistral-7B-Instruct-v0.1 Thank you

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
