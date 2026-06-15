# vllm-project/vllm#4665: [Bug]: Unable to use vLLM for serving fine tuned mistral model 

| 字段 | 值 |
| --- | --- |
| Issue | [#4665](https://github.com/vllm-project/vllm/issues/4665) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to use vLLM for serving fine tuned mistral model 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: Could not collect Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.10.213-201.855.amzn2.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-16GB GPU 1: Tesla V100-SXM2-16GB GPU 2: Tesla V100-SXM2-16GB GPU 3: Tesla V100-SXM2-16GB Nvidia driver version: 535.161.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz CPU family: 6 Model: 79 Thr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: f `python collect_env.py` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Unable to use vLLM for serving fine tuned mistral model usage;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.2.1+cu121 Is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: Could not collect Clang version: Cou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unable to use vLLM for serving fine tuned mistral model usage;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.2.1+cu121 Is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: del TheBloke/Mistral-7B-Instruct-v0.2-GPTQ --served-model-name mistral --dtype float16 --tokenizer TheBloke/Mistral-7B-Instruct-v0.2-GPTQ --enable-lora --lora-modules tuned-model=/model/v1 -q gptq INFO 05-08 00:44:27 ap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
