# vllm-project/vllm#3335: [Feature request] Support CohereForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#3335](https://github.com/vllm-project/vllm/issues/3335) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature request] Support CohereForCausalLM

### Issue 正文摘录

Would it be possible you add support for CohereForCausalLM? Here is the model: https://huggingface.co/CohereForAI/c4ai-command-r-v01 It's a very capable model that supports many languages (including some not supported by many other models like Vietnamese and Persian) so I think it will be quite widely used by the non-English AI community. Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Would it be possible you add support for CohereForCausalLM? Here is the model: https://huggingface.co/CohereForAI/c4ai-command-r-v01 It's a very capable model that supports many languages (including some not supported b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature request] Support CohereForCausalLM Would it be possible you add support for CohereForCausalLM? Here is the model: https://huggingface.co/CohereForAI/c4ai-command-r-v01 It's a very capable model that supports ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
