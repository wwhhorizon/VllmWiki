# vllm-project/vllm#3411: Gemma implementation should use approximate GELU

| 字段 | 值 |
| --- | --- |
| Issue | [#3411](https://github.com/vllm-project/vllm/issues/3411) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Gemma implementation should use approximate GELU

### Issue 正文摘录

Based on the [unsloth.ai blog #8](https://unsloth.ai/blog/gemma-bugs) as well as discussion with @pengchongjin from the Gemma team, the Gemma implementation in vLLM should switch to using tanh approximation rather than exact (code ref [1](https://github.com/vllm-project/vllm/blob/8fe838659164b415d7f3044ec6b7e5bc52c6b6a5/vllm/model_executor/layers/activation.py#L50), [2](https://github.com/vllm-project/vllm/blob/06ec486794f42db656c3cc16c8c5ed56ce4f696b/vllm/model_executor/models/gemma.py#L63)).

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Gemma implementation should use approximate GELU Based on the [unsloth.ai blog #8](https://unsloth.ai/blog/gemma-bugs) as well as discussion with @pengchongjin from the Gemma team, the Gemma implementation in vLLM should
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Gemma implementation should use approximate GELU Based on the [unsloth.ai blog #8](https://unsloth.ai/blog/gemma-bugs) as well as discussion with @pengchongjin from the Gemma team, the Gemma implementation in vLLM shoul...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Gemma implementation should use approximate GELU Based on the [unsloth.ai blog #8](https://unsloth.ai/blog/gemma-bugs) as well as discussion with @pengchongjin from the Gemma team, the Gemma implementation in vLLM should

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
