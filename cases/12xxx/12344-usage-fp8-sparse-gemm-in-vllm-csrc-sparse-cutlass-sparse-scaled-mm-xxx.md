# vllm-project/vllm#12344: [Usage]: fp8 sparse gemm in vllm/csrc/sparse/cutlass/sparse_scaled_mm__xxx

| 字段 | 值 |
| --- | --- |
| Issue | [#12344](https://github.com/vllm-project/vllm/issues/12344) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: fp8 sparse gemm in vllm/csrc/sparse/cutlass/sparse_scaled_mm__xxx

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm In the three implementation files of fp8 sparse gemm vllm/csrc/sparse/cutlass/sparse_scaled_mm__xxx. 1. Can you abstract the implementation formula of cutlass_scaled_sparse_mm_sm90? 2. 2. In addition, I understand that bt_nzs bt_meta is the data after gemm weight sparse (from sparse_compressor_xxx), what are the arrangements of the three tensors bt_nzs, a and c respectively (in ColumnMajor RowMajor)? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: fp8 sparse gemm in vllm/csrc/sparse/cutlass/sparse_scaled_mm__xxx usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm In the three implementat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Can you abstract the implementation formula of cutlass_scaled_sparse_mm_sm90? 2. 2. In addition, I understand that bt_nzs bt_meta is the data after gemm weight sparse (from sparse_compressor_xxx), what are the arrangeme...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: fp8 sparse gemm in vllm/csrc/sparse/cutlass/sparse_scaled_mm__xxx usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm In the three implementat...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: fp8 sparse gemm in vllm/csrc/sparse/cutlass/sparse_scaled_mm__xxx usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm In the three implementat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
