# vllm-project/vllm#19584: [Usage]: Gemma3 not supported on B200 w/ Flash-Infer

| 字段 | 值 |
| --- | --- |
| Issue | [#19584](https://github.com/vllm-project/vllm/issues/19584) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Gemma3 not supported on B200 w/ Flash-Infer

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.1 (main, Jan 8 2024, 04:46:10) [Clang 17.0.6 ] (64-bit runtime) Python platform : Linux-4.4.0-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA B200 Nvidia driver version : 570.86.15 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Add...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Usage]: Gemma3 not supported on B200 w/ Flash-Infer usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC versi
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Gemma3 not supported on B200 w/ Flash-Infer usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 22.04.
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: u128 [pip3] torchvision==0.22.0+cu128 [pip3] transformers==4.52.4 [pip3] triton==3.3.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: diri movdir64b fsrm md_clear serialize tsxldtrk pconfig arch_lbr ibt amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities Virtualization: VT-x ============================== Versions of relevant libraries...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
