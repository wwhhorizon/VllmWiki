# vllm-project/vllm#6567: [Bug]: gptq model fails on pascal gpu with long prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#6567](https://github.com/vllm-project/vllm/issues/6567) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gptq model fails on pascal gpu with long prompt

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] (64-bit runtime) Python platform: Linux-4.14.83-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla P40 GPU 1: Tesla P40 Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.3 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.3 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: l gpu with long prompt bug ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04.1) 11.3....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gptq model fails on pascal gpu with long prompt bug ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: transformers==4.42.4 [pip3] transformers-stream-generator==0.0.4 [pip3] triton==2.3.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.1 vLLM Build Flags: CUDA Archs: N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: t/ --gpu-memory-utilization 0.95 --max-model-len 4096 --max-num-seqs 1 --dtype half ``` fp16 works fine with short or long prompt: ``` INFO 07-19 15:44:53 metrics.py:295] Avg prompt throughput: 107.4 tokens/s, Avg gener...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
