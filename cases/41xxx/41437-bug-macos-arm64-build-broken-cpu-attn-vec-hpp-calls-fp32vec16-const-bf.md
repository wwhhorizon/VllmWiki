# vllm-project/vllm#41437: [Bug]: macOS arm64 build broken — `cpu_attn_vec.hpp` calls `FP32Vec16(const BF16Vec32&, int)` constructor that doesn't exist on ARM (regression from #39445)

| 字段 | 值 |
| --- | --- |
| Issue | [#41437](https://github.com/vllm-project/vllm/issues/41437) |
| 状态 | open |
| 标签 | cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: macOS arm64 build broken — `cpu_attn_vec.hpp` calls `FP32Vec16(const BF16Vec32&, int)` constructor that doesn't exist on ARM (regression from #39445)

### Issue 正文摘录

### Your current environment - OS: macOS 26.3.1 (arm64, Apple Silicon) - Compiler: Apple clang 21.0.0 - Python: 3.12.13 (uv-managed venv) - torch: 2.11.0 - vLLM commit: `9c61864bf` (current `main` HEAD as of filing) - `VLLM_TARGET_DEVICE`: auto-routed to `cpu` per `setup.py:42-44` ### 🐛 Describe the bug Building from source on macOS arm64 (`uv pip install -e .`) fails with the following compiler errors in `csrc/cpu/cpu_attn_vec.hpp`: ``` csrc/cpu/cpu_attn_vec.hpp:23:13: error: no matching constructor for initialization of 'vec_op::FP32Vec16' 23 | return {vec_op::FP32Vec16(bf16_b_reg, 0), vec_op::FP32Vec16(bf16_b_reg, 1)}; csrc/cpu/cpu_attn_vec.hpp:27:13: error: no matching constructor for initialization of 'vec_op::FP32Vec16' 27 | return {vec_op::FP32Vec16(bf16_b_reg, 0), vec_op::FP32Vec16(bf16_b_reg, 1)}; ``` (There are 4 errors total — one per `FP32Vec16(bf16_b_reg, N)` call across lines 23 and 27.) ### Root cause `csrc/cpu/cpu_attn_vec.hpp` (introduced/expanded by #39445, [22524f7a9](https://github.com/vllm-project/vllm/commit/22524f7a9)) calls: ```cpp vec_op::FP32Vec16(bf16_b_reg, 0) ``` where `bf16_b_reg` is a `vec_op::BF16Vec32`. This requires a constructor with signature: `...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: macOS arm64 build broken — `cpu_attn_vec.hpp` calls `FP32Vec16(const BF16Vec32&, int)` constructor that doesn't exist on ARM (regression from #39445) cpu ### Your current environment - OS: macOS 26.3.1 (arm64, Ap...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: g]: macOS arm64 build broken — `cpu_attn_vec.hpp` calls `FP32Vec16(const BF16Vec32&, int)` constructor that doesn't exist on ARM (regression from #39445) cpu ### Your current environment - OS: macOS 26.3.1 (arm64, Apple...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ard around the FP8 KV-cache code path that uses this constructor. Other backends (`cpu_types_neon.hpp`, `cpu_types_vsx.hpp`, `cpu_types_arm.hpp`, `cpu_types_s390x.hpp`) likely have the same gap, but ARM is the one I can...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: cpu_types_s390x.hpp`) likely have the same gap, but ARM is the one I can reproduce on. ### Reproduction ```bash git clone https://github.com/vllm-project/vllm.git cd vllm uv venv --python 3.12 uv pip install -r requirem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tors. ### Before submitting a new issue... - [x] Make sure I already searched for relevant issues — no existing issue mentions `cpu_attn_vec.hpp` or this regression.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
