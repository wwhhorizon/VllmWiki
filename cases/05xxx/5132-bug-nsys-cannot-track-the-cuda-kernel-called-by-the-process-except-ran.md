# vllm-project/vllm#5132: [Bug]: nsys cannot track the cuda kernel called by the process except rank 0

| 字段 | 值 |
| --- | --- |
| Issue | [#5132](https://github.com/vllm-project/vllm/issues/5132) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nsys cannot track the cuda kernel called by the process except rank 0

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0 Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.35 Python version: 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-5.4.56.bsk.9-amd64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ss except rank 0 bug;stale ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: nsys cannot track the cuda kernel called by the process except rank 0 bug;stale ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: sys cannot track the cuda kernel called by the process except rank 0 bug;stale ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ==0.7.0a0 [pip3] torchtext==0.16.0a0 [pip3] torchvision==0.16.0a0 [pip3] triton==2.2.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.0.post1 vLLM Build Flags: CUDA Ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
