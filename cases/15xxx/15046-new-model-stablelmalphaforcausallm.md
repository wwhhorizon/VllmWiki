# vllm-project/vllm#15046: [New Model]: StableLMAlphaForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#15046](https://github.com/vllm-project/vllm/issues/15046) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: StableLMAlphaForCausalLM

### Issue 正文摘录

**The model to consider.** * StableLMAlphaForCausalLM, including `stabilityai/stablelm-base-alpha-7b-v2` `stabilityai/stablelm-base-alpha-3b-v2` **The closest model vllm already supports.** * StableLmForCausalLM, such as `stabilityai/stablelm-3b-4e1t` **What's your difficulty of supporting the model you want?** N/A ### Before submitting a new issue... - [x] #15052

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: StableLMAlphaForCausalLM new-model;stale **The model to consider.** * StableLMAlphaForCausalLM, including `stabilityai/stablelm-base-alpha-7b-v2` `stabilityai/stablelm-base-alpha-3b-v2` **The closest model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: StableLMAlphaForCausalLM new-model;stale **The model to consider.** * StableLMAlphaForCausalLM, including `stabilityai/stablelm-base-alpha-7b-v2` `stabilityai/stablelm-base-alpha-3b-v2` **The closest model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
