# vllm-project/vllm#1557: Add support for LongLora

| 字段 | 值 |
| --- | --- |
| Issue | [#1557](https://github.com/vllm-project/vllm/issues/1557) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add support for LongLora

### Issue 正文摘录

I am using [LongLora](https://github.com/dvlab-research/LongLoRA) for inference. The model uses [short shift attention](https://github.com/dvlab-research/LongLoRA/blob/main/llama_attn_replace_sft.py). I am not sure whether vllm supports it? If no, is it possible to support it?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LongLora](https://github.com/dvlab-research/LongLoRA) for inference. The model uses [short shift attention](https://github.com/dvlab-research/LongLoRA/blob/main/llama_attn_replace_sft.py). I am not sure whether vllm sup...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gLora feature request I am using [LongLora](https://github.com/dvlab-research/LongLoRA) for inference. The model uses [short shift attention](https://github.com/dvlab-research/LongLoRA/blob/main/llama_attn_replace_sft.p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Add support for LongLora feature request I am using [LongLora](https://github.com/dvlab-research/LongLoRA) for inference. The model uses [short shift attention](https://github.com/dvlab-research/LongLoRA/blob/main/llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
