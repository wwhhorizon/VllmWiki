# vllm-project/vllm#31056: [Bug]: GLM4-MoE AssertionError with --all2all-backend pplx (dtype mismatch)

| 字段 | 值 |
| --- | --- |
| Issue | [#31056](https://github.com/vllm-project/vllm/issues/31056) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM4-MoE AssertionError with --all2all-backend pplx (dtype mismatch)

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 (main, Oct 28 2025, 12:10:49) [Clang 20.1.4 ] (64-bit runtime) Python platform : Linux-6.2.0-1015-nvidia-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version : 550.90.07 cuDNN version : Cou...

## 现有链接修复摘要

#31055 [Bugfix] Fix GLM-4 MoE router logits dtype for data parallel chunking

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: GLM4-MoE AssertionError with --all2all-backend pplx (dtype mismatch) bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: GLM4-MoE AssertionError with --all2all-backend pplx (dtype mismatch) bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_6...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: GLM4-MoE AssertionError with --all2all-backend pplx (dtype mismatch) bug;stale ### Your current environment ============================== System Info ============================== OS : Ubu

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31055](https://github.com/vllm-project/vllm/pull/31055) | closes_keyword | 0.95 | [Bugfix] Fix GLM-4 MoE router logits dtype for data parallel chunking | fix): Server starts successfully with `--all2all-backend pplx`. Related issue: #31056 #### Environment info ```bash ============================== System Info ========== |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
