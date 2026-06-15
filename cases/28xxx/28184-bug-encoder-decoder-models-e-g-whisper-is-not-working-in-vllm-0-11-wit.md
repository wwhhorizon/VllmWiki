# vllm-project/vllm#28184: [Bug]: encoder_decoder models (e.g. Whisper) is not working in vLLM 0.11 with ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#28184](https://github.com/vllm-project/vllm/issues/28184) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: encoder_decoder models (e.g. Whisper) is not working in vLLM 0.11 with ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description: I downloaded the [vllm/rocm-dev](https://hub.docker.com/layers/rocm/vllm-dev/nightly_main_20251105/images/sha256-49ce35bb2c053b5ab76b955453aa7d651afe9b4fbef895183ef5299ba7935007) image version 0.11.1_20251105 with ROCm 7 to test if Whisper could perform timestamp transcription with segments in this version, since this functionality was not available in the version I was using before [(0.10.1)](https://hub.docker.com/layers/rocm/vllm/rocm6.4.1_vllm_0.10.1_20250909/images/sha256-1113268572e26d59b205792047bea0e61e018e79aeadceba118b7bf23cb3715c). ## Then, when i was running the container, this error occurred: ```text Attaching to vllm_container vllm_container | DEBUG 11-06 05:01:05 [plugins/__init__.py:32] No plugins for group vllm.platform_plugins found. vllm_container | DEBUG 11-06 05:01:05 [platforms/__init__.py:36] Checking if TPU platform is available. vllm_container | DEBUG 11-06 05:01:05 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' vllm_container | DEBUG 11-06 05:01:05 [platforms/__init__.py:61] Checking if CUDA platform is available. vllm_container | DEBUG 11-06 05...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: e the bug ## Description: I downloaded the [vllm/rocm-dev](https://hub.docker.com/layers/rocm/vllm-dev/nightly_main_20251105/images/sha256-49ce35bb2c053b5ab76b955453aa7d651afe9b4fbef895183ef5299ba7935007) image version...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: rver pid=1) INFO 11-06 05:01:17 [config/model.py:1951] Downcasting torch.float32 to torch.bfloat16. vllm_container | (APIServer pid=1) INFO 11-06 05:01:17 [config/model.py:1728] Using max model len 448 vllm_container |...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: encoder_decoder models (e.g. Whisper) is not working in vLLM 0.11 with ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug ## Description: I downloaded the [vllm/rocm-dev](https://hub.docker.com/lay...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: ly detected platform rocm. vllm_container | DEBUG 11-06 05:01:08 [utils/flashinfer.py:44] FlashInfer unavailable since package was not found vllm_container | DEBUG 11-06 05:01:10 [entrypoints/utils.py:175] Setting VLLM_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : encoder_decoder models (e.g. Whisper) is not working in vLLM 0.11 with ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug ## Description: I downloaded the [vllm/rocm-dev](https://hub.docker.com/layers/r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
