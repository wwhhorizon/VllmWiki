# vllm-project/vllm#38772: [Feature]: General LL GEMMs with PDL Support

| 字段 | 值 |
| --- | --- |
| Issue | [#38772](https://github.com/vllm-project/vllm/issues/38772) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: General LL GEMMs with PDL Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We currently have two highly specialized low latency GEMMS that support PDL after AR - `dsv3_a_gemm`: https://github.com/vllm-project/vllm/blob/6241521dd2751b036d43d4bfc965f68319c32068/csrc/dsv3_fused_a_gemm.cu#L46 - `dsv3_router_gemm`: https://github.com/vllm-project/vllm/blob/6241521dd2751b036d43d4bfc965f68319c32068/csrc/moe/dsv3_router_gemm_utils.h#L38 These: - currently only support specific shapes - only support bf16 We should create generalized versions of these low-latency PDL enabled GEMMS, which support: - bf16 - fp8 - nvfp4 - arbitrary shapes ### Alternatives None ### Additional context PDL fix in flashinfer: https://github.com/flashinfer-ai/flashinfer/issues/2887 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ls.h#L38 These: - currently only support specific shapes - only support bf16 We should create generalized versions of these low-latency PDL enabled GEMMS, which support: - bf16 - fp8 - nvfp4 - arbitrary shapes ### Alter...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: General LL GEMMs with PDL Support feature request ### 🚀 The feature, motivation and pitch We currently have two highly specialized low latency GEMMS that support PDL after AR - `dsv3_a_gemm`: https://github.c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### 🚀 The feature, motivation and pitch We currently have two highly specialized low latency GEMMS that support PDL after AR - `dsv3_a_gemm`: https://github.com/vllm-project/vllm/blob/6241521dd2751b036d43d4bfc965f68319c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ture, motivation and pitch We currently have two highly specialized low latency GEMMS that support PDL after AR - `dsv3_a_gemm`: https://github.com/vllm-project/vllm/blob/6241521dd2751b036d43d4bfc965f68319c32068/csrc/ds...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: trary shapes ### Alternatives None ### Additional context PDL fix in flashinfer: https://github.com/flashinfer-ai/flashinfer/issues/2887 ### Before submitting a new issue... - [x] Make sure you already searched for rele...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
