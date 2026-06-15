# vllm-project/vllm#7353: [Feature]: continuous batching for vllm.LLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7353](https://github.com/vllm-project/vllm/issues/7353) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: continuous batching for vllm.LLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Motivation: I'm using vllm.LLM to instantiate multiple vllm engines. During training, I want to make a large number of one-prompt requests to the vllm engines. From the output, it seems that vllm engines cannot use continuous batching, because it's processing one prompt at a time. vllm serve is able to use continuous batching, but does not support update of vllm model param during training. Pitch: enable continuous batching for vllm.LLM engines, or allow online update of param for vllm's openai-compatible server. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is able to use continuous batching, but does not support update of vllm model param during training. Pitch: enable continuous batching for vllm.LLM engines, or allow online update of param for vllm's openai-compatible s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: continuous batching for vllm.LLM feature request ### 🚀 The feature, motivation and pitch Motivation: I'm using vllm.LLM to instantiate multiple vllm engines. During training, I want to make a large number of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
