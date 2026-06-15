# vllm-project/vllm#5148: [Misc]: Should inference with temperature 0 generate the same results for a lora adapter and equivalent merged model?

| 字段 | 值 |
| --- | --- |
| Issue | [#5148](https://github.com/vllm-project/vllm/issues/5148) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Should inference with temperature 0 generate the same results for a lora adapter and equivalent merged model?

### Issue 正文摘录

### Anything you want to discuss about vllm. I am scoring a fine-tuned mistral modal using the vllm enable_lora option with temperature 0.0. Subsequently merging that lora adapter into the base model using peft merge_and_unload results in a new merged model which when used with vllm (again temperature 0.0) generates noticeably different results. 1. Should I be expecting these two methods of inference to generate the same result? 2. If so is there any suggested method for loading the base model and adapter and merging that would result in the same generation results?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ure 0 generate the same results for a lora adapter and equivalent merged model? ### Anything you want to discuss about vllm. I am scoring a fine-tuned mistral modal using the vllm enable_lora option with temperature 0.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
