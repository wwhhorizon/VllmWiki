# vllm-project/vllm#39809: [Bug]: Mamba prefix caching + MTP speculative decoding crashes on startup for NemotronH models

| 字段 | 值 |
| --- | --- |
| Issue | [#39809](https://github.com/vllm-project/vllm/issues/39809) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mamba prefix caching + MTP speculative decoding crashes on startup for NemotronH models

### Issue 正文摘录

### Your current environment - vLLM version: 0.19.0 (official Docker image `vllm/vllm-openai:v0.19.0`) - GPU: NVIDIA B200 (178 GB VRAM), tested TP=1 through TP=8 - Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` (NemotronH hybrid Mamba2-Transformer MoE) - Python: 3.12 ### Model/config ```bash vllm serve nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --dtype bfloat16 \ --trust-remote-code \ --gpu-memory-utilization 0.90 \ --max-model-len 21525 \ --tensor-parallel-size 4 \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' ``` Key flags: `--enable-prefix-caching` + `--speculative-config` with MTP on a hybrid model that declares `SupportsMambaPrefixCaching`. ### 🐛 Describe the bug Enabling both prefix caching (`mamba_cache_mode="all"`) and MTP speculative decoding on NemotronH (hybrid Mamba2 architecture) causes three cascading bugs during cudagraph profiling at startup. Each bug manifests only after patching the previous one. **Without MTP, prefix caching works correctly.** All Nano-30B configs (no MTP) pass with 120/120 valid results. The bugs are specific to the combination of `SupportsMambaPrefixCaching...

## 现有链接修复摘要

#41233 [Bugfix][Hybrid][NemotronH] Fix mamba_cache_mode=all + speculative decoding crash

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: ted TP=1 through TP=8 - Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` (NemotronH hybrid Mamba2-Transformer MoE) - Python: 3.12 ### Model/config ```bash vllm serve nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Mamba prefix caching + MTP speculative decoding crashes on startup for NemotronH models bug ### Your current environment - vLLM version: 0.19.0 (official Docker image `vllm/vllm-openai:v0.19.0`) - GPU: NVIDIA B20...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: on startup for NemotronH models bug ### Your current environment - vLLM version: 0.19.0 (official Docker image `vllm/vllm-openai:v0.19.0`) - GPU: NVIDIA B200 (178 GB VRAM), tested TP=1 through TP=8 - Model: `nvidia/NVID...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 0.19.0 (official Docker image `vllm/vllm-openai:v0.19.0`) - GPU: NVIDIA B200 (178 GB VRAM), tested TP=1 through TP=8 - Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` (NemotronH hybrid Mamba2-Transformer MoE) -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: cker image `vllm/vllm-openai:v0.19.0`) - GPU: NVIDIA B200 (178 GB VRAM), tested TP=1 through TP=8 - Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` (NemotronH hybrid Mamba2-Transformer MoE) - Python: 3.12 ### Mo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41233](https://github.com/vllm-project/vllm/pull/41233) | closes_keyword | 0.95 | [Bugfix][Hybrid][NemotronH] Fix mamba_cache_mode=all + speculative decoding crash | Fixes the chain of three bugs reported in #39809 that crash NemotronH (and other hybrid Mamba2) models when prefix caching `all` mode is combined with speculative decoding. This |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
