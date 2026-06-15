# vllm-project/vllm#1277: Question about the design of attention

| 字段 | 值 |
| --- | --- |
| Issue | [#1277](https://github.com/vllm-project/vllm/issues/1277) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Question about the design of attention

### Issue 正文摘录

In the model_executor/layers/attention.py, line 207-209, how does vLLM can ensure that when `num_prompt_tokens > 0`, `num_generation_tokens == 0`? Does this mean the prompt will always be prioritised than generation? I have check the `_prepare_inputs()` in worker.py. However, I have not found any clue why this can happen. I am really looking forward to any help.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Question about the design of attention In the model_executor/layers/attention.py, line 207-209, how does vLLM can ensure that when `num_prompt_tokens > 0`, `num_generation_tokens == 0`? Does this mean the prompt will al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
