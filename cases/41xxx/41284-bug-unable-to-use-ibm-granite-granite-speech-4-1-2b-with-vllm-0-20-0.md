# vllm-project/vllm#41284: [Bug]: Unable to use ibm-granite/granite-speech-4.1-2b with vllm 0.20.0

| 字段 | 值 |
| --- | --- |
| Issue | [#41284](https://github.com/vllm-project/vllm/issues/41284) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to use ibm-granite/granite-speech-4.1-2b with vllm 0.20.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # vLLM 0.20.0 Regression: granite-speech-4.1-2b Audio Processing Broken ## Summary `ibm-granite/granite-speech-4.1-2b` audio input is silently ignored in vLLM 0.20.0. The same model, quantization, and request format works correctly with vLLM 0.17.x. All audio API paths are affected, including the dedicated `/v1/audio/transcriptions` endpoint. I had built a version of vllm 0.17.0 using these instructions and installed it in my conda environment by copying the miniforge3/envs/vllm/bin/vllm into miniforge3/envs/msp/bin/.: [BUILD_VLLM.md](https://github.com/user-attachments/files/27216626/BUILD_VLLM.md) ## Environment - **vLLM version**: 0.20.0 (regression — works on 0.17.x) - **Model**: `ibm-granite/granite-speech-4.1-2b` - **Platform**: NVIDIA DGX Spark, ARM64 (aarch64), Linux 6.17.0 - **GPU**: NVIDIA GB10 (120 GB) - **Quantization**: `--quantization fp8` - **Launch command**: ```bash vllm serve ibm-granite/granite-speech-4.1-2b \ --api-key vllm_token_here \ --quantization fp8 \ --max-model-len 2048 \ --port 8083 \ --gpu-memory-utilization 0.25 ``` ## Reproduction ### 1. Chat completions with `input_audio` — audio silently ignored...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: luding the dedicated `/v1/audio/transcriptions` endpoint. I had built a version of vllm 0.17.0 using these instructions and installed it in my conda environment by copying the miniforge3/envs/vllm/bin/vllm into miniforg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: granite/granite-speech-4.1-2b` - **Platform**: NVIDIA DGX Spark, ARM64 (aarch64), Linux 6.17.0 - **GPU**: NVIDIA GB10 (120 GB) - **Quantization**: `--quantization fp8` - **Launch command**: ```bash vllm serve ibm-granit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: -speech-4.1-2b` audio input is silently ignored in vLLM 0.20.0. The same model, quantization, and request format works correctly with vLLM 0.17.x. All audio API paths are affected, including the dedicated `/v1/audio/tra...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -4.1-2b` audio input is silently ignored in vLLM 0.20.0. The same model, quantization, and request format works correctly with vLLM 0.17.x. All audio API paths are affected, including the dedicated `/v1/audio/transcript...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.2.0 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
