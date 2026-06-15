# vllm-project/vllm#3526: [Bug]: when intalling vllm by pip, some errors happend.

| 字段 | 值 |
| --- | --- |
| Issue | [#3526](https://github.com/vllm-project/vllm/issues/3526) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when intalling vllm by pip, some errors happend.

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.1.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Kylin Linux Advanced Server V10 (Sword) (aarch64) GCC version: (GCC) 7.3.0 Clang version: Could not collect CMake version: version 3.27.9 Libc version: glibc-2.28 Python version: 3.8.18 (default, Sep 11 2023, 13:19:25) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.19.90-24.4.v2101.ky10.aarch64-aarch64-with-glibc2.26 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： aarch64 CPU 运行模式： 64-bit 字节序： Little Endian CPU: 256 在线 CPU 列表： 0-255 每个核的线程数： 1 每个座的核数： 64 座： 4 NUMA 节点： 8 厂商 ID： HiSilicon 型号： 0 型号名称： Kunpeng-920 步进： 0x1 CPU 最大 MHz： 3000.0000 CPU 最小 MHz： 200.0000 BogoMIPS： 200.00 L1d 缓存： 16 MiB L1i 缓存： 16 MiB L2 缓存： 128 MiB L3 缓存： 256 MiB NUMA 节点0 CPU： 0-31 NUMA 节点1 CPU： 32-63 NUMA 节点2 CPU： 64-95 NUMA 节点3 CPU： 96-127 NUMA 节点4 CPU： 128-159 NUMA 节点5 CPU： 160-191 NUMA 节点6 CPU： 192-223 NUMA 节点7 CPU： 224-255 Vulnerab...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: , some errors happend. bug ### Your current environment ```text PyTorch version: 2.1.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Kylin Linux Advanced Server V10 (Sword) (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: urrent environment ```text PyTorch version: 2.1.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Kylin Linux Advanced Server V10 (Sword) (aarch64) GCC version: (GCC) 7.3.0 Cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNN...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ur current environment ```text PyTorch version: 2.1.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Kylin Linux Advanced Server V10 (Sword) (aarch64) GCC version: (GCC) 7.3.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: down: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl Vulnerability Spectre v1: Mitigation; __user pointer sanitization Vulnerability Spectre v2: Not affected Vulner...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
