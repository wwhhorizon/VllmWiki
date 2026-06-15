# vllm-project/vllm#7368: [Installation]: git clone cutlass fails

| 字段 | 值 |
| --- | --- |
| Issue | [#7368](https://github.com/vllm-project/vllm/issues/7368) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: git clone cutlass fails

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.10 (Ootpa) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-22) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.28 Python version: 3.11.9 (main, Jun 19 2024, 10:02:06) [GCC 8.5.0 20210514 (Red Hat 8.5.0-22)] (64-bit runtime) Python platform: Linux-4.18.0-553.8.1.el8_10.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40S-48C GPU 1: NVIDIA L40S-48C GPU 2: NVIDIA L40S-48C Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.9.3.0 /usr/lib64/libcudnn_adv.so.9.3.0 /usr/lib64/libcudnn_cnn.so.9.3.0 /usr/lib64/libcudnn_engines_precompiled.so.9.3.0 /usr/lib64/libcudnn_engines_runtime_compiled.so.9.3.0 /usr/lib64/libcudnn_graph.so.9.3.0 /usr/lib64/libcudnn_heuristic.so.9.3.0 /usr/lib64/libcudnn_ops.so.9.3.0 HIP runtime version: N/A MIOpen runtime version:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: git clone cutlass fails installation ### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM use
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.10 (Ootpa) (x86_64) GCC version: (GCC) 8.5...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tallation ### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.10 (Ootpa) (x86_64) GCC version: (GCC)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Installation]: git clone cutlass fails installation ### Your current environment ```text Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
