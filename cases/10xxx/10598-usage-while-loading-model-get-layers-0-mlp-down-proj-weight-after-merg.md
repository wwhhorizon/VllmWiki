# vllm-project/vllm#10598: [Usage]: While loading model get 'layers.0.mlp.down_proj.weight' after merge_and_unload()

| 字段 | 值 |
| --- | --- |
| Issue | [#10598](https://github.com/vllm-project/vllm/issues/10598) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: While loading model get 'layers.0.mlp.down_proj.weight' after merge_and_unload()

### Issue 正文摘录

### Your current environment ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.9.7 (default, Sep 16 2021, 13:09:58) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.4.0-200-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 10.1.243 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 40 bits physical, 48 bits virtual CPU(s): 8 On-line CPU(s) list: 0-7 Thread(s) per core: 1 Core(s) per socket: 4 Socket(s): 2 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel Xeon Processor (Cascadelake) Stepping: 6 CPU MHz: 2600.111 BogoMIPS: 5200.22 Virtualization: VT-x L1d cache: 256 Ki...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: tale ### Your current environment ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: While loading model get 'layers.0.mlp.down_proj.weight' after merge_and_unload() usage;stale ### Your current environment ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA use...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: model get 'layers.0.mlp.down_proj.weight' after merge_and_unload() usage;stale ### Your current environment ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
