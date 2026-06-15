# vllm-project/vllm#743: Data-parallel inference 

| 字段 | 值 |
| --- | --- |
| Issue | [#743](https://github.com/vllm-project/vllm/issues/743) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Data-parallel inference 

### Issue 正文摘录

Is there a supported way to do data-parallel inference with vLLM? I have N gpus and would like to parallelise a model on each gpu (not tensor parallel but data parallel). Right now I’m just wrapping LLM in a remote task (with resource=1 gpu) for offline processing of chunks of prompts (each gpu gets assigned total_prompts/N number of prompts to process).

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: allel inference with vLLM? I have N gpus and would like to parallelise a model on each gpu (not tensor parallel but data parallel). Right now I’m just wrapping LLM in a remote task (with resource=1 gpu) for offline proc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
