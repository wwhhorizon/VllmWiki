# vllm-project/vllm#37979: [RFC]: Intel Quantization Support Roadmap (H1 2026)

| 字段 | 值 |
| --- | --- |
| Issue | [#37979](https://github.com/vllm-project/vllm/issues/37979) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Intel Quantization Support Roadmap (H1 2026)

### Issue 正文摘录

## Status ### Scheme Status | Scheme | Module | Intel GPU | CPU | |--------|--------|-----|-----| | wNa16 INT (W4A16) | Linear | :white_check_mark: Merged [#37986](https://github.com/vllm-project/vllm/pull/37986) | :white_check_mark: Merged [#38192](https://github.com/vllm-project/vllm/pull/38192) | | wNa16 INT (W4A16, ARK) | Linear | :mag: Review [#39778](https://github.com/vllm-project/vllm/pull/39778) | :mag: Review [#39778](https://github.com/vllm-project/vllm/pull/39778) | | wNa16 INT (W4A16) | MoE | :clipboard: Planned | :clipboard: Planned | | w4a4 MXFP4 | Linear | WIP https://github.com/yiliu30/vllm-fork/pull/108 | | #### Architectural Cleanup https://github.com/vllm-project/vllm/pull/40601 ------------------------------------------------------- # Original RFC ## Related RFCs - [Consolidate Intel Quantization Toolkit Integration in vLLM](https://github.com/vllm-project/vllm/issues/30663) - [XPU Kernel Migration to vllm-xpu-kernels](https://github.com/vllm-project/vllm/issues/33214) - [Deprecate Legacy Quantization Formats](https://github.com/vllm-project/vllm/issues/30136) ## Motivation Previously, we merged `auto_round.py` into `inc.py` as the unified Intel quantization b...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC]: Intel Quantization Support Roadmap (H1 2026) RFC ## Status ### Scheme Status | Scheme | Module | Intel GPU | CPU | |--------|--------|-----|-----| | wNa16 INT (W4A16) | Linear | :white_check_mark: Merged [#37986]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e merged `auto_round.py` into `inc.py` as the unified Intel quantization backend. The `vllm-xpu-kernels` replacement for IPEX is a work in progress. This H1 2026 roadmap covers completing the consolidation, migrating fr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: https://github.com/vllm-project/vllm/pull/39778) | | wNa16 INT (W4A16) | MoE | :clipboard: Planned | :clipboard: Planned | | w4a4 MXFP4 | Linear | WIP https://github.com/yiliu30/vllm-fork/pull/108 | | #### Architectural...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hub.com/vllm-project/vllm/issues/33214) - [Deprecate Legacy Quantization Formats](https://github.com/vllm-project/vllm/issues/30136) ## Motivation Previously, we merged `auto_round.py` into `inc.py` as the unified Intel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: scheme and delegates to the correct Level 2 impl. **Level 2 — Scheme-specific impl** (e.g. `AutoRoundWNA16LinearImpl`, `AutoRoundFP8LinearImpl`): Implements an abstract `AutoRoundQuantImpl` base class that defines `crea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
