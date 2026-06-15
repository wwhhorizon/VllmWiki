# vllm-project/vllm#7420: [New Model]: LLaVA-OneVision

| 字段 | 值 |
| --- | --- |
| Issue | [#7420](https://github.com/vllm-project/vllm/issues/7420) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: LLaVA-OneVision

### Issue 正文摘录

### The model to consider. https://huggingface.co/lmms-lab/llava-onevision-qwen2-7b-ov There are a bunch of others using the same architecture. ### The closest model vllm already supports. qwen2. AFAIK the main difference is a vision encoder which I think is based on siglip (also supported) ### What's your difficulty of supporting the model you want? Mixing qwen2 and siglip (maybe other changes)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: LLaVA-OneVision new-model ### The model to consider. https://huggingface.co/lmms-lab/llava-onevision-qwen2-7b-ov There are a bunch of others using the same architecture. ### The closest model vllm already s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /llava-onevision-qwen2-7b-ov There are a bunch of others using the same architecture. ### The closest model vllm already supports. qwen2. AFAIK the main difference is a vision encoder which I think is based on siglip (a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
