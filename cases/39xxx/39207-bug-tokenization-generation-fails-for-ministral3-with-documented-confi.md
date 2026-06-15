# vllm-project/vllm#39207: [Bug]: Tokenization/Generation fails for Ministral3 with documented configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#39207](https://github.com/vllm-project/vllm/issues/39207) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tokenization/Generation fails for Ministral3 with documented configuration

### Issue 正文摘录

### Your current environment **vLLM version:** 0.19.0 **Environment:** - OS: openSUSE Leap 15.5 (x86_64) - Python: 3.12.9 - PyTorch: 2.10.0+cu126 - GPU: NVIDIA RTX A6000 ×6 - CUDA: 12.6 - transformers: 4.57.6 ``` [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu12==12.6.77 [pip3] nvidia-cuda-runtime-cu12==12.6.77 [pip3] nvidia-cudnn-cu12==9.10.2.21 [pip3] nvidia-cudnn-frontend==1.18.0 [pip3] nvidia-cufft-cu12==11.3.0.4 [pip3] nvidia-cufile-cu12==1.11.1.6 [pip3] nvidia-curand-cu12==10.3.7.77 [pip3] nvidia-cusolver-cu12==11.7.1.2 [pip3] nvidia-cusparse-cu12==12.5.4.2 [pip3] nvidia-cusparselt-cu12==0.7.1 [pip3] nvidia-cutlass-dsl==4.4.2 [pip3] nvidia-cutlass-dsl-libs-base==4.4.2 [pip3] nvidia-ml-py==13.595.45 [pip3] nvidia-nccl-cu12==2.27.5 [pip3] nvidia-nvjitlink-cu12==12.6.85 [pip3] nvidia-nvshmem-cu12==3.4.5 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pyzmq==27.1.0 [pip3] torch==2.10.0+cu126 [pip3] torch_c_dlpack_ext==0.1.5 [pip3] torchaudio==2.10.0+cu126 [pip3] torchvision==0.25.0+cu126 [pip3] transformers==4.57.6 [pip3] triton==3.6.0 ``` ### 🐛 Describe the bug When serving `mistr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 3 with documented configuration bug ### Your current environment **vLLM version:** 0.19.0 **Environment:** - OS: openSUSE Leap 15.5 (x86_64) - Python: 3.12.9 - PyTorch: 2.10.0+cu126 - GPU: NVIDIA RTX A6000 ×6 - CUDA: 12...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Tokenization/Generation fails for Ministral3 with documented configuration bug ### Your current environment **vLLM version:** 0.19.0 **Environment:** - OS: openSUSE Leap 15.5 (x86_64) - Python: 3.12.9 - PyTorch:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: GPU: NVIDIA RTX A6000 ×6 - CUDA: 12.6 - transformers: 4.57.6 ``` [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-nvrtc-cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eap 15.5 (x86_64) - Python: 3.12.9 - PyTorch: 2.10.0+cu126 - GPU: NVIDIA RTX A6000 ×6 - CUDA: 12.6 - transformers: 4.57.6 ``` [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ipe for Ministral-3-Instruct](https://docs.vllm.ai/projects/recipes/en/latest/Mistral/Ministral-3-Instruct.html), the model produces completely garbled and repetitive output. **Command used (from documentation):** ```ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
