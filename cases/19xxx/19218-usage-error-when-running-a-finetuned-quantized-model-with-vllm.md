# vllm-project/vllm#19218: [Usage]: Error when running a finetuned, quantized model with vllm.

| 字段 | 值 |
| --- | --- |
| Issue | [#19218](https://github.com/vllm-project/vllm/issues/19218) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Error when running a finetuned, quantized model with vllm.

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version : Could not collect CMake version : version 3.26.4 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.4.0+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.143.bsk.5-oci-amd64-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.1.105 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB Nvidia driver version : 470.103.01 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_trai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version : Could not collect CMake version : version 3.26.4 Libc version : glibc-2.31 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.4.0+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.13 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Error when running a finetuned, quantized model with vllm. usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Usage]: Error when running a finetuned, quantized model with vllm. usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: Error when running a finetuned, quantized model with vllm. usage;stale ### Your current environment ```text ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
