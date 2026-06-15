# vllm-project/vllm#4509: [Bug] FP8 MoE performance regression since updating to torch 2.3.0

| 字段 | 值 |
| --- | --- |
| Issue | [#4509](https://github.com/vllm-project/vllm/issues/4509) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | fp8;kernel;moe |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] FP8 MoE performance regression since updating to torch 2.3.0

### Issue 正文摘录

### Your current environment H100 80GB, torch 2.3.0 ### 🐛 Describe the bug Since https://github.com/vllm-project/vllm/pull/4454, the performance on the FP8 MoE kernel has been pretty bad. On FP8, for qps 6 (1000 input, 50 output tokens) and static activation scales on H100, the mixtral 8x7b ITL goes from 12ms to over 40ms.

## 现有链接修复摘要

#5327 [MISC] Upgrade dependency to PyTorch 2.3.1

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug] FP8 MoE performance regression since updating to torch 2.3.0 bug ### Your current environment H100 80GB, torch 2.3.0 ### 🐛 Describe the bug Since https://github.com/vllm-project/vllm/pull/4454, the performance on...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s. performance activation_norm;moe;quantization fp8;kernel;moe dtype;env_dependency #5327 [MISC] Upgrade dependency to PyTorch 2.3.1 Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gression since updating to torch 2.3.0 bug ### Your current environment H100 80GB, torch 2.3.0 ### 🐛 Describe the bug Since https://github.com/vllm-project/vllm/pull/4454, the performance on the FP8 MoE kernel has been...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug] FP8 MoE performance regression since updating to torch 2.3.0 bug ### Your current environment H100 80GB, torch 2.3.0 ### 🐛 Describe the bug Since https://github.com/vllm-project/vllm/pull/4454, the performance on...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug] FP8 MoE performance regression since updating to torch 2.3.0 bug ### Your current environment H100 80GB, torch 2.3.0 ### 🐛 Describe the bug Since https://github.com/vllm-project/vllm/pull/4454, the performance on...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5327](https://github.com/vllm-project/vllm/pull/5327) | closes_keyword | 0.95 | [MISC] Upgrade dependency to PyTorch 2.3.1 | FIX #4509 FIX #5535 FIX #5579 FIX #5705 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
