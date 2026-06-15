# vllm-project/vllm#19176: [Usage]: how to place a vllm model initialized inside the python code on a specific gpu?

| 字段 | 值 |
| --- | --- |
| Issue | [#19176](https://github.com/vllm-project/vllm/issues/19176) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to place a vllm model initialized inside the python code on a specific gpu?

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.1 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.0-72-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.5.82 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version : 550.144.03 cuDNN version : Probably one o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: e]: how to place a vllm model initialized inside the python code on a specific gpu? usage;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: how to place a vllm model initialized inside the python code on a specific gpu? usage;stale ### Your current environment ============================== System Info ============================== OS : Ubunt
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: quested device {vllm_device} is also being used for training. For higher throughput " "and to avoid out-of-memory errors, it is recommended to use a dedicated device for vLLM. " "If this is intentional, you may ignore t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: a vllm model initialized inside the python code on a specific gpu? usage;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.1 LTS (x86_64) GCC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
