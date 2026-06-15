# vllm-project/vllm#21593: [Bug]: MistralTokenizer is missing batch_decode, breaks /detokenize in OpenAI server

| 字段 | 值 |
| --- | --- |
| Issue | [#21593](https://github.com/vllm-project/vllm/issues/21593) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MistralTokenizer is missing batch_decode, breaks /detokenize in OpenAI server

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.36 ============================== PyTorch Info ============================== PyTorch version : 2.5.1+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.2 (main, Apr 28 2025, 14:11:48) [GCC 12.2.0] (64-bit runtime) Python platform : Linux-6.1.0-37-amd64-x86_64-with-glibc2.36 ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.36 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: ch version : 2.5.1+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.2 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: MistralTokenizer is missing batch_decode, breaks /detokenize in OpenAI server bug;stale ### Your current environment ============================== System Info ============================== OS : Debian GNU/Linux...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: he decoded text (list of strings for batched inputs) without requiring a fallback to the slower HF tokenizer. Actual The server raises AttributeError because MistralTokenizer lacks batch_decode. Environment vLLM: main (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
