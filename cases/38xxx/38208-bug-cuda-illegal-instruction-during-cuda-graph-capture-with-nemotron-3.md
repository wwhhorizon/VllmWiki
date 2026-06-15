# vllm-project/vllm#38208: [Bug]: CUDA Illegal Instruction during CUDA Graph capture with Nemotron-3-Nano NVFP4 on sm_121

| 字段 | 值 |
| --- | --- |
| Issue | [#38208](https://github.com/vllm-project/vllm/issues/38208) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Illegal Instruction during CUDA Graph capture with Nemotron-3-Nano NVFP4 on sm_121

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the new NVIDIA Nemotron-3-Nano (Hybrid Mamba-2 + MoE) in NVFP4 format on Blackwell hardware (DGX Spark) results in a fatal `cudaErrorIllegalInstruction` when the V1 engine attempts to capture or synchronize CUDA Graphs for batch sizes > 1. ### Environment - **Hardware:** NVIDIA DGX Spark (Blackwell `sm_121`) - **Memory:** 128GB Unified Memory - **Image:** `vllm/vllm-openai:v0.17.1-cu130` - **Model:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4` (Hybrid Mamba-2 + MoE) - **Quantization:** NVFP4 (ModelOpt) ### Steps to Reproduce 1. Start the vLLM server using the official NVIDIA-provided Docker command for DGX Spark: ``` docker run --gpus all \ --ipc=host \ --entrypoint vllm \ -v ~/models:/workspace/models \ -p 8000:8000 \ -e VLLM_NVFP4_GEMM_BACKEND=marlin \ -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ -e VLLM_FLASHINFER_ALLREDUCE_BACKEND=trtllm \ vllm/vllm-openai:v0.17.1-cu130 \ serve /workspace/models/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 \ --served-model-name nemotron-3-nano \ --host 0.0.0.0 \ --port 8000 \ --dtype auto \ --kv-cache-dtype fp8 \ --trust-remote-code \ --gpu-memory-utilization 0.80 \ --max-model-len 1048576 \ --max-...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: CUDA Illegal Instruction during CUDA Graph capture with Nemotron-3-Nano NVFP4 on sm_121 bug ### Your current environment ### 🐛 Describe the bug Running the new NVIDIA Nemotron-3-Nano (Hybrid Mamba-2 + MoE) in NVFP4 form...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: -v ~/models:/workspace/models \ -p 8000:8000 \ -e VLLM_NVFP4_GEMM_BACKEND=marlin \ -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \ -e VLLM_FLASHINFER_ALLREDUCE_BACKEND=trtllm \ vllm/vllm-openai:v0.17.1-cu130 \ serve /workspace/mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ModelOpt) ### Steps to Reproduce 1. Start the vLLM server using the official NVIDIA-provided Docker command for DGX Spark: ``` docker run --gpus all \ --ipc=host \ --entrypoint vllm \ -v ~/models:/workspace/models \ -p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA Illegal Instruction during CUDA Graph capture with Nemotron-3-Nano NVFP4 on sm_121 bug ### Your current environment ### 🐛 Describe the bug Running the new NVIDIA Nemotron-3-Nano (Hybrid Mamba-2 + MoE) in NVF...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Running the new NVIDIA Nemotron-3-Nano (Hybrid Mamba-2 + MoE) in NVFP4 format on Blackwell hardware (DGX Spark) results in a fatal `cudaErrorIllegalInstruction` when the V1 engine attempts to capture or synchronize CUDA...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
