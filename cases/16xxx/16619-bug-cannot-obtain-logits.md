# vllm-project/vllm#16619: [Bug]: Cannot obtain logits

| 字段 | 值 |
| --- | --- |
| Issue | [#16619](https://github.com/vllm-project/vllm/issues/16619) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot obtain logits

### Issue 正文摘录

### Your current environment I do not want logprobs but want the logits of shape Batch Size,Tokens,Dictionary similar to model.generate(return_logits=True) in huggingface. Is this possible? The output of `python collect_env.py` ```text PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.24.2 Libc version: glibc-2.35 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.15.0-112-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.5.119 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe GPU 4: NVIDIA A100 80GB PCIe GPU 5: NVIDIA A100 80GB PCIe GPU 6: NVIDIA A100 80GB PCIe GPU 7: NVIDIA A100 80GB PCIe Nvidia driver version: 570.86.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: this possible? The output of `python collect_env.py` ```text PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ect_env.py` ```text PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: obs but want the logits of shape Batch Size,Tokens,Dictionary similar to model.generate(return_logits=True) in huggingface. Is this possible? The output of `python collect_env.py` ```text PyTorch version: 2.6.0+cu124 Is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Cannot obtain logits bug;stale ### Your current environment I do not want logprobs but want the logits of shape Batch Size,Tokens,Dictionary similar to model.generate(return_logits=True) in huggingface. Is this p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.51.3 [pip3] triton==3.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
