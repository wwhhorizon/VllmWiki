# vllm-project/vllm#25882: [Bug]: Eagle3 speculative decoding fails with quantized verifier + unquantized drafter

| 字段 | 值 |
| --- | --- |
| Issue | [#25882](https://github.com/vllm-project/vllm/issues/25882) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Eagle3 speculative decoding fails with quantized verifier + unquantized drafter

### Issue 正文摘录

### Your current environment Output of collect_env.py: ```bash uv is set ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : Could not collect CMake version : version 3.26.5 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Aug 14 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-11)] (64-bit runtime) Python platform : Linux-5.14.0-611.el9.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H...

## 现有链接修复摘要

#25883 [Bugfix][Speculative Decoding] Fix Eagle3 quantization config issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ============ OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : Could not collect CMake version : version 3.26.5 Libc version : glibc-2.34 =============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: untime version : 12.9.86 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Eagle3 speculative decoding fails with quantized verifier + unquantized drafter bug ### Your current environment Output of collect_env.py: ```bash uv is set ============================== System Info ============...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Eagle3 speculative decoding fails with quantized verifier + unquantized drafter bug ### Your current environment Output of collect_env.py: ```bash uv is set ============================== System Info ============...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25883](https://github.com/vllm-project/vllm/pull/25883) | closes_keyword | 0.95 | [Bugfix][Speculative Decoding] Fix Eagle3 quantization config issue | Fixes #25882 ## Problem Eagle3 drafters were incorrectly inheriting the verifier's quantization configuration instead of using their own, causing `KeyError: 'layers.0.mlp.down_pro |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
