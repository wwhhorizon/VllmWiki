# vllm-project/vllm#20621: [Bug]: AttributeError: Linear has no attribute `mask`

| 字段 | 值 |
| --- | --- |
| Issue | [#20621](https://github.com/vllm-project/vllm/issues/20621) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: Linear has no attribute `mask`

### Issue 正文摘录

============================== Versions of relevant libraries ============================== [pip3] flake8==7.1.1 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu12==12.6.77 [pip3] nvidia-cuda-runtime-cu12==12.6.77 [pip3] nvidia-cudnn-cu12==9.5.1.17 [pip3] nvidia-cufft-cu12==11.3.0.4 [pip3] nvidia-cufile-cu12==1.11.1.6 [pip3] nvidia-curand-cu12==10.3.7.77 [pip3] nvidia-cusolver-cu12==11.7.1.2 [pip3] nvidia-cusparse-cu12==12.5.4.2 [pip3] nvidia-cusparselt-cu12==0.6.3 [pip3] nvidia-ml-py==12.570.86 [pip3] nvidia-nccl-cu12==2.26.2 [pip3] nvidia-nvjitlink-cu12==12.6.85 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pynvml==12.0.0 [pip3] pyzmq==26.2.0 [pip3] torch==2.7.0 [pip3] torchaudio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.53.0 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80 pypi_0 pypi [conda] nvidia-cuda-nvrtc-cu12 12.6.77 pypi_0 pypi [conda] nvidia-cuda-runtime-cu12 12.6.77 pypi_0 pypi [conda] nvidia-cudnn-cu12 9.5.1.17 pypi_0 pypi [conda] nvidia-cufft-cu12 11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Linear has no attribute `mask` bug;stale ============================== Versions of relevant libraries ============================== [pip3] flake8==7.1.1 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu12==12.6.77 [pip3] nvidia-cuda-runtime-cu12==12.6.77 [pip3] nvidia-cudnn-cu12==9.5.1.17 [pip3]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 3.3.0 pypi_0 pypi ### 🐛 Describe the bug The model underwent structural sparsity optimization (2:4) and is now being fine-tuned. When running the fine-tuning using torchrun in parallel mode with the command: torchrun --...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.53.0 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;model_support cuda;triton crash env_dependency ==============================

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
