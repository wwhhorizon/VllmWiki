# vllm-project/vllm#40259: [Bug]: v0.19.1 Crash with CUDA invalid argument / Segfault when using KV Offloading + EAGLE3 + Expert Parallel (on 8x H20 141GB)

| 字段 | 值 |
| --- | --- |
| Issue | [#40259](https://github.com/vllm-project/vllm/issues/40259) |
| 状态 | open |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.19.1 Crash with CUDA invalid argument / Segfault when using KV Offloading + EAGLE3 + Expert Parallel (on 8x H20 141GB)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment - **vLLM version:** v0.19.1 (docker: `vllm/vllm-openai:v0.19.1`) *Note: Host environment has v0.12.0, but bug is reproduced in v0.19.1 container* - **Hardware:** 8× NVIDIA H20-3e (141GB) — Total VRAM ~1.1TB - **CPU:** 2× Intel Xeon Platinum 8558 (192 cores, 2 NUMA nodes) - **System:** 2TB RAM, Ubuntu 22.04, NVIDIA Driver 570.86.15, CUDA 12.6/12.8 - **Interconnect:** NV18 (18 NVLinks) fully connected mesh - **Model:** moonshot-ai/Kimi-K2.5 (compressed-tensors, ~72GB) - **Draft model:** moonshot-ai/Kimi-K2.5-Eagle3 (EAGLE3 speculative decoding) ### Problem Description When running Kimi-K2.5 with **EAGLE3 speculative decoding** and **Expert Parallel (EP)** enabled, the presence of `--kv-offloading-size` causes a **fatal cascade failure** (segfault → NVLink corruption → distributed crash) once context length exceeds the configured GPU block limit. **Critical observation:** With 8× H20-3e (1.1TB+ VRAM available after model weights), the system should never need offloading for 32K context. Instead of graceful operation, the configuration triggers memory corruption. ### Reproduction Command ```bash docker run --rm -it \...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: current environment ### 🐛 Describe the bug ### Environment - **vLLM version:** v0.19.1 (docker: `vllm/vllm-openai:v0.19.1`) *Note: Host environment has v0.12.0, but bug is reproduced in v0.19.1 container* - **Hardware:*...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: v0.19.1 Crash with CUDA invalid argument / Segfault when using KV Offloading + EAGLE3 + Expert Parallel (on 8x H20 141GB) bug ### Your current environment ### 🐛 Describe the bug ### Environment - **vLLM version:*...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: tion → distributed crash) once context length exceeds the configured GPU block limit. **Critical observation:** With 8× H20-3e (1.1TB+ VRAM available after model weights), the system should never need offloading for 32K...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -config '{"pass_config": {"fuse_allreduce_rms": true}}' \ --kv-cache-dtype fp8 \ --speculative-config '{"model": "/model_files/Kimi-K2.5-Eagle3", "method": "eagle3", "num_speculative_tokens": 3}' \ --gpu-memory-utilizat...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ith CUDA invalid argument / Segfault when using KV Offloading + EAGLE3 + Expert Parallel (on 8x H20 141GB) bug ### Your current environment ### 🐛 Describe the bug ### Environment - **vLLM version:** v0.19.1 (docker: `vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
