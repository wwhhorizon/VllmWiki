# vllm-project/vllm#5199: [Bug]: Issues with Applying LoRA in vllm on a T4 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#5199](https://github.com/vllm-project/vllm/issues/5199) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issues with Applying LoRA in vllm on a T4 GPU

### Issue 正文摘录

### Your current environment I am currently using a T4 instance on Google Colaboratory. ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.27.9 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.1.85+-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla T4 Nvidia driver version: 535.104.05 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.6 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: Google Colaboratory. ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: sing a T4 instance on Google Colaboratory. ``` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: nown Vulnerability Meltdown: Vulnerable Vulnerability Mmio stale data: Vulnerable Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Vulnerable Vulnerability Spec rstack overflow: Not affected Vu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: utilization=VLLM_GPU_MEMORY_UTILIZATION, trust_remote_code=True, dtype=torch.float16, enforce_eager=True, enable_lora=True ) ``` which yields the following output: ``` ---------------------------------------------------...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
