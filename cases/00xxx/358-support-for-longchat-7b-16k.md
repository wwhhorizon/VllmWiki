# vllm-project/vllm#358: Support for longchat-7b-16k

| 字段 | 值 |
| --- | --- |
| Issue | [#358](https://github.com/vllm-project/vllm/issues/358) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for longchat-7b-16k

### Issue 正文摘录

It would be great, if you can add support for longchat(from Fastchat) models, which have 16k context length: https://github.com/lm-sys/FastChat https://github.com/lm-sys/FastChat/blob/6d06351542bc0c3701d54619e6df4c26aa91a260/fastchat/model/llama_condense_monkey_patch.py#L10C18-L10C18

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support for longchat-7b-16k new-model It would be great, if you can add support for longchat(from Fastchat) models, which have 16k context length: https://github.com/lm-sys/FastChat https://github.com/lm-sys/FastChat/bl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
