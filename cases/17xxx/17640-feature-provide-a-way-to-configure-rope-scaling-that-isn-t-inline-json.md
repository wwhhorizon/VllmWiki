# vllm-project/vllm#17640: [Feature]: provide a way to configure rope-scaling that isn't inline JSON

| 字段 | 值 |
| --- | --- |
| Issue | [#17640](https://github.com/vllm-project/vllm/issues/17640) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: provide a way to configure rope-scaling that isn't inline JSON

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Having to use literal JSON strings as a command argument is breaking a lot automation and scripts out there. I propose it's addressed so that all configuration can be done via simple key-value pairs. ### Alternatives Instead of configuring it as follows: ``` vllm server [...] --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' ``` I suggest something like: ``` vllm server [...] --rope-scaling "1" \ --rope-type "yarn" \ --rope-factor "4.0" \ --original-max-position-embeddings "32768"

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: provide a way to configure rope-scaling that isn't inline JSON feature request ### 🚀 The feature, motivation and pitch Having to use literal JSON strings as a command argument is breaking a lot automation and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : provide a way to configure rope-scaling that isn't inline JSON feature request ### 🚀 The feature, motivation and pitch Having to use literal JSON strings as a command argument is breaking a lot automation and scripts...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
