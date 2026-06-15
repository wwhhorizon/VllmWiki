# vllm-project/vllm#26614: [Usage]: attn_metadata.seq_lens is not equal to attn_metadata.num_actual_tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#26614](https://github.com/vllm-project/vllm/issues/26614) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: attn_metadata.seq_lens is not equal to attn_metadata.num_actual_tokens

### Issue 正文摘录

### Your current environment ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jul 23 2025, 00:34:44) [Clang 20.1.4 ] (64-bit runtime) Python platform : Linux-5.4.0-216-generic-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 555.42.06 cuDNN version : Could not collect HIP runtime version...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.31 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Usage]: attn_metadata.seq_lens is not equal to attn_metadata.num_actual_tokens usage;stale ### Your current environment ``` Collecting environment information... uv is set ============================== System Info ===...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s usage;stale ### Your current environment ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ub...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: _metadata.seq_lens is not equal to attn_metadata.num_actual_tokens usage;stale ### Your current environment ``` Collecting environment information... uv is set ============================== System Info ================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
