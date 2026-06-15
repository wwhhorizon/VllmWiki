# vllm-project/vllm#37836: [Bug] Potential incorrect tokenizer source path in RunAI object storage pull

| 字段 | 值 |
| --- | --- |
| Issue | [#37836](https://github.com/vllm-project/vllm/issues/37836) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Potential incorrect tokenizer source path in RunAI object storage pull

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, thanks for the great work on vLLM! While reviewing the RunAI object storage integration, I noticed a potential inconsistency in `maybe_pull_model_tokenizer_for_runai`. In the tokenizer branch: object_storage_tokenizer = ObjectStorageModel(url=tokenizer) object_storage_tokenizer.pull_files( model, ignore_pattern=[...], ) Here, `model` is passed to `pull_files()` instead of `tokenizer`. From the RunAI Model Streamer S3 implementation: def pull_files(model_path: str, dst: str, ...): ... bucket_name, base_dir, files = list_files(s3, model_path, ...) ... s3.download_file(bucket_name, file, destination_file) The `model_path` argument is directly used as the object storage source for listing and downloading files. This suggests that in the tokenizer branch above, files would be pulled from `model` rather than `tokenizer`. This seems inconsistent with the expected behavior where model and tokenizer URIs are handled independently. When `model != tokenizer`, this may lead to: - tokenizer files being fetched from the model path - missing or incorrect tokenizer files - silent mismatch between model and tokenizer This issue is likely mask...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed from the model path - missing or incorrect tokenizer files - silent mismatch between model and tokenizer This issue is likely masked when `model == tokenizer`. The tokenizer branch would likely call: object_storage_t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ched from the model path - missing or incorrect tokenizer files - silent mismatch between model and tokenizer This issue is likely masked when `model == tokenizer`. The tokenizer branch would likely call: object_storage...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: storage integration, I noticed a potential inconsistency in `maybe_pull_model_tokenizer_for_runai`. In the tokenizer branch: object_storage_tokenizer = ObjectStorageModel(url=tokenizer) object_storage_tokenizer.pull_fil...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
