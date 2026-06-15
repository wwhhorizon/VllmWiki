# vllm-project/vllm#6508: [Feature]: Add OpenAI server `prompt_logprobs` support

| 字段 | 值 |
| --- | --- |
| Issue | [#6508](https://github.com/vllm-project/vllm/issues/6508) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add OpenAI server `prompt_logprobs` support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As noted in documentation OpenAI API don't support outputing only one token But it's a very strong advantage over commertial models Been able to get logits for prompt tokens ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: utputing only one token But it's a very strong advantage over commertial models Been able to get logits for prompt tokens ### Alternatives _No response_ ### Additional context _No response_
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Add OpenAI server `prompt_logprobs` support good first issue;feature request ### 🚀 The feature, motivation and pitch As noted in documentation OpenAI API don't support outputing only one token But it's a very strong...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
