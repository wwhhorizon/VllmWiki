# vllm-project/vllm#39104: [Usage]: The qwen3.5 model generates a random stream of words in thought mode.

| 字段 | 值 |
| --- | --- |
| Issue | [#39104](https://github.com/vllm-project/vllm/issues/39104) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: The qwen3.5 model generates a random stream of words in thought mode.

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.12.0.dev20260405+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 3 2026, 12:15:18) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.17.0-1014-nvidia-aarch64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.2.51 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GB10 Nvidia driver version : 580.142 cuDNN version : Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.9.20.0 /usr/lib/aarch64-linux-gnu/libcudnn_adv.so.9.20.0 /usr/lib/aarch64-linux-gnu/libcudnn_cnn.so.9.20.0 /usr/lib/aarch64-linux-gnu/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ======== OS : Ubuntu 24.04.4 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ==================== OS : Ubuntu 24.04.4 LTS (aarch64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt Model name: Cortex-A725 BIOS Model name: GB10 To Be Filled by OEM CPU @ 3.9GHz BIOS CPU family: 258 Model:
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: : 2.12.0.dev20260405+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: The qwen3.5 model generates a random stream of words in thought mode. usage ### Your current environment ```text ============================== System Info ============================== OS

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
