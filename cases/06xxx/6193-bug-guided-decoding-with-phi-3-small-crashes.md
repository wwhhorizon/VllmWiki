# vllm-project/vllm#6193: [Bug]: Guided decoding with Phi-3-small crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#6193](https://github.com/vllm-project/vllm/issues/6193) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Guided decoding with Phi-3-small crashes

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.0-30-cloud-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.128 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 4 On-line CPU(s) list: 0-3 Thread(s) per core: 2 Core(s) per socket: 2 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) CPU @ 2.20GHz Stepping: 7 CPU MHz: 2200.196 BogoMIPS: 4400.39 Hypervisor vendor: KVM Virtu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: -3-small crashes bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug buil
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Guided decoding with Phi-3-small crashes bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.2.128 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: _vnni md_clear arch_capabilities Versions of relevant libraries: [pip3] flashinfer==0.0.8+cu121torch2.3 [pip3] numpy==1.25.2 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] torchvision==0.18.0 [pip3] transfor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Guided decoding with Phi-3-small crashes bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
