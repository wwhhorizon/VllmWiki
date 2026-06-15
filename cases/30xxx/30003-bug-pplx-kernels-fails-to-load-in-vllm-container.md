# vllm-project/vllm#30003: [Bug]: `pplx-kernels` fails to load in vLLM container

| 字段 | 值 |
| --- | --- |
| Issue | [#30003](https://github.com/vllm-project/vllm/issues/30003) |
| 状态 | open |
| 标签 | bug;stale;nvidia |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `pplx-kernels` fails to load in vLLM container

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using the vLLM container on CUDA 13.0, built with: ``` DOCKER_BUILDKIT=1 docker build \ --build-arg max_jobs=24 \ --build-arg nvcc_threads=2 \ --build-arg RUN_WHEEL_CHECK=false \ --build-arg CUDA_VERSION=13.0.1 \ --build-arg BUILD_BASE_IMAGE=nvidia/cuda:13.0.1-devel-ubuntu22.04 \ --build-arg FLASHINFER_AOT_COMPILE=true \ --build-arg torch_cuda_arch_list='9.0 10.0+PTX' \ --build-arg INSTALL_KV_CONNECTORS=true \ --platform "linux/arm64" \ --target vllm-openai \ --progress plain \ -f docker/Dockerfile \ . ``` `pplx-kernels` fails to load when serving `RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4`: ``` vllm serve RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4 -dp 2 --mm-encoder-tp-mode data --async-scheduling --max-model-len 32768 ``` The following error is thrown (after which the checkpoint continues to load): ``` (EngineCore_DP0 pid=3040376) [2025-12-03 14:55:53] ERROR ops.py:16: Error loading pplx-kernels (EngineCore_DP0 pid=3040376) Traceback (most recent call last): (EngineCore_DP0 pid=3040376) File "/usr/local/lib/python3.12/dist-packages/torch/_ops.py", line 1488, in load_library (EngineCore_DP0 pid=3040376) ctypes.CDLL(path) (Engin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: Describe the bug Using the vLLM container on CUDA 13.0, built with: ``` DOCKER_BUILDKIT=1 docker build \ --build-arg max_jobs=24 \ --build-arg nvcc_threads=2 \ --build-arg RUN_WHEEL_CHECK=false \ --build-arg CUDA_VERSIO...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ernels` fails to load when serving `RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4`: ``` vllm serve RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4 -dp 2 --mm-encoder-tp-mode data --async-scheduling --max-model-len 32768 ``` The...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: `pplx-kernels` fails to load in vLLM container bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Using the vLLM container on CUDA 13.0, built with: ``` DOCKER_BUILDKIT=1 docker build \ --build-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: BUILD_BASE_IMAGE=nvidia/cuda:13.0.1-devel-ubuntu22.04 \ --build-arg FLASHINFER_AOT_COMPILE=true \ --build-arg torch_cuda_arch_list='9.0 10.0+PTX' \ --build-arg INSTALL_KV_CONNECTORS=true \ --platform "linux/arm64" \ --t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rent environment ### 🐛 Describe the bug Using the vLLM container on CUDA 13.0, built with: ``` DOCKER_BUILDKIT=1 docker build \ --build-arg max_jobs=24 \ --build-arg nvcc_threads=2 \ --build-arg RUN_WHEEL_CHECK=false \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
