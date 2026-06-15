# vllm-project/vllm#7252: [Feature]: Support to use draft models with different vocabulary sizes for speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#7252](https://github.com/vllm-project/vllm/issues/7252) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support to use draft models with different vocabulary sizes for speculative decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In most open-source LLM families, models with different parameters use the same tokenizer and vocabulary. However, due to differences in GPU infrastructure during training, they might use different numbers of padding tokens, resulting in different `vocab_size` values. For instance, the `vocab_size` of Qwen2's [1.5B version](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct/blob/main/config.json) is **151936**, while the [72B version](https://huggingface.co/Qwen/Qwen2-72B-Instruct/blob/main/config.json) is **152064**. These padding tokens are essentially [meaningless at inference time](https://github.com/QwenLM/Qwen2/issues/466), but when used for speculative decoding, vLLM raises an error due to the mismatch in vocabulary size. Therefore, I propose adding an engine argument, such as `--disable-vocab-check-for-spec-decoding`, to allow the use of draft models with different vocabulary sizes upon user confirmation. ### Alternatives Adding a new engine argument is definitely the most reliable approach. Alternatively, perhaps we can relax the check on vocabulary sizes, ensuring only that the draft model's `vocab_size` is less than or equal to that...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support to use draft models with different vocabulary sizes for speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch In most open-source LLM families, models with different param...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Support to use draft models with different vocabulary sizes for speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch In most open-source LLM families, models with different param...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: but when used for speculative decoding, vLLM raises an error due to the mismatch in vocabulary size. Therefore, I propose adding an engine argument, such as `--disable-vocab-check-for-spec-decoding`, to allow the use of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nt `vocab_size` values. For instance, the `vocab_size` of Qwen2's [1.5B version](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct/blob/main/config.json) is **151936**, while the [72B version](https://huggingface.co/Qwen/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut when used for speculative decoding, vLLM raises an error due to the mismatch in vocabulary size. Therefore, I propose adding an engine argument, such as `--disable-vocab-check-for-spec-decoding`, to allow the use of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
