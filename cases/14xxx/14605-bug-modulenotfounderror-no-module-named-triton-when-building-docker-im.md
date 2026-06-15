# vllm-project/vllm#14605: [Bug]: ModuleNotFoundError: No module named 'triton' when building docker image for Arm64

| 字段 | 值 |
| --- | --- |
| Issue | [#14605](https://github.com/vllm-project/vllm/issues/14605) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash;import_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModuleNotFoundError: No module named 'triton' when building docker image for Arm64

### Issue 正文摘录

### Your current environment NVIDIA GH200 ### 🐛 Describe the bug While building the vLLM Docker image for ARM64 (Nvidia GH200 instance) as per the official [documentation](https://docs.vllm.ai/en/stable/deployment/docker.html#building-for-arm64-aarch64), I encountered the following issues: 1. PyTorch CUDA Version Mismatch The [Dockerfile](https://github.com/vllm-project/vllm/blob/main/Dockerfile) installs different PyTorch nightly versions with inconsistent CUDA versions in different stages: - **Base Image Installation**: Installs PyTorch nightly with CUDA 12.6 ``` uv pip install --index-url https://download.pytorch.org/whl/nightly/cu126 "torch==2.7.0.dev20250121+cu126" "torchvision==0.22.0.dev20250121"; ``` - **vLLM Installation Image**: Installs PyTorch nightly with CUDA 12.4 ``` uv pip install --index-url https://download.pytorch.org/whl/nightly/cu124 "torch==2.6.0.dev20241210+cu124" "torchvision==0.22.0.dev20241215"; ``` This mismatch caused build failures. Updating both installations to use CUDA 12.6 resolved the issue. 2. Missing **triton** Module During Container Execution After successfully building the image and running the container with the model **DeepSeek-R1-Distill-L...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: ModuleNotFoundError: No module named 'triton' when building docker image for Arm64 bug;stale ### Your current environment NVIDIA GH200 ### 🐛 Describe the bug While building the vLLM Docker image for ARM64 (Nvidia...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Error: No module named 'triton' when building docker image for Arm64 bug;stale ### Your current environment NVIDIA GH200 ### 🐛 Describe the bug While building the vLLM Docker image for ARM64 (Nvidia GH200 instance) as p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: After successfully building the image and running the container with the model **DeepSeek-R1-Distill-Llama-70B-bnb-4bit**, the following error occurred: ``` ModuleNotFoundError: No module named 'triton' ``` Complete log...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=8192, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ttps://docs.vllm.ai/en/stable/deployment/docker.html#building-for-arm64-aarch64), I encountered the following issues: 1. PyTorch CUDA Version Mismatch The [Dockerfile](https://github.com/vllm-project/vllm/blob/main/Dock...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
