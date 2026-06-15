# vllm-project/vllm#813: Stream Tokens operation integration into LLM class (which uses LLMEngine behind the scenes)

| 字段 | 值 |
| --- | --- |
| Issue | [#813](https://github.com/vllm-project/vllm/issues/813) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stream Tokens operation integration into LLM class (which uses LLMEngine behind the scenes)

### Issue 正文摘录

Hey, I wonder why the token streaming via LLM class is not implemented, but for LLMEngine it does? https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/llm.py LLM is using behind the scene the LLMEngine. LLM class is much simpler (to me I guess, not sure if to everyone else) and also utilize batch processing on top (on top LLMEngine) of tensor parallel, so it would be nice to get also a stream with batch process together if possible, or either of them. It shouldn't be much work to do as I read the code and after I talked with @naed90 about that feature. Thanks, Orel

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: gine. LLM class is much simpler (to me I guess, not sure if to everyone else) and also utilize batch processing on top (on top LLMEngine) of tensor parallel, so it would be nice to get also a stream with batch process t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
