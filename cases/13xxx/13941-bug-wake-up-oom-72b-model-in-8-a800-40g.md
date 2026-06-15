# vllm-project/vllm#13941: [Bug]: wake up OOM (72B model in 8*A800(40G))

| 字段 | 值 |
| --- | --- |
| Issue | [#13941](https://github.com/vllm-project/vllm/issues/13941) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: wake up OOM (72B model in 8*A800(40G))

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.120.bsk.2-amd64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.20 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-40GB GPU 1: NVIDIA A800-SXM4-40GB GPU 2: NVIDIA A800-SXM4-40GB GPU 3: NVIDIA A800-SXM4-40GB GPU 4: NVIDIA A800-SXM4-40GB GPU 5: NVIDIA A800-SXM4-40GB GPU 6: NVIDIA A800-SXM4-40GB GPU 7: NVIDIA A800-SXM4-40GB Nvidia driver version: 535.161.08 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.3.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.3.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.3.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.3.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.3.0 /usr/lib/x86_64-linux-gnu/libcu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: model in 8*A800(40G)) bug;unstale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: wake up OOM (72B model in 8*A800(40G)) bug;unstale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: wake up OOM (72B model in 8*A800(40G)) bug;unstale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -pyindex==1.0.9 [pip3] onnx==1.16.0 [pip3] optree==0.12.1 [pip3] pytorch-triton==3.0.0+dedb7bdf3 [pip3] pyzmq==26.1.0 [pip3] torch==2.5.1 [pip3] torch_tensorrt==2.5.0a0 [pip3] torchaudio==2.5.1 [pip3] torchvision==0.20....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
