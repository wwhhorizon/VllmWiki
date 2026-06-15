# vllm-project/vllm#30663: [RFC]: Consolidate Intel Quantization Toolkit Integration in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#30663](https://github.com/vllm-project/vllm/issues/30663) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Consolidate Intel Quantization Toolkit Integration in vLLM

### Issue 正文摘录

**Authors**: Intel Neural Compressor Team, Intel vLLM Team **Related**: [RFC: vLLM Quantization Cleanup](https://github.com/vllm-project/vllm/issues/30136) ### Motivation. In alignment with vLLM's quantization consolidation effort, we propose to streamline Intel's quantization support, currently fragmented across three implementations: | File | Scope | Capabilities | | --------------- | ----------------- | -------------------------------------- | | `inc.py` | Intel Gaudi (HPU) | Online W8A8_FP8 quantization | | `auto_round.py` | Intel CPU/GPU | WnA16 (AutoRound models) | | `ipex_quant.py` | Intel CPU/GPU | W4A16,W4A8, W8A16_FP8 via IPEX backend | This fragmentation creates maintenance overhead and inconsistent user experience. Consolidation will: - Reduce code duplication and maintenance burden - Provide a unified entry point for Intel quantization - Enable future formats (`MXFP4`/`MXFP8`/`NVFP4`, and advanced mixed-precision recipes ### Proposed Change. The overall status and proposal are below: #### 1. Consolidate Intel CPU/GPU Quantization → `inc.py` - Merge `auto_round.py` into `inc.py` as unified Intel quantization backend - Extend `inc.py` to support: - `WnA16` inference (fr...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [RFC]: Consolidate Intel Quantization Toolkit Integration in vLLM RFC **Authors**: Intel Neural Compressor Team, Intel vLLM Team **Related**: [RFC: vLLM Quantization Cleanup](https://github.com/vllm-project/vllm/issues/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ion | | `auto_round.py` | Intel CPU/GPU | WnA16 (AutoRound models) | | `ipex_quant.py` | Intel CPU/GPU | W4A16,W4A8, W8A16_FP8 via IPEX backend | This fragmentation creates maintenance overhead and inconsistent user exp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `ipex_quant.py` | Intel CPU/GPU | W4A16,W4A8, W8A16_FP8 via IPEX backend | This fragmentation creates maintenance overhead and inconsistent user experience. Consolidation will: - Reduce code duplication and maintenance...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ion - Enable future formats (`MXFP4`/`MXFP8`/`NVFP4`, and advanced mixed-precision recipes ### Proposed Change. The overall status and proposal are below: #### 1. Consolidate Intel CPU/GPU Quantization → `inc.py` - Merg...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: - Enable future formats (`MXFP4`/`MXFP8`/`NVFP4`, and advanced mixed-precision recipes ### Proposed Change. The overall status and proposal are below: #### 1. Consolidate Intel CPU/GPU Quantization → `inc.py` - Merge `a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
