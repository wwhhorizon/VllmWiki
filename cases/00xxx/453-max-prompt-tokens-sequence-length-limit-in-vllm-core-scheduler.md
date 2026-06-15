# vllm-project/vllm#453: Max prompt tokens/sequence length limit in vllm core scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#453](https://github.com/vllm-project/vllm/issues/453) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Max prompt tokens/sequence length limit in vllm core scheduler

### Issue 正文摘录

### Discussed in https://github.com/vllm-project/vllm/discussions/446 Originally posted by **yuanheng-zhao** July 12, 2023 I noticed that the following block (https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L193) was added to vllm core scheduler ```python if num_prompt_tokens >= self.scheduler_config.max_seq_len: logger.warning( f"Input prompt ({num_prompt_tokens} tokens) is too long" " and exceeds limit of " f"{self.scheduler_config.max_seq_len}") for seq in seq_group.get_seqs(): seq.status = SequenceStatus.FINISHED_IGNORED ignored_seq_groups.append(seq_group) self.waiting.pop(0) break ``` as a fix for the issue https://github.com/vllm-project/vllm/issues/113 I wonder why we're not using `num_prompt_tokens > self.scheduler_config.max_seq_len` as a condition? It seems to filter out input sequences with exact length (e.g. `--input-len 1024`) for benchmarks. Thank you for your instruction! *** I was running the [benchmark script](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_latency.py) `benchmark_latency.py` with llama-7b, input_length == 1024, output length == 128, fp16, and bs == 1. The above block of code seems to cause the following w...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: to vllm core scheduler ```python if num_prompt_tokens >= self.scheduler_config.max_seq_len: logger.warning( f"Input prompt ({num_prompt_tokens} tokens) is too long" " and exceeds limit of " f"{self.scheduler_config.max_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: lter out input sequences with exact length (e.g. `--input-len 1024`) for benchmarks. Thank you for your instruction! *** I was running the [benchmark script](https://github.com/vllm-project/vllm/blob/main/benchmarks/ben...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -testing/llama-tokenizer', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) INFO 07-13 14:16:25 tokeniz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: posted by **yuanheng-zhao** July 12, 2023 I noticed that the following block (https://github.com/vllm-project/vllm/blob/main/vllm/core/scheduler.py#L193) was added to vllm core scheduler ```python if num_prompt_tokens >...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Max prompt tokens/sequence length limit in vllm core scheduler bug ### Discussed in https://github.com/vllm-project/vllm/discussions/446 Originally posted by **yuanheng-zhao** July 12, 2023 I noticed that the following...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
