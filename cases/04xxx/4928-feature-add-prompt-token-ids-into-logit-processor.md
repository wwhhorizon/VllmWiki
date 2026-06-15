# vllm-project/vllm#4928: [Feature]: Add prompt token ids into logit processor?

| 字段 | 值 |
| --- | --- |
| Issue | [#4928](https://github.com/vllm-project/vllm/issues/4928) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add prompt token ids into logit processor?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am using vllm's SamplingParams to set up the logit processor. It looks the same as huggingface, but there are some subtle differences in use. The main difference is that it does not give the logit processor all the token IDs, but starts from the generated token. On the contrary, huggingface provides the prompt and the token ID of the generated token. I was wondering if there is a way to allow the use of vllm's logit processor to also obtain this information? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm's SamplingParams to set up the logit processor. It looks the same as huggingface, but there are some subtle differences in use. The main difference is that it does not give the logit processor all the token IDs, but...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re]: Add prompt token ids into logit processor? good first issue;feature request ### 🚀 The feature, motivation and pitch I am using vllm's SamplingParams to set up the logit processor. It looks the same as huggingface,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
