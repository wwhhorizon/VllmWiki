# vllm-project/vllm#4198: [Bug]: KeyError: 'model.layers.24.mlp.down_proj.weight' for llama 7b model SqueezeLLM quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#4198](https://github.com/vllm-project/vllm/issues/4198) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'model.layers.24.mlp.down_proj.weight' for llama 7b model SqueezeLLM quantization

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (conda-forge gcc 12.3.0-5) 12.3.0 Clang version: 14.0.6 CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.11.8 | packaged by conda-forge | (main, Feb 16 2024, 20:53:32) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.4.0-100-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.91 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.4.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.4.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.4.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.4.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (conda-forge gcc 12.3.0-5) 12.3.0 Cl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: KeyError: 'model.layers.24.mlp.down_proj.weight' for llama 7b model SqueezeLLM quantization bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is deb...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: .24.mlp.down_proj.weight' for llama 7b model SqueezeLLM quantization bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: or: 'model.layers.24.mlp.down_proj.weight' for llama 7b model SqueezeLLM quantization bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: Fal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
