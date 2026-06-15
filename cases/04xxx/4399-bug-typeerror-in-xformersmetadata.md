# vllm-project/vllm#4399: [Bug]: TypeError in XFormersMetadata 

| 字段 | 值 |
| --- | --- |
| Issue | [#4399](https://github.com/vllm-project/vllm/issues/4399) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError in XFormersMetadata 

### Issue 正文摘录

### Your current environment ```text python collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Fedora release 36 (Thirty Six) (x86_64) GCC version: (GCC) 12.2.1 20221121 (Red Hat 12.2.1-4) Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.7 (main, Sep 7 2022, 00:00:00) [GCC 12.2.1 20220819 (Red Hat 12.2.1-1)] (64-bit runtime) Python platform: Linux-6.2.15-100.fc36.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Quadro T1000 Nvidia driver version: 530.41.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 12 On-line CPU(s) list: 0-11 Vendor ID: GenuineIntel Model name: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz CPU family: 6 Model: 158 Thread(s) per core: 2 Core(s) per socket: 6 Socket(s): 1 S...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: text python collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Fedora release 36 (Thirty Six) (x8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: rent environment ```text python collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Fedora release...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: TypeError in XFormersMetadata bug;stale ### Your current environment ```text python collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: TypeError in XFormersMetadata bug;stale ### Your current environment ```text python collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: TypeError in XFormersMetadata bug;stale ### Your current environment ```text python collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
