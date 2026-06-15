# vllm-project/vllm#28640: [Bug]: LoRA/Adapter Loading Error with Qwen3-VL-8B-Instruct Multimodal Model in vLLM Deployment (AssertionError in lora_shrink_op)

| 字段 | 值 |
| --- | --- |
| Issue | [#28640](https://github.com/vllm-project/vllm/issues/28640) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm |
| 子分类 | cold_start |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA/Adapter Loading Error with Qwen3-VL-8B-Instruct Multimodal Model in vLLM Deployment (AssertionError in lora_shrink_op)

### Issue 正文摘录

============================== System Info ============================== OS : CentOS Linux 7 (Core) (x86_64) GCC version : (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.28 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 | packaged by conda-forge | (main, Apr 15 2024, 18:38:13) [GCC 12.3.0] (64-bit runtime) Python platform : Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.28 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.2.91 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version : 535.129.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ====== OS : CentOS Linux 7 (Core) (x86_64) GCC version : (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.28 ============
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: LoRA/Adapter Loading Error with Qwen3-VL-8B-Instruct Multimodal Model in vLLM Deployment (AssertionError in lora_shrink_op) bug;unstale ============================== System Info ============================== OS...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 |...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: orch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: the Qwen3-VL-8B-Instruct multimodal model using vLLM version 0.11.0 (and tested with 0.12.0). LoRA adapter trained via LLaMA-Factory, with weights containing only language model parameters (vision encoder is frozen and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
