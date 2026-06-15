# vllm-project/vllm#10652: [Bug]: Inference is exceptionally slow on the L20 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#10652](https://github.com/vllm-project/vllm/issues/10652) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference is exceptionally slow on the L20 GPU

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC) 9.2.1 20200522 (Alibaba 9.2.1-3 2.17) Clang version: Could not collect CMake version: version 3.20.1 Libc version: glibc-2.30 Python version: 3.9.19 (main, Mar 21 2024, 17:11:28) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.9.151-015.ali3000.alios7.x86_64-x86_64-with-glibc2.30 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: L20-2-PCIE-48GB-48GB-L-H-V Nvidia driver version: 535.161.08 cuDNN version: Probably one of the following: /usr/local/cuda/targets/x86_64-linux/lib/libcudnn.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.3 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.9.3 /...es (without traversing the PCIe Host Bridge) PIX = Connection traversing at most a single PCIe bridge NV# = Connection traversing a bonded set of # NVLinks LD_LIBRARY_PATH...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ally slow on the L20 GPU bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Serv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version: (GCC)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: L20-2-PCIE-48GB-48GB-L-H-V Nvidia driver version: 535.161.08 cuDNN version: Probably one of the following: /usr/lo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64) GCC version:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Inference is exceptionally slow on the L20 GPU bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibab...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
