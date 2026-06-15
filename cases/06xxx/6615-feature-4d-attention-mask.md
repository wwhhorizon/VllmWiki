# vllm-project/vllm#6615: [Feature]: 4D Attention Mask

| 字段 | 值 |
| --- | --- |
| Issue | [#6615](https://github.com/vllm-project/vllm/issues/6615) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: 4D Attention Mask

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am workning on 4D attention mask input and LLM generateion process. Huggingface provides an interface for the 4D attention mask. Does vllm have any plan? https://github.com/huggingface/transformers/pull/27539 ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: 4D Attention Mask feature request;stale ### 🚀 The feature, motivation and pitch I am workning on 4D attention mask input and LLM generateion process. Huggingface provides an interface for the 4D attention mas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h I am workning on 4D attention mask input and LLM generateion process. Huggingface provides an interface for the 4D attention mask. Does vllm have any plan? https://github.com/huggingface/transformers/pull/27539 ### Al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
