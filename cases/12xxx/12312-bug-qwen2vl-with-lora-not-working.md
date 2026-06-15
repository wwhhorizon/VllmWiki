# vllm-project/vllm#12312: [Bug]: Qwen2VL with lora not working.

| 字段 | 值 |
| --- | --- |
| Issue | [#12312](https://github.com/vllm-project/vllm/issues/12312) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2VL with lora not working.

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.12.8 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 16:31:09) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-49-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX 6000 Ada Generation GPU 1: NVIDIA RTX 6000 Ada Generation GPU 2: NVIDIA RTX 6000 Ada Generation GPU 3: NVIDIA RTX 6000 Ada Generation GPU 4: NVIDIA RTX 6000 Ada Generation GPU 5: NVIDIA RTX 6000 Ada Generation GPU 6: NVIDIA RTX 6000 Ada Generation GPU 7: NVIDIA RTX 6000 Ada Generation Nvidia driver version: 550.120 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.5.0 /usr/lib/x86_64-linux-gnu/li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen2VL with lora not working. bug ### Your current environment Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: n cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqd...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.48.0 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
