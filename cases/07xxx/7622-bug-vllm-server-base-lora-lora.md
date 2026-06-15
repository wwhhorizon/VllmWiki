# vllm-project/vllm#7622: [Bug]: vllm server 部署base和lora模型后，请求lora模型失败

| 字段 | 值 |
| --- | --- |
| Issue | [#7622](https://github.com/vllm-project/vllm/issues/7622) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm server 部署base和lora模型后，请求lora模型失败

### Issue 正文摘录

### Your current environment 部署指令： vllm serve /root/autodl-fs/llm_models/qwen/Qwen2-7B-Instruct --enable-lora --lora-modules bi-lora=/root/autodl-fs/saves/Qwen2-7B-Instruct/lora/sft/checkpoint-1500/ --port 6006 请求体： { "model": "bi-lora", "prompt": "你是谁", "temperature": 0.7, "top_p": 0.8, "repetition_penalty": 1.05, "max_tokens": 512 } 报错信息：RuntimeError: Loading lora /root/autodl-fs/saves/Qwen2-7B-Instruct/lora/sft/checkpoint-1500/ failed 如果 访问base模型是没问题的（model改成 /root/autodl-fs/llm_models/qwen/Qwen2-7B-Instruct） ### 🐛 Describe the bug PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.3 | packaged by Anaconda, Inc. | (main, May 6 2024, 19:46:43) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-91-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 Nvidia driver version: 550.54.14 cuDNN version: Probably on...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: l-fs/llm_models/qwen/Qwen2-7B-Instruct） ### 🐛 Describe the bug PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: # 🐛 Describe the bug PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: stale ### Your current environment 部署指令： vllm serve /root/autodl-fs/llm_models/qwen/Qwen2-7B-Instruct --enable-lora --lora-modules bi-lora=/root/autodl-fs/saves/Qwen2-7B-Instruct/lora/sft/checkpoint-1500/ --port 6006 请求...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm server 部署base和lora模型后，请求lora模型失败 bug;stale ### Your current environment 部署指令： vllm serve /root/autodl-fs/llm_models/qwen/Qwen2-7B-Instruct --enable-lora --lora-modules bi-lora=/root/autodl-fs/saves/Qwen2-7B-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx_vnni avx512_bf16 wbnoinvd arat avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid cldemo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
