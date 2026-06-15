# vllm-project/vllm#32412: [RFC]: online quantization user facing API

| 字段 | 值 |
| --- | --- |
| Issue | [#32412](https://github.com/vllm-project/vllm/issues/32412) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: online quantization user facing API

### Issue 正文摘录

### Motivation. Online quantization (weights passed to vLLM in high precision, quantization of weights done inside of vLLM) is emerging as an important use case for quick experimentation and RL. Today vLLM supports online quantization with a single recipe (float8 per-tensor scaling). Let's align how to extend the user API for specifying other online quant recipes. Today, the main user API for fp8 online quant is --quantization="fp8", which defaults to float8 tensorwise scaling for all linear and moe layers. There is no ability to specify scaling type, no ability to ignore layers, no ability to specify other dtypes for weights or activations: ```python # current API LLM(..., quantization="fp8", ...,) ``` See https://github.com/vllm-project/vllm/issues/32029 for more context on online quantization roadmap ### Proposed Change tl;dr; 1. add a new frontend for online quantization, `LLM(..., quantization="fp8_blockwise", ...)`, with enough expressivity to support important use cases for online quant in 2026 such as selecting different quant schemes by layer type (all layers vs `LinearBase` vs `FusedMoE`, and skipping layers. The existing online quantization frontends (fp8.py, etc) will...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [RFC]: online quantization user facing API RFC ### Motivation. Online quantization (weights passed to vLLM in high precision, quantization of weights done inside of vLLM) is emerging as an important use case for quick e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ontend ```python # # 1. new top-level arguments to the `LLM` object for configuring online quantization: # # 1a: turn on online quantization with the `quantization` argument only, passing in a global quant scheme LLM(.....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: online quantization user facing API RFC ### Motivation. Online quantization (weights passed to vLLM in high precision, quantization of weights done inside of vLLM) is emerging as an important use case for quick e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: add a new frontend for online quantization, `LLM(..., quantization="fp8_blockwise", ...)`, with enough expressivity to support important use cases for online quant in 2026 such as selecting different quant schemes by la...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: on="fp8", which defaults to float8 tensorwise scaling for all linear and moe layers. There is no ability to specify scaling type, no ability to ignore layers, no ability to specify other dtypes for weights or activation...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
