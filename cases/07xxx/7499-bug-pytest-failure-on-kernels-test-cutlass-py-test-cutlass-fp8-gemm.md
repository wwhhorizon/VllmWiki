# vllm-project/vllm#7499: [Bug]: pytest failure on kernels/test_cutlass.py test_cutlass_fp8_gemm

| 字段 | 值 |
| --- | --- |
| Issue | [#7499](https://github.com/vllm-project/vllm/issues/7499) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | gemm_linear |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pytest failure on kernels/test_cutlass.py test_cutlass_fp8_gemm

### Issue 正文摘录

### Your current environment GPU: L40 CUDA version: 12.4 Driver version: 550.90.07 ### 🐛 Describe the bug All pytests fail and large gap between cutlass and torch._scaled_mm

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: y test_cutlass_fp8_gemm bug ### Your current environment GPU: L40 CUDA version: 12.4 Driver version: 550.90.07 ### 🐛 Describe the bug All pytests fail and large gap between cutlass and torch._scaled_mm development gemm_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: pytest failure on kernels/test_cutlass.py test_cutlass_fp8_gemm bug ### Your current environment GPU: L40 CUDA version: 12.4 Driver version: 550.90.07 ### 🐛 Describe the bug All pytests fail and large gap between...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: pytest failure on kernels/test_cutlass.py test_cutlass_fp8_gemm bug ### Your current environment GPU: L40 CUDA version: 12.4 Driver version: 550.90.07 ### 🐛 Describe the bug All pytests fail and large gap between...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ass.py test_cutlass_fp8_gemm bug ### Your current environment GPU: L40 CUDA version: 12.4 Driver version: 550.90.07 ### 🐛 Describe the bug All pytests fail and large gap between cutlass and torch._scaled_mm development...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: pytest failure on kernels/test_cutlass.py test_cutlass_fp8_gemm bug ### Your current environment GPU: L40 CUDA version: 12.4 Driver version: 550.90.07 ### 🐛 Describe the bug All pytests fail and large gap between...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
