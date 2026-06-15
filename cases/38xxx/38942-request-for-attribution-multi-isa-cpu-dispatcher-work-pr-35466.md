# vllm-project/vllm#38942: Request for attribution: Multi-ISA CPU dispatcher work (PR #35466)

| 字段 | 值 |
| --- | --- |
| Issue | [#38942](https://github.com/vllm-project/vllm/issues/38942) |
| 状态 | open |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Request for attribution: Multi-ISA CPU dispatcher work (PR #35466)

### Issue 正文摘录

# Attribution Report: Multi-ISA CPU Dispatcher Contribution **Prepared by**: Mohammad Mekayel Anik ([@MekayelAnik](https://github.com/MekayelAnik)) **Date**: 2026-04-04 **Regarding**: Unattributed use of prior work in vllm-project/vllm#35466 --- ## Summary My original work on a Python dispatcher for multi-ISA CPU support — contributed to [dtrifiro/vllm PR #9](https://github.com/dtrifiro/vllm/pull/9) in December 2025 — was used without attribution in [vllm-project/vllm PR #35466](https://github.com/vllm-project/vllm/pull/35466), merged on 2026-02-28. A clear lineage exists through an intermediate PR ([#35346](https://github.com/vllm-project/vllm/pull/35346)) that explicitly rebased my commits, was closed, and replaced the next day with a reimplementation that gave no credit. --- ## Timeline of Events ### 1. Original Contribution — December 2025 | Detail | Value | |--------|-------| | **Repository** | [dtrifiro/vllm](https://github.com/dtrifiro/vllm) | | **PR** | [#9 — "fix: Add Python dispatcher for multi-ISA CPU support"](https://github.com/dtrifiro/vllm/pull/9) | | **Author** | MekayelAnik (MD. MEKAYEL ANIK) | | **Created** | 2025-12-19 | | **Merged** | 2025-12-22 (into `cpu-buil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: PR ([#35346](https://github.com/vllm-project/vllm/pull/35346)) that explicitly rebased my commits, was closed, and replaced the next day with a reimplementation that gave no credit. --- ## Timeline of Events ### 1. Orig...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Request for attribution: Multi-ISA CPU dispatcher work (PR #35466) # Attribution Report: Multi-ISA CPU Dispatcher Contribution **Prepared by**: Mohammad Mekayel Anik ([@MekayelAnik](https://github.com/MekayelAnik)) **Da...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nup"* - This PR **directly contains all 3 of my commits** with my authorship preserved - My file `vllm/_ops_dispatch.py` is included in this PR - All commits are re-signed as `Signed-off-by: Ma Jian ` but retain my orig...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ps._C, ...)` checks with `has_op()` across compilation, distributed, and model executor files **Problem solved:** The two CPU extensions (`_C.so` for AVX2/generic and `_C_avx512.so` for AVX512) registered to different `...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: | **Dispatch mechanism** | Python-level dispatcher (`_ops_dispatch.py`) routing `torch.ops._C.*` calls to correct namespace at runtime | C++ level: `#define TORCH_EXTENSION_NAME _C` forces both extensions to register un...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
