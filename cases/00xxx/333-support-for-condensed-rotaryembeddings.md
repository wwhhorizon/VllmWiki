# vllm-project/vllm#333: Support for Condensed RotaryEmbeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#333](https://github.com/vllm-project/vllm/issues/333) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for Condensed RotaryEmbeddings

### Issue 正文摘录

looks like there are various methods of extending context length, suck as superhot, ntk-aware, and condensed rope. This request is to track support for condensed rotaryembeddings as it seems to have the best performance at long contexts atm. https://lmsys.org/blog/2023-06-29-longchat/ https://github.com/lm-sys/FastChat/blob/3f0c6e54498e179098ead9a596929e23327ad75c/fastchat/model/llama_condense_monkey_patch.py#L68

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m/lm-sys/FastChat/blob/3f0c6e54498e179098ead9a596929e23327ad75c/fastchat/model/llama_condense_monkey_patch.py#L68
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Support for Condensed RotaryEmbeddings feature request looks like there are various methods of extending context length, suck as superhot, ntk-aware, and condensed rope. This request is to track support for condensed ro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
