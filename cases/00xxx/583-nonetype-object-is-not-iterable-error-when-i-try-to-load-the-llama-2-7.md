# vllm-project/vllm#583: 'NoneType' object is not iterable error when I try to load the llama-2-7b-chat model.

| 字段 | 值 |
| --- | --- |
| Issue | [#583](https://github.com/vllm-project/vllm/issues/583) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 'NoneType' object is not iterable error when I try to load the llama-2-7b-chat model.

### Issue 正文摘录

I downloaded the llama-2-7b-chat model straight from meta and I'm trying to load it through vLLM, after taking 5-10 mins loading the tokenizer, it gives me the following error: -> for arch in architectures: 'NoneType' object is not iterable Any way to resolve this issue?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 'NoneType' object is not iterable error when I try to load the llama-2-7b-chat model. I downloaded the llama-2-7b-chat model straight from meta and I'm trying to load it through vLLM, after taking 5-10 mins loading the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -10 mins loading the tokenizer, it gives me the following error: -> for arch in architectures: 'NoneType' object is not iterable Any way to resolve this issue?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
