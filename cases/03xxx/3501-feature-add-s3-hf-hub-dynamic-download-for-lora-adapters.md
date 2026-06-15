# vllm-project/vllm#3501: [Feature]: Add S3/HF Hub dynamic download for LoRA adapters

| 字段 | 值 |
| --- | --- |
| Issue | [#3501](https://github.com/vllm-project/vllm/issues/3501) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add S3/HF Hub dynamic download for LoRA adapters

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Request for dynamic download of LoRA adapters from S3 or HF Hub based on what `model` adapter id is passed in the request. ### Alternatives No alternatives as of today, adapters need to be downloaded to server upfront and locally available. ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add S3/HF Hub dynamic download for LoRA adapters feature request;stale ### 🚀 The feature, motivation and pitch Request for dynamic download of LoRA adapters from S3 or HF Hub based on what `model` adapter id...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add S3/HF Hub dynamic download for LoRA adapters feature request;stale ### 🚀 The feature, motivation and pitch Request for dynamic download of LoRA adapters from S3 or HF Hub based on what `model` adapter id...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
