# vllm-project/vllm#18832: [Bug]: Error during serialization of the model.

| 字段 | 值 |
| --- | --- |
| Issue | [#18832](https://github.com/vllm-project/vllm/issues/18832) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Error during serialization of the model.

### Issue 正文摘录

### Your current environment ``` Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Feb 4 2025, 14:57:36) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.1.119-129.201.amzn2023.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA L4 Nvidia driver version : 560.35.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ======================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ;stale ### Your current environment ``` Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error during serialization of the model. bug;stale ### Your current environment ``` Automatically detected platform cuda. Collecting environment information... ============================== System Info =========...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ilable() else 1 def serialize_vllm_model(model_id: str, save_path: str, dtype: str, max_model_len: int) -> str: tensor_parallel_size = get_tensor_parallel_size() print(f"vLLM Model Serialization Detected {tensor_paralle...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Error during serialization of the model. bug;stale ### Your current environment ``` Automatically detected platform cuda. Collecting environment information... ============================== System Info =========...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
