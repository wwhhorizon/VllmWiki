# vllm-project/vllm#12950: [Usage]: How to do offline inference on multi-node with tensor-parallel and pipeline-parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#12950](https://github.com/vllm-project/vllm/issues/12950) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to do offline inference on multi-node with tensor-parallel and pipeline-parallel

### Issue 正文摘录

### Your current environment ```text 15:44:15.931 Collecting environment information... 15:44:15.931 PyTorch version: 2.5.1+cu121 15:44:15.931 Is debug build: False 15:44:15.931 CUDA used to build PyTorch: 12.1 15:44:15.931 ROCM used to build PyTorch: N/A 15:44:15.931 15:44:15.932 OS: CentOS Linux 7 (Core) (x86_64) 15:44:15.932 GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2) 15:44:15.932 Clang version: Could not collect 15:44:15.932 CMake version: version 3.31.2 15:44:15.932 Libc version: glibc-2.17 15:44:15.932 15:44:15.932 Python version: 3.9.18 (main, Sep 11 2023, 13:41:44) [GCC 11.2.0] (64-bit runtime) 15:44:15.932 Python platform: Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.17 15:44:15.932 Is CUDA available: True 15:44:15.932 CUDA runtime version: 12.2.140 15:44:15.933 CUDA_MODULE_LOADING set to: LAZY 15:44:15.933 GPU models and configuration: 15:44:15.933 GPU 0: NVIDIA A100-SXM4-80GB 15:44:15.933 GPU 1: NVIDIA A100-SXM4-80GB 15:44:15.933 15:44:15.933 Nvidia driver version: 470.103.01 15:44:15.933 cuDNN version: Probably one of the following: 15:44:15.933 /usr/lib64/libcudnn.so.8.9.4 15:44:15.933 /usr/lib64/libcudnn_adv_infer.so.8.9.4 15:44:15.933 /usr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: 15:44:15.931 Collecting environment information... 15:44:15.931 PyTorch version: 2.5.1+cu121 15:44:15.931 Is debug build: False 15:44:15.931 CUDA used to build PyTorch: 12.1 15:44:15.931 ROCM used to build PyTorch: N/A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: rch version: 2.5.1+cu121 15:44:15.931 Is debug build: False 15:44:15.931 CUDA used to build PyTorch: 12.1 15:44:15.931 ROCM used to build PyTorch: N/A 15:44:15.931 15:44:15.932 OS: CentOS Linux 7 (Core) (x86_64) 15:44:1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Your current environment ```text 15:44:15.931 Collecting environment information... 15:44:15.931 PyTorch version: 2.5.1+cu121 15:44:15.931 Is debug build: False 15:44:15.931 CUDA used to build PyTorch: 12.1 15:44:15.931...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: inference on multi-node with tensor-parallel and pipeline-parallel usage;stale ### Your current environment ```text 15:44:15.931 Collecting environment information... 15:44:15.931 PyTorch version: 2.5.1+cu121 15:44:15.9...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: :44:15.938 [pip3] nvidia-nvtx-cu12==12.1.105 15:44:15.938 [pip3] pytorch-triton==2.1.0+e6216047b8 15:44:15.938 [pip3] pyzmq==26.2.1 15:44:15.938 [pip3] torch==2.5.1+cu121 15:44:15.939 [pip3] torchaudio==2.5.1 15:44:15.9...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
