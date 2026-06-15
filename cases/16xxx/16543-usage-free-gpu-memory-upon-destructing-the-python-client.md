# vllm-project/vllm#16543: [Usage]: Free GPU memory upon destructing the Python client

| 字段 | 值 |
| --- | --- |
| Issue | [#16543](https://github.com/vllm-project/vllm/issues/16543) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Free GPU memory upon destructing the Python client

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.12.7 (main, Apr 9 2025, 11:35:32) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.11.0-19-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.8.93 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 GPU 2: NVIDIA L4 GPU 3: NVIDIA L4 GPU 4: NVIDIA L4 GPU 5: NVIDIA L4 GPU 6: NVIDIA L4 GPU 7: NVIDIA L4 Nvidia driver version: 570.124.06 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.7 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.7 /usr/lib/x...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req hfi vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ent usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.2...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Usage]: Free GPU memory upon destructing the Python client usage ### Your current environment ```text Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
