# vllm-project/vllm#14618: [Bug]: Quantization In MambaMixer2 Not Supported when Tensor Parallel is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#14618](https://github.com/vllm-project/vllm/issues/14618) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Quantization In MambaMixer2 Not Supported when Tensor Parallel is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The current implementation for TP for Mamba2 is complicated for the `in_proj`, because the gate, projection, state space, heads, are all fused into this one layer. And furthermore, we also need to consider different possibilities if the number of groups divide the number of heads or not, see https://github.com/vllm-project/vllm/pull/13660. For now the implementation of TP is simplified: - limited to the case of `num_groups == 1` if `num_groups` does not divide `num_heads` [#13660](https://github.com/vllm-project/vllm/pull/13660.). - will does not support TP > 1 if the mamba2 mixer is quantised, see [#14617 ](https://github.com/vllm-project/vllm/pull/14617) However for large models, it may be useful to support TP > 1 with quant layers, even in some special cases of `num_heads` and `num_groups`. cc: @tlrmchlsmth ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: even in some special cases of `num_heads` and `num_groups`. cc: @tlrmchlsmth ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom righ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s, it may be useful to support TP > 1 with quant layers, even in some special cases of `num_heads` and `num_groups`. cc: @tlrmchlsmth ### Before submitting a new issue... - [x] Make sure you already searched for relevan...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Quantization In MambaMixer2 Not Supported when Tensor Parallel is enabled bug;stale ### Your current environment ### 🐛 Describe the bug The current implementation for TP for Mamba2 is complicated for the `in_proj...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 17 ](https://github.com/vllm-project/vllm/pull/14617) However for large models, it may be useful to support TP > 1 with quant layers, even in some special cases of `num_heads` and `num_groups`. cc: @tlrmchlsmth ### Befo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ization In MambaMixer2 Not Supported when Tensor Parallel is enabled bug;stale ### Your current environment ### 🐛 Describe the bug The current implementation for TP for Mamba2 is complicated for the `in_proj`, because t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
