# vllm-project/vllm#16489: [Usage]: Empty "content" when running Gemma3-27B across multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#16489](https://github.com/vllm-project/vllm/issues/16489) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Empty "content" when running Gemma3-27B across multiple GPUs

### Issue 正文摘录

### Your current environment - Hardware: [Nvidia DGX-2](https://www.nvidia.com/en-in/data-center/dgx-2/) - 16x32GB V100 GPUs - Ubuntu 20.04.6 - Docker version 24.0.7 - Docker Image: vllm/vllm-openai:v0.8.2 - Cuda information: - `nvidia-smi`: "CUDA Version: 12.2 - `nvcc --version`: Cuda compilation tools, release 12.8 ### How would you like to use vllm Hello and thank you for this awesome tool! ## Background: - My goal is to get Gemma3-27B running on a completely offline Nvidia DGX-2 GPU cluster (16x32GB V100 GPUs = 512GB VRAM) using vLLM's v0.8.2 Docker Image. - The smaller Gemma3-1B on just one of the GPUs runs perfectly with no problems 👍 ``` sh docker run -d --name vLLM-Gemma3-1B --runtime nvidia \ --gpus='"device=10"' \ -v /raid/models/google/:/root/.cache/huggingface \ -p 8001:8000 \ --ipc=host \ --restart=unless-stopped \ offline-image-repo:8180/vllm-openai:v0.8.2 \ --model /root/.cache/huggingface/gemma-3-1b-it \ --dtype float16 \ --served-model-name google/gemma-3-1b-it ``` ## The Problem - I can get the Gemma3-27B container start and run with no errors reported in the `docker logs`, everything seems good.. ``` sh docker run -d --name vLLM-Gemma3-27B --runtime nvidia \ --g...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: dia.com/en-in/data-center/dgx-2/) - 16x32GB V100 GPUs - Ubuntu 20.04.6 - Docker version 24.0.7 - Docker Image: vllm/vllm-openai:v0.8.2 - Cuda information: - `nvidia-smi`: "CUDA Version: 12.2 - `nvcc --version`: Cuda com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 0.04.6 - Docker version 24.0.7 - Docker Image: vllm/vllm-openai:v0.8.2 - Cuda information: - `nvidia-smi`: "CUDA Version: 12.2 - `nvcc --version`: Cuda compilation tools, release 12.8 ### How would you like to use vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Empty "content" when running Gemma3-27B across multiple GPUs usage ### Your current environment - Hardware: [Nvidia DGX-2](https://www.nvidia.com/en-in/data-center/dgx-2/) - 16x32GB V100 GPUs - Ubuntu 20.04.6 -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 8.2 \ --model /root/.cache/huggingface/gemma-3-1b-it \ --dtype float16 \ --served-model-name google/gemma-3-1b-it ``` ## The Problem - I can get the Gemma3-27B container start and run with no errors reported in the `doc...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: Empty "content" when running Gemma3-27B across multiple GPUs usage ### Your current environment - Hardware: [Nvidia DGX-2](https://www.nvidia.com/en-in/data-center/dgx-2/) - 16x32GB V100 GPUs - Ubuntu 20.04.6 -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
