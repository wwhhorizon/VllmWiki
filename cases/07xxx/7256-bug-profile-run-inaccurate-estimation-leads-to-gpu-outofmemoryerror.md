# vllm-project/vllm#7256: [Bug]: profile_run Inaccurate estimation leads to gpu OutOfMemoryError

| 字段 | 值 |
| --- | --- |
| Issue | [#7256](https://github.com/vllm-project/vllm/issues/7256) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: profile_run Inaccurate estimation leads to gpu OutOfMemoryError

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.19.91-014-kangaroo.2.10.13.5c249cdaf.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.0.0 /usr/l...

## 现有链接修复摘要

#9352 [Bugfix][Core] Use torch.cuda.memory_stats() to profile peak memory usage

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: o gpu OutOfMemoryError bug ### Your current environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ironment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvid...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: umpy==1.24.4 [pip3] onnx==1.15.0rc2 [pip3] optree==0.10.0 [pip3] pytorch-quantization==2.1.2 [pip3] torch==2.3.0a0+ebedce2 [pip3] torch-tensorrt==2.3.0a0 [pip3] torchdata==0.7.1a0 [pip3] torchtext==0.17.0a0 [pip3] torch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9352](https://github.com/vllm-project/vllm/pull/9352) | closes_keyword | 0.95 | [Bugfix][Core] Use torch.cuda.memory_stats() to profile peak memory usage | FIX #7256 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
