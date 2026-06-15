# vllm-project/vllm#42096: [Performance]: Qwen3-VL-235B-A22B-Instruct NVFP4 Performance dropped at upstream main

| 字段 | 值 |
| --- | --- |
| Issue | [#42096](https://github.com/vllm-project/vllm/issues/42096) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;moe;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: Qwen3-VL-235B-A22B-Instruct NVFP4 Performance dropped at upstream main

### Issue 正文摘录

### Proposal to improve performance # Performance regression on Qwen3-VL-235B-A22B-Instruct (NVFP4, GB300 / CUDA 13) — TTFT P99 +55-67%, plus several rough edges in current main ## TL;DR Running Qwen3-VL-235B-A22B-Instruct (NVFP4 via compressed-tensors) on GB300 with TP=4 against the latest upstream nightly (`vllm/vllm-openai:nightly`, vllm `0.20.2rc1.dev93+g51f22dcfd`, May 7 2026, cu130, torch 2.11.0+cu130) shows a significant prefill-path regression vs a fork branched from main near `1cbbcfe8a334bab004c43a60be201c8ab528e0d2` (Mar 23 2026): - **TTFT P99: +55%** (fp8 ViT static scale) to **+67%** (fp8 ViT OFF) - **LAT P99: +28% to +36%** - **TPOT P99: ~0% (slightly faster, −7%)** — decode itself is fine in upstream Plus three smaller papercuts that are worth filing alongside (see "Workarounds needed"). ## Setup - Hardware: GB300 (compute capability 10.0), 4 GPUs, NVLink, NVIDIA driver 580.159.04 - Model: `nvidia/Qwen3-VL-235B-A22B-Instruct-NVFP4-MLPerf-Inference-Closed-V6.0` (compressed-tensors NVFP4) - Workload: online benchmark, target QPS=5 (Poisson), 1000 samples, num_workers=5, mixed multimodal Shopify product-catalogue dataset - Engine config: TP=4, `max_model_len=32768`, `m...

## 现有链接修复摘要

#38061 [MM][Perf][CG] Support ViT full CUDA graph for Qwen3-VL video inference

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Performance]: Qwen3-VL-235B-A22B-Instruct NVFP4 Performance dropped at upstream main performance ### Proposal to improve performance # Performance regression on Qwen3-VL-235B-A22B-Instruct (NVFP4, GB300 / CUDA 13) — TT...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Performance]: Qwen3-VL-235B-A22B-Instruct NVFP4 Performance dropped at upstream main performance ### Proposal to improve performance # Performance regression on Qwen3-VL-235B-A22B-Instruct (NVFP4, GB300 / CUDA 13) — TT...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: ream main performance ### Proposal to improve performance # Performance regression on Qwen3-VL-235B-A22B-Instruct (NVFP4, GB300 / CUDA 13) — TTFT P99 +55-67%, plus several rough edges in current main ## TL;DR Running Qw...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: --max-num-seqs=1024 --max-num-batched-tokens=13824 \ --mm-encoder-attn-backend=FLASHINFER \ --mm-encoder-attn-dtype=fp8 \ --mm-encoder-fp8-scale-path=/tmp/q3vl_fp8_scales.json \ --no-enable-prefix-caching \ --kernel-con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # Performance regression on Qwen3-VL-235B-A22B-Instruct (NVFP4, GB300 / CUDA 13) — TTFT P99 +55-67%, plus several rough edges in current main ## TL;DR Running Qwen3-VL-235B-A22B-Instruct (NVFP4 via compressed-tensors) o...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38061](https://github.com/vllm-project/vllm/pull/38061) | mentioned | 0.45 | [MM][Perf][CG] Support ViT full CUDA graph for Qwen3-VL video inference | ----:\|----------------:\|-----------------:\| \| encoder cudagraph (vllm #38061) \| ~0pp \| ~0pp \| ~0pp \| \| flashinfer 0.6.6 ⇄ 0.6.7 (who |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
