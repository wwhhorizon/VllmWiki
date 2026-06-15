# vllm-project/vllm#4739: [New Model]: Blip2 Support required

| 字段 | 值 |
| --- | --- |
| Issue | [#4739](https://github.com/vllm-project/vllm/issues/4739) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Blip2 Support required

### Issue 正文摘录

### The model to consider. https://huggingface.co/Salesforce/blip2-opt-2.7b ### The closest model vllm already supports. https://huggingface.co/liuhaotian/llava-v1.5-7b ### What's your difficulty of supporting the model you want? Support for Llava 1.5 was recently added. Blip2 has a different architecture which is currently not supported.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Blip2 Support required new-model ### The model to consider. https://huggingface.co/Salesforce/blip2-opt-2.7b ### The closest model vllm already supports. https://huggingface.co/liuhaotian/llava-v1.5-7b ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: u want? Support for Llava 1.5 was recently added. Blip2 has a different architecture which is currently not supported.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
