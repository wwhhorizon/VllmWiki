# vllm-project/vllm#37242: [Community] RTX 5090 (Blackwell sm_120) + WSL2 2.7.0: CUDA graphs work — benchmarks + full config

| 字段 | 值 |
| --- | --- |
| Issue | [#37242](https://github.com/vllm-project/vllm/issues/37242) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;kernel;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Community] RTX 5090 (Blackwell sm_120) + WSL2 2.7.0: CUDA graphs work — benchmarks + full config

### Issue 正文摘录

# RTX 5090 + WSL2 2.7.0: vLLM CUDA Graphs Work on Blackwell (Benchmarks + Full Config) **TL;DR:** CUDA graph capture works on RTX 5090 (sm_120 Blackwell) under WSL2 2.7.0 — something widely believed to be permanently broken. With the right config, vLLM hits **~140 tok/s on Qwen3-14B-AWQ**, beating Ollama by 26% and 8x faster than enforce-eager mode. --- ## Hardware & Software - **GPU:** RTX 5090 32GB GDDR7 (sm_120, Blackwell) - **OS:** Windows 11 + WSL2 2.7.0 (pre-release), Ubuntu 22.04 - **Kernel:** 6.6.114.1-microsoft-standard-WSL2 - **CUDA:** 12.8, driver 581.80 - **vLLM:** 0.17.1 - **Model:** Qwen/Qwen3-14B-AWQ (awq_marlin quantization) --- ## The Problem Everyone Hit Running vLLM on RTX 5090 + WSL2 caused a hard crash during CUDA graph capture: ``` cudaErrorUnknown: unknown error ``` The community consensus was this was a permanent WSL2 limitation with Blackwell sm_120 — the dxgkrnl Hyper-V GPU virtualization layer not supporting CUDA graph capture on the new architecture. Most workarounds used `--enforce-eager` which disables CUDA graphs entirely. ## What Actually Fixed It WSL2 **2.7.0** (pre-release, December 2025) shipped significant dxgkrnl improvements for Blackwell. But...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Community] RTX 5090 (Blackwell sm_120) + WSL2 2.7.0: CUDA graphs work — benchmarks + full config # RTX 5090 + WSL2 2.7.0: vLLM CUDA Graphs Work on Blackwell (Benchmarks + Full Config) **TL;DR:** CUDA graph capture work...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: be stable — the CUDA graph crash is easily triggered by other services racing for the GPU at boot. **Root causes we found and fixed:** **1. Tailscale in WSL2** — intercepts network at boot, interferes with CUDA initiali...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: er 581.80 - **vLLM:** 0.17.1 - **Model:** Qwen/Qwen3-14B-AWQ (awq_marlin quantization) --- ## The Problem Everyone Hit Running vLLM on RTX 5090 + WSL2 caused a hard crash during CUDA graph capture: ``` cudaErrorUnknown:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 90 (Blackwell sm_120) + WSL2 2.7.0: CUDA graphs work — benchmarks + full config # RTX 5090 + WSL2 2.7.0: vLLM CUDA Graphs Work on Blackwell (Benchmarks + Full Config) **TL;DR:** CUDA graph capture works on RTX 5090 (sm_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ls back to an emulated path. Skip FP8 until MS ships dxgkrnl support. **Speculative decoding with draft model:** Generic Qwen3-1.7B as draft gives only 1.4% acceptance rate (need 70%+ to break even). No Qwen3-14B EAGLE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
