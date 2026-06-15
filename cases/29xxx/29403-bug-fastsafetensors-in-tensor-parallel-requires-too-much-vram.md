# vllm-project/vllm#29403: [Bug]: fastsafetensors in tensor parallel requires too much VRAM

| 字段 | 值 |
| --- | --- |
| Issue | [#29403](https://github.com/vllm-project/vllm/issues/29403) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;gemm;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fastsafetensors in tensor parallel requires too much VRAM

### Issue 正文摘录

### Your current environment ``` ============================== Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] mypy==1.18.2 [pip3] mypy-extensions==1.1.0 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-cu12==12.8.93 [pip3] nvidia-cuda-runtime-cu12==12.8.90 [pip3] nvidia-cudnn-cu12==9.10.2.21 [pip3] nvidia-cudnn-frontend==1.16.0 [pip3] nvidia-cufft-cu12==11.3.3.83 [pip3] nvidia-cufile-cu12==1.13.1.3 [pip3] nvidia-curand-cu12==10.3.9.90 [pip3] nvidia-cusolver-cu12==11.7.3.90 [pip3] nvidia-cusparse-cu12==12.5.8.93 [pip3] nvidia-cusparselt-cu12==0.7.1 [pip3] nvidia-cutlass-dsl==4.3.0 [pip3] nvidia-ml-py==13.580.82 [pip3] nvidia-nccl-cu12==2.27.5 [pip3] nvidia-nvjitlink-cu12==12.8.93 [pip3] nvidia-nvshmem-cu12==3.3.20 [pip3] nvidia-nvtx-cu12==12.8.90 [pip3] pyzmq==27.1.0 [pip3] torch==2.9.0 [pip3] torch-c-dlpack-ext==0.1.3 [pip3] torchaudio==2.9.0 [pip3] torchvision==0.24.0 [pip3] transformers==4.57.2 [pip3] triton==3.5.0 [conda] Could not collect ``` ### 🐛 Describe the bug When using the fastsafetensors plugin, it seems that VRAM usage is significantly increase...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: RAM bug ### Your current environment ``` ============================== Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] mypy==1.18.2 [pip3] mypy-extensions==1.1.0 [pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] mypy==1.18.2 [pip3] mypy-extensions==1.1.0 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n tensor parallel mode. I am unable to load Qwen3-VL-235B-A22B-Instruct-FP8 with the parameters from https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html ``` vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct-FP8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .0 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-cu12==12.8.93 [pip3] nvidia-cuda-runtime-cu12==12.8.90 [pip3] nvidia-cudnn-cu12==9.10.2.21 [pip3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: is significantly increased in tensor parallel mode. I am unable to load Qwen3-VL-235B-A22B-Instruct-FP8 with the parameters from https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-VL.html ``` vllm serve Qwen/Qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
