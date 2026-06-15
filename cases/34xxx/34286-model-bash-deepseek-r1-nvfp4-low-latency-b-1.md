# vllm-project/vllm#34286: [Model Bash]: DeepSeek R1 NVFP4 Low Latency (B=1)

| 字段 | 值 |
| --- | --- |
| Issue | [#34286](https://github.com/vllm-project/vllm/issues/34286) |
| 状态 | open |
| 标签 | feature request;model-bash |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model Bash]: DeepSeek R1 NVFP4 Low Latency (B=1)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Based on some profiling by @alexm-redhat, there are a few optimizations for low-latency serving that we could use. - [x] Turn on AR fusion by default (https://github.com/vllm-project/vllm/pull/34299, requires bugfix from FI for TRTLLM NVFP4: https://github.com/flashinfer-ai/flashinfer/pull/2557/changes --- turn back on for DSR1 after FI 0.6.4) - [ ] PDL for AR+RMS + the first attention gemm (as done by sgl) - [ ] PDL for AR+RMS + the router gemm (as done by sgl) - [x] Remove Clone from Shared Experts Stream (https://github.com/vllm-project/vllm/pull/34344) - [x] Remove Bias Casts in TRTLLM NVFP4 MoE Kernel (https://github.com/vllm-project/vllm/pull/34298) - [x] Remove Logits Casts in TRTLLM NVFP4 MoE Kernel (https://github.com/vllm-project/vllm/pull/34302) - [x] Investigate passing unquantized inputs to the TRTLLM NVFP4 MoE Kernel ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: k on for DSR1 after FI 0.6.4) - [ ] PDL for AR+RMS + the first attention gemm (as done by sgl) - [ ] PDL for AR+RMS + the router gemm (as done by sgl) - [x] Remove Clone from Shared Experts Stream (https://github.com/vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Model Bash]: DeepSeek R1 NVFP4 Low Latency (B=1) feature request;model-bash ### 🚀 The feature, motivation and pitch Based on some profiling by @alexm-redhat, there are a few optimizations for low-latency serving that w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Model Bash]: DeepSeek R1 NVFP4 Low Latency (B=1) feature request;model-bash ### 🚀 The feature, motivation and pitch Based on some profiling by @alexm-redhat, there are a few optimizations for low-latency serving that w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pull/34299, requires bugfix from FI for TRTLLM NVFP4: https://github.com/flashinfer-ai/flashinfer/pull/2557/changes --- turn back on for DSR1 after FI 0.6.4) - [ ] PDL for AR+RMS + the first attention gemm (as done by s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
