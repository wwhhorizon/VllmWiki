# vllm-project/vllm#3934: [Feature]: Support for Higher than 64 LoRa Ranks

| 字段 | 值 |
| --- | --- |
| Issue | [#3934](https://github.com/vllm-project/vllm/issues/3934) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Higher than 64 LoRa Ranks

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, I was delighted to see the implementation of the multi LoRa feature and would like to express my gratitude and appreciation for your efforts. However, the LoRa we have developed operates with r=128 and r=256, and currently, it does not work for me, resulting in the following error: `ValueError: max_lora_rank (128) must be one of (8, 16, 32, 64).` I am curious to know if there are any plans to support higher ranks? Is this on the priority list? It's quite crucial for us, and we would greatly appreciate any development in this area. Thank you. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support for Higher than 64 LoRa Ranks feature request;stale ### 🚀 The feature, motivation and pitch Hello, I was delighted to see the implementation of the multi LoRa feature and would like to express my grat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: f the multi LoRa feature and would like to express my gratitude and appreciation for your efforts. However, the LoRa we have developed operates with r=128 and r=256, and currently, it does not work for me, resulting in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
