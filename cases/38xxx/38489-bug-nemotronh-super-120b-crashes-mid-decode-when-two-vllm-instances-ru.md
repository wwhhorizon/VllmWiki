# vllm-project/vllm#38489: [Bug]: NemotronH Super 120B crashes mid-decode when two vLLM instances run concurrently on AGX Thor unified memory

| 字段 | 值 |
| --- | --- |
| Issue | [#38489](https://github.com/vllm-project/vllm/issues/38489) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;fp8;gemm;kernel;moe;quantization |
| 症状 | build_error;crash;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NemotronH Super 120B crashes mid-decode when two vLLM instances run concurrently on AGX Thor unified memory

### Issue 正文摘录

### Your current environment Component: vLLM — NemotronH model implementation / CUDA memory management on unified memory architectures Severity: Fatal — engine crash, complete loss of in-flight response Reproducibility: Consistent under concurrent dual-model load; does NOT reproduce solo under equivalent memory pressure Context (read this first) NVIDIA AGX Thor is an edge AI developer kit with 122.8 GiB of unified memory — CPU and GPU share the same physical DRAM pool. Running two inference servers on this hardware is a natural and intended use case: a large "reasoning" model for complex tasks alongside a smaller "fast" model for interactive use. I'm running NemotronH Super 120B NVFP4 (vLLM, port 8000) alongside Nemotron Nano 30B NVFP4 (vLLM, port 8001). When both models generate responses simultaneously — triggered via Open WebUI's side-by-side comparison mode — Super crashes mid-decode with CUDA error: an illegal instruction was encountered . Nano is never affected. The key finding that makes this worth investigating: the crash does NOT reproduce when Super runs solo under equivalent or greater memory pressure. I ran Super solo at --gpu-memory-utilization 0.88 (leaving the same...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: ler "fast" model for interactive use. I'm running NemotronH Super 120B NVFP4 (vLLM, port 8000) alongside Nemotron Nano 30B NVFP4 (vLLM, port 8001). When both models generate responses simultaneously — triggered via Open...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: / JetPack 7.2 CUDA | 13.2 OS | Ubuntu 24.04 aarch64 (SBSA) vLLM | 0.19.0 FlashInfer | 0.6.7 Container | jetson-containers vLLM build Models Super (crashes): Model: Nemotron-H Super 120B NVFP4+FP8 checkpoint Quantization...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rrent environment Component: vLLM — NemotronH model implementation / CUDA memory management on unified memory architectures Severity: Fatal — engine crash, complete loss of in-flight response Reproducibility: Consistent...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: Reproducibility: Consistent under concurrent dual-model load; does NOT reproduce solo under equivalent memory pressure Context (read this first) NVIDIA AGX Thor is an edge AI developer kit with 122.8 GiB of unified memo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ity: Fatal — engine crash, complete loss of in-flight response Reproducibility: Consistent under concurrent dual-model load; does NOT reproduce solo under equivalent memory pressure Context (read this first) NVIDIA AGX...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
