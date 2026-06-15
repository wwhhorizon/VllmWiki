# vllm-project/vllm#41537: [Build] CPU extension fails to compile on macOS ARM64 (Apple Silicon)

| 字段 | 值 |
| --- | --- |
| Issue | [#41537](https://github.com/vllm-project/vllm/issues/41537) |
| 状态 | open |
| 标签 | cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Build] CPU extension fails to compile on macOS ARM64 (Apple Silicon)

### Issue 正文摘录

## Description Building vLLM's CPU backend from source on macOS ARM64 (Apple Silicon) fails with two compilation errors: ### 1. C++20 structured bindings captured in lambdas `csrc/cpu/cpu_attn_vec.hpp:105` uses C++20 structured bindings captured in lambdas: ```cpp auto [fp32_b_0_reg, fp32_b_1_reg] = load_b_pair_vec(curr_b); vec_op::unroll_loop ([&](int32_t i) { // fp32_b_0_reg and fp32_b_1_reg captured here — requires C++20 c_regs[i * 2] = c_regs[i * 2] + a_reg * fp32_b_0_reg; c_regs[i * 2 + 1] = c_regs[i * 2 + 1] + a_reg * fp32_b_1_reg; }); ``` GCC allows this as an extension in C++17 mode, but Clang (used on macOS) rejects it with: ``` warning: captured structured bindings are a C++20 extension [-Wc++20-extensions] ``` ### 2. Missing `FP32Vec16(const BF16Vec32&, int)` constructor on ARM `csrc/cpu/cpu_attn_vec.hpp:23` calls `FP32Vec16(bf16_b_reg, 0)` and `FP32Vec16(bf16_b_reg, 1)`, but this two-argument constructor only exists in `cpu_types_x86.hpp`, not in `cpu_types_arm.hpp`: ``` error: no matching constructor for initialization of 'vec_op::FP32Vec16' ``` ## Steps to reproduce ```bash # On macOS ARM64 (Apple Silicon) with Python 3.12 uv pip install --editable . --torch-backend=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Build] CPU extension fails to compile on macOS ARM64 (Apple Silicon) cpu ## Description Building vLLM's CPU backend from source on macOS ARM64 (Apple Silicon) fails with two compilation errors: ### 1. C++20 structured
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e on macOS ARM64 (Apple Silicon) cpu ## Description Building vLLM's CPU backend from source on macOS ARM64 (Apple Silicon) fails with two compilation errors: ### 1. C++20 structured bindings captured in lambdas `csrc/cp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: g constructor for initialization of 'vec_op::FP32Vec16' ``` ## Steps to reproduce ```bash # On macOS ARM64 (Apple Silicon) with Python 3.12 uv pip install --editable . --torch-backend=auto ``` ## Environment - macOS (Ap...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ++20 extension [-Wc++20-extensions] ``` ### 2. Missing `FP32Vec16(const BF16Vec32&, int)` constructor on ARM `csrc/cpu/cpu_attn_vec.hpp:23` calls `FP32Vec16(bf16_b_reg, 0)` and `FP32Vec16(bf16_b_reg, 1)`, but this two-a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
