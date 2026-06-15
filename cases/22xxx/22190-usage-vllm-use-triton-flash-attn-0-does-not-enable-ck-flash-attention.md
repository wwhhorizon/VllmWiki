# vllm-project/vllm#22190: [Usage]: VLLM_USE_TRITON_FLASH_ATTN=0 does not enable CK flash attention

| 字段 | 值 |
| --- | --- |
| Issue | [#22190](https://github.com/vllm-project/vllm/issues/22190) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: VLLM_USE_TRITON_FLASH_ATTN=0 does not enable CK flash attention

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525bc7d01f727) CMake version : version 4.0.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.9.0a0+git880249a Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43483-a187df25c ============================== Python Environment ============================== Python version : 3.10.18 | packaged by conda-forge | (main, Jun 4 2025, 14:45:41) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-60-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : AMD Instinct MI100 (gfx908:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n : 2.9.0a0+git880249a Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43483-a187df25c ============================== Python Environment ============================== Python ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: age;stale ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Usage]: VLLM_USE_TRITON_FLASH_ATTN=0 does not enable CK flash attention usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ================...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ]: VLLM_USE_TRITON_FLASH_ATTN=0 does not enable CK flash attention usage;stale ### Your current environment ```text Collecting environment information... ============================== System Info ======================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
