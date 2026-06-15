# vllm-project/vllm#4934: [Bug]: speculative decoding got `shape mismatch` error with n>1 and random sample

| 字段 | 值 |
| --- | --- |
| Issue | [#4934](https://github.com/vllm-project/vllm/issues/4934) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: speculative decoding got `shape mismatch` error with n>1 and random sample

### Issue 正文摘录

### Your current environment The vllm is installed from source code of recent commit 26148120b3c0570440. ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.1 Libc version: glibc-2.35 Python version: 3.11.0rc1 (main, Aug 12 2022, 10:02:14) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.42.2.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version: 470.57.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 112 On-line CPU(s) list: 0-111 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8350C CPU @ 2.60GHz CPU family: 6 Mode...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: >1 and random sample bug;stale ### Your current environment The vllm is installed from source code of recent commit 26148120b3c0570440. ```text The output of `python collect_env.py` Collecting environment information......
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: speculative decoding got `shape mismatch` error with n>1 and random sample bug;stale ### Your current environment The vllm is installed from source code of recent commit 26148120b3c0570440. ```text The output of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: speculative decoding got `shape mismatch` error with n>1 and random sample bug;stale ### Your current environment The vllm is installed from source code of recent commit 26148120b3c0570440. ```text The output of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
