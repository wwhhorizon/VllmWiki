# vllm-project/vllm#905: vLLM doesn't support context length exceeding about 13k

| 字段 | 值 |
| --- | --- |
| Issue | [#905](https://github.com/vllm-project/vllm/issues/905) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM doesn't support context length exceeding about 13k

### Issue 正文摘录

I use 4 A100 80G. vLLM runs perfectly with my code when context length is up to 11k, but when it exceeds around 13k, I've got the error shown below: ``` RuntimeError: CUDA error: invalid argument CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` Given the fact that pure hf code can run up to that length with 4 A100*80G, it can be a memory-related issue, so I'm wondering what might be the issue. (I've set `max_num_batched_tokens` and `get_max_model_len` large enough)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ht be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` Given the fact that pure hf code can run up to that length with 4 A100*80G,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM doesn't support context length exceeding about 13k bug I use 4 A100 80G. vLLM runs perfectly with my code when context length is up to 11k, but when it exceeds around 13k, I've got the error shown below: ``` Runtim...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: UDA_DSA` to enable device-side assertions. ``` Given the fact that pure hf code can run up to that length with 4 A100*80G, it can be a memory-related issue, so I'm wondering what might be the issue. (I've set `max_num_b...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: large enough) correctness ci_build;frontend_api cuda;kernel build_error;mismatch I use 4 A100 80G.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ce below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` Given the fact that pure hf code can run up to that length with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
