# vllm-project/vllm#801: I think it would be good to have option of both an OpenAI or a HuggingFace style sampler.

| 字段 | 值 |
| --- | --- |
| Issue | [#801](https://github.com/vllm-project/vllm/issues/801) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> I think it would be good to have option of both an OpenAI or a HuggingFace style sampler.

### Issue 正文摘录

Huggingface sampler is more commonly used. I think it would be good to be able to swap between them. What do people think? In future I could contribute a PR (not soon though) - if the authors of the library believe this is a good idea.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: I think it would be good to have option of both an OpenAI or a HuggingFace style sampler. Huggingface sampler is more commonly used. I think it would be good to be able to swap between them. What do people think? In fut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
