# vllm-project/vllm#6737: [Usage]: use vllm==0.4.2 to infer qwen2-0.5b model on H800 1*80G,but GPU's computational power utilization is only around 20%

| 字段 | 值 |
| --- | --- |
| Issue | [#6737](https://github.com/vllm-project/vllm/issues/6737) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: use vllm==0.4.2 to infer qwen2-0.5b model on H800 1*80G,but GPU's computational power utilization is only around 20%

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.18.0-348.7.1.el8_5.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.128 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H800 GPU 1: NVIDIA H800 GPU 2: NVIDIA H800 GPU 3: NVIDIA H800 GPU 4: NVIDIA H800 GPU 5: NVIDIA H800 GPU 6: NVIDIA H800 GPU 7: NVIDIA H800 Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.4 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.4 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.4 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.4 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.4 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.4 /usr/lib/x86...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC ver...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: n collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: use vllm==0.4.2 to infer qwen2-0.5b model on H800 1*80G,but GPU's computational power utilization is only around 20% usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` Py...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: not possible to achieve over 90% utilization like the 70b model, and the GPU memory doesn't get fully occupied either. ![image](https://github.com/user-attachments/assets/5bf405eb-c3af-4a7d-84a7-be70be7be96c) Here is de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
