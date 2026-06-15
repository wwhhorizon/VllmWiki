# vllm-project/vllm#24564: [Bug]: When using DP8, runing seqs num in 8 engine is not average, perf loss

| 字段 | 值 |
| --- | --- |
| Issue | [#24564](https://github.com/vllm-project/vllm/issues/24564) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;moe;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using DP8, runing seqs num in 8 engine is not average, perf loss

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-5.4.119-19.0009.28-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.9.41 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 575.57.08 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.39 =================
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: n3 -m vllm.entrypoints.openai.api_server --model=/datasets/Qwen3-30B-A3B-FP8/ --no-enable-prefix-caching --seed=0 --quantization=fp8 --dtype bfloat16 --trust-remote-code --max-model-len=32768 --max-num-seqs=16 --kv-cach...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ge, perf loss bug ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 24.04.2 LTS (x86_64) GCC version : (Ubuntu 13.3....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: pip3] torch_tensorrt==2.8.0a0 [pip3] torchaudio==2.8.0+cu129 [pip3] torchprofile==0.0.4 [pip3] torchvision==0.23.0+cu129 [pip3] transformers==4.56.1 [pip3] triton==3.4.0 [conda] Could not collect =======================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
