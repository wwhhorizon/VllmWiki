# vllm-project/vllm#7740: [Feature]: phi-3.5 is a strong model for its size, including vision support.  Has multi-image support, but vllm does not support

| 字段 | 值 |
| --- | --- |
| Issue | [#7740](https://github.com/vllm-project/vllm/issues/7740) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: phi-3.5 is a strong model for its size, including vision support.  Has multi-image support, but vllm does not support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch phi-3.5 is a strong model for its size, including strong multi-image vision support. But vllm does not support the multi-image case. https://github.com/vllm-project/vllm/blob/03b7bfb79b1edf54511fd1b12acc9a875cee5656/vllm/model_executor/models/phi3v.py#L421-L425 ### Alternatives Only other models ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: phi-3.5 is a strong model for its size, including vision support. Has multi-image support, but vllm does not support feature request ### 🚀 The feature, motivation and pitch phi-3.5 is a strong model for its s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ion support. Has multi-image support, but vllm does not support feature request ### 🚀 The feature, motivation and pitch phi-3.5 is a strong model for its size, including strong multi-image vision support. But vllm does...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
