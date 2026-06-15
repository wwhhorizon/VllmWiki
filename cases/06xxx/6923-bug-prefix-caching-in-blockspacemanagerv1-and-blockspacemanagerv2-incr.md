# vllm-project/vllm#6923: [Bug]: Prefix Caching in BlockSpaceManagerV1 and BlockSpaceManagerV2 Increases Time to First Token(TTFT) and Slows Down System

| 字段 | 值 |
| --- | --- |
| Issue | [#6923](https://github.com/vllm-project/vllm/issues/6923) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix Caching in BlockSpaceManagerV1 and BlockSpaceManagerV2 Increases Time to First Token(TTFT) and Slows Down System

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.114.2.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.129.03 Versions of relevant libraries: [pip3] mypy-extensions==1.0.0 [pip3] mypy-protobuf==3.6.0 [pip3] numpy==1.22.0 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] onnx==1.14.0 [pip3] pytorch-quantization==2.1.2 [pip3] torch==2.3.1 [pip3] torch-tensorrt==0.0.0 [pip3] torchdata==0.7.0a0 [pip3] torchtext==0.16.0a0 [pip3] torchvision==0.18.1 [pip3]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lows Down System bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Prefix Caching in BlockSpaceManagerV1 and BlockSpaceManagerV2 Increases Time to First Token(TTFT) and Slows Down System bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eManagerV2 Increases Time to First Token(TTFT) and Slows Down System bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
