# vllm-project/vllm#3245: Is there a ModelList that supports LoRA adapter?

| 字段 | 值 |
| --- | --- |
| Issue | [#3245](https://github.com/vllm-project/vllm/issues/3245) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there a ModelList that supports LoRA adapter?

### Issue 正文摘录

ValueError: Model ChatGLMForCausalLM does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. Where can I find information about which models are supported? And is there a schedule for adapting models?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Is there a ModelList that supports LoRA adapter? ValueError: Model ChatGLMForCausalLM does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please op...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. Where can I find information about which models are supported? And is there a schedule for adapt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
