# vllm-project/vllm#18585: [Bug]:openai接口tools使用enum多标签问题

| 字段 | 值 |
| --- | --- |
| Issue | [#18585](https://github.com/vllm-project/vllm/issues/18585) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]:openai接口tools使用enum多标签问题

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.35 Python version: 3.12.10 (main, Apr 9 2025, 08:55:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4060 Laptop GPU Nvidia driver version: 560.94 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: GenuineIntel Model name: 13th Gen Intel(R) Core(TM) i9-13900HX CPU family: 6 Model: 183 Thread(s) per core: 2 Core(s) per socket: 16 Socket(s): 1 Stepping: 1 BogoMIPS: 4838.39 Flags: fpu vme de pse ts...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: PyTorch version: 2.6.0+cu124 Is debug build: False CUDA use
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ls使用enum多标签问题 bug ### Your current environment Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Vulnerable: No microcode Vulnerability Retbl
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [pip3] flashinfer-python==0.2.1.post2+cu124torch2.6 [pip3] numpy==2.2.5 [pip3]

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
