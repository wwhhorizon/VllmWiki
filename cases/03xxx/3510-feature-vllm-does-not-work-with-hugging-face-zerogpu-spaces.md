# vllm-project/vllm#3510: [Feature]: vLLM does not work with Hugging Face ZeroGPU Spaces

| 字段 | 值 |
| --- | --- |
| Issue | [#3510](https://github.com/vllm-project/vllm/issues/3510) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: vLLM does not work with Hugging Face ZeroGPU Spaces

### Issue 正文摘录

Information about HF ZeroGPU Spaces can be found here: https://huggingface.co/zero-gpu-explorers The environment and code for this issue is kept fully within this Hugging Face space, specifically the `app.py` for the expected working code for being able to run a chat with vLLM: https://huggingface.co/spaces/mgoin/vllm-zero-gpu ### Your current environment Interestingly, it seems like ZeroGPU Spaces really don't have GPUs available at startup. This is clearly an issue :) ```text Collecting environment information... /usr/local/lib/python3.10/site-packages/torch/cuda/__init__.py:611: UserWarning: Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: version 3.25.1 Libc version: glibc-2.36 Python version: 3.10.13 (main, Mar 12 2024, 12:16:25) [GCC 12.2.0] (64-bit runtime) Python platform: Linux-5.10.192-183.736.amzn2.x86_64-x86_64-with-glibc2.36 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: and code for this issue is kept fully within this Hugging Face space, specifically the `app.py` for the expected working code for being able to run a chat with vLLM: https://huggingface.co/spaces/mgoin/vllm-zero-gpu ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment information... /usr/local/lib/python3.10/site-packages/torch/cuda/__init__.py:611: UserWarning: Can't initialize NVML warnings.warn("Can't initialize NVML") PyTorch version: 2.1.2+cu121 Is debug build: False...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: eature]: vLLM does not work with Hugging Face ZeroGPU Spaces bug;stale Information about HF ZeroGPU Spaces can be found here: https://huggingface.co/zero-gpu-explorers The environment and code for this issue is kept ful...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.3.3 vLLM Build Flags: CUDA Archs: N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
