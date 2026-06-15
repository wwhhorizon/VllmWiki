# vllm-project/vllm#6083: [Usage]: Why is the useage information missing in the streaming call. Not streaming is there.

| 字段 | 值 |
| --- | --- |
| Issue | [#6083](https://github.com/vllm-project/vllm/issues/6083) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why is the useage information missing in the streaming call. Not streaming is there.

### Issue 正文摘录

### Your current environment ```text data: {"id":"cmpl-840312ff78664572bb504e606140b952","object":"chat.completion.chunk","created":1719969577,"model":"Qwen-v","choices":[{"index":0,"delta":{"role":"assistant"},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-840312ff78664572bb504e606140b952","object":"chat.completion.chunk","created":1719969577,"model":"Qwen-v","choices":[{"index":0,"delta":{"content":"我是"},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-840312ff78664572bb504e606140b952","object":"chat.completion.chunk","created":1719969577,"model":"Qwen-v","choices":[{"index":0,"delta":{"content":"阿里"},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-840312ff78664572bb504e606140b952","object":"chat.completion.chunk","created":1719969577,"model":"Qwen-v","choices":[{"index":0,"delta":{"content":"云"},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-840312ff78664572bb504e606140b952","object":"chat.completion.chunk","created":1719969577,"model":"Qwen-v","choices":[{"index":0,"delta":{"content":"开发"},"logprobs":null,"finish_reason":null}]} data: {"id":"cmpl-840312ff78664572bb504e606140b952","object":"chat.completion.chunk","created":1719969577,"mo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Why is the useage information missing in the streaming call. Not streaming is there. usage ### Your current environment ```text data: {"id":"cmpl-840312ff78664572bb504e606140b952","object":"chat.completion.chun...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
