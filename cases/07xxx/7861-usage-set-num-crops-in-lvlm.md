# vllm-project/vllm#7861: [Usage]: set num_crops in LVLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7861](https://github.com/vllm-project/vllm/issues/7861) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: set num_crops in LVLM

### Issue 正文摘录

How to set up the num_crops for LVLMs? For example, when initializing the processor for Ph-3.5-vision-instruct, the hugging face code looks like the following: ```python processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True, num_crops=4 ) ``` But I didn't find a way to set num_crops in vllm. I checked the [pull request #7710](https://github.com/vllm-project/vllm/pull/7710), but I didn't find the solution.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: set num_crops in LVLM usage How to set up the num_crops for LVLMs? For example, when initializing the processor for Ph-3.5-vision-instruct, the hugging face code looks like the following: ```python processor =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: But I didn't find a way to set num_crops in vllm. I checked the [pull request #7710](https://github.com/vllm-project/vllm/pull/7710), but I didn't find the solution.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
