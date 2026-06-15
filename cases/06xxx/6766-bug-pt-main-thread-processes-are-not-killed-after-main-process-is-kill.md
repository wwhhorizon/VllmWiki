# vllm-project/vllm#6766: [Bug]: `pt_main_thread` processes are not killed after main process is killed in MP distributed executor backend 

| 字段 | 值 |
| --- | --- |
| Issue | [#6766](https://github.com/vllm-project/vllm/issues/6766) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `pt_main_thread` processes are not killed after main process is killed in MP distributed executor backend 

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-78-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: LAZY GPU models: A100s Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.3.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled ``` ### 🐛 Describe the bug I am trying to understand the vllm's workflow for distributed serving via multiprocessing. The original setup is deploying a model with tensor parallel size = 2 through Triton Inference Server and `distributed_executor_backend: mp` . W...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: xecutor backend bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s are not killed after main process is killed in MP distributed executor backend bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: True CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: LAZY GPU models: A100s Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.1 [pip3] torchvision==0.18.1 [...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: led after main process is killed in MP distributed executor backend bug;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build P...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
