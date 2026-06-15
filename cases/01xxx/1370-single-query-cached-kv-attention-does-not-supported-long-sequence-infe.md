# vllm-project/vllm#1370: single_query_cached_kv_attention  does not supported long sequence inference.

| 字段 | 值 |
| --- | --- |
| Issue | [#1370](https://github.com/vllm-project/vllm/issues/1370) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 | edge_case |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> single_query_cached_kv_attention  does not supported long sequence inference.

### Issue 正文摘录

In 'test_attention.py': MAX_SEQ_LEN=get_max_shared_memory_bytes() // FLOAT32_BYTES - 512 In my A100 env, the MAX_SEQ_LEN = 41216. While, when my kv seq len is larger than the value, such as 65536, the kernel will failed.the error like this: " E RuntimeError: CUDA error: invalid argument E CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. E For debugging consider passing CUDA_LAUNCH_BLOCKING=1. E Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. " How can I fix it?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: For debugging consider passing CUDA_LAUNCH_BLOCKING=1. E Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. " How can I fix it? correctness ci_build;frontend_api cuda;kernel build_error;mismatch shape I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : MAX_SEQ_LEN=get_max_shared_memory_bytes() // FLOAT32_BYTES - 512 In my A100 env, the MAX_SEQ_LEN = 41216. While, when my kv seq len is larger than the value, such as 65536, the kernel will failed.the error like this:...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: can I fix it? correctness ci_build;frontend_api cuda;kernel build_error;mismatch shape In 'test_attention.py': MAX_SEQ_LEN=get_max_shared_memory_bytes() // FLOAT32_BYTES - 512
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ce. In 'test_attention.py': MAX_SEQ_LEN=get_max_shared_memory_bytes() // FLOAT32_BYTES - 512 In my A100 env, the MAX_SEQ_LEN = 41216. While, when my kv seq len is larger than the value, such as 65536, the kernel will fa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: be incorrect. E For debugging consider passing CUDA_LAUNCH_BLOCKING=1. E Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. " How can I fix it? correctness ci_build;frontend_api cuda;kernel build_error;...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
