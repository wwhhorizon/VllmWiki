# vllm-project/vllm#16330: [Bug]: meta-llama/Llama-4-Scout-17B-16E-Instruct compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#16330](https://github.com/vllm-project/vllm/issues/16330) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: meta-llama/Llama-4-Scout-17B-16E-Instruct compatibility

### Issue 正文摘录

### Your current environment Error while deploying the LLM ### 🐛 Describe the bug Loading safetensors checkpoint shards: 96% Completed | 48/50 [00:03 what(): CUDA error: device-side assert triggered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:43 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7f8f1ef6c1b6 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x64 (0x7f8f1ef15a76 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) frame #2: c10::cuda::c10_cuda_check_implementation(int, char const*, char const*, int, bool) + 0x118 (0x7f8f1f355918 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10_cuda.so) frame #3: + 0x103ad78 (0x7f8ecd065d78 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #4:...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: afetensors checkpoint shards: 96% Completed | 48/50 [00:03 what(): CUDA error: device-side assert triggered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: meta-llama/Llama-4-Scout-17B-16E-Instruct compatibility bug ### Your current environment Error while deploying the LLM ### 🐛 Describe the bug Loading safetensors checkpoint shards: 96% Completed | 48/50 [00:03 wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: api;model_support cuda;kernel build_error;mismatch env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation Your curre...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: correctness ci_build;frontend_api;model_support cuda;kernel build_error;mismatch env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search &...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0x10433c5 (0x7f8ecd06e3c5 in /usr/local/lib/python3.10/dist-packages/torch/lib/libto… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | ocal/lib/python3.10/dist-packages/torch/lib/libtorch_python.so) frame #6: <unknown function> + 0x6f30f (0x7f8f1ef4d30f in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) frame #7: c10::tensorimpl::~tensorimpl() + 0x21b (0x7f8f1ef4633b in /usr/local/lib/python3.10/dist-packages/torch/l… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
