# vllm-project/vllm#5155: [Feature]: Linear adapter support for Mixtral

| 字段 | 值 |
| --- | --- |
| Issue | [#5155](https://github.com/vllm-project/vllm/issues/5155) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Linear adapter support for Mixtral

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi folks, While vLLM does support running inference with LoRA adapters for Mixtral, it seems like it only does so for layers k, v, q, and o. It would be great to have LoRA inference support for linear layers (w1, w2, w3, gate) as well. That would bring inference to parity with training support - https://github.com/OpenAccess-AI-Collective/axolotl/blob/main/examples/mistral/mixtral.yml ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Linear adapter support for Mixtral feature request ### 🚀 The feature, motivation and pitch Hi folks, While vLLM does support running inference with LoRA adapters for Mixtral, it seems like it only does so for...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
