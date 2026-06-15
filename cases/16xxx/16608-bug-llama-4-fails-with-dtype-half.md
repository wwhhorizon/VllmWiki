# vllm-project/vllm#16608: [Bug]: Llama-4 fails with dtype=half

| 字段 | 值 |
| --- | --- |
| Issue | [#16608](https://github.com/vllm-project/vllm/issues/16608) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-4 fails with dtype=half

### Issue 正文摘录

### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.35 Versions of relevant libraries: [pip3] numpy==2.1.3 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cuda-nvrtc-cu12==12.4.127 [pip3] nvidia-cuda-runtime-cu12==12.4.127 [pip3] nvidia-cudnn-cu12==9.1.0.70 [pip3] nvidia-cufft-cu12==11.2.1.3 [pip3] nvidia-curand-cu12==10.3.5.147 [pip3] nvidia-cusolver-cu12==11.6.1.9 [pip3] nvidia-cusparse-cu12==12.3.1.170 [pip3] nvidia-cusparselt-cu12==0.6.2 [pip3] nvidia-nccl-cu12==2.21.5 [pip3] nvidia-nvjitlink-cu12==12.4.127 [pip3] nvidia-nvtx-cu12==12.4.127 [pip3] pyzmq==26.4.0 [pip3] torch==2.6.0 [pip3] torchaudio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.51.2 [pip3] triton==3.2.0 [conda] numpy 2.1.3 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cuda-nvrtc-cu12 12.4.127 pypi_0 pypi [conda] nvidia-cuda...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Llama-4 fails with dtype=half bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Llama-4 fails with dtype=half bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama-4 fails with dtype=half bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug bu
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] triton==3.2.0 [conda] numpy 2.1.3 pypi_0 pypi

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
