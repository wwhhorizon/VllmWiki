# vllm-project/vllm#11286: [Performance]: decoding speed on long context

| 字段 | 值 |
| --- | --- |
| Issue | [#11286](https://github.com/vllm-project/vllm/issues/11286) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 54; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: decoding speed on long context

### Issue 正文摘录

### Proposal to improve performance In our experiments, we found that the decoding speed of vLLM decreases dramatically when the length of the prompt becomes longer. We fixed the batchsize=90 the decoding speed is 5364 tokens/s when the length of the prompt is within 100, 5500 tokens/s when 100 to 200, and decreases to 782 when 4000 to 8000, and decreases to 273 when greater than 8000. prompt length | 0-100 | 100-200 | 200-500 | 500-1000 | 1000-2000 | 2000-4000 | 4000-8000 | 8000+ -- | -- | -- | -- | -- | -- | -- | -- | -- words/s | 5364 | 5500 | 4722 | 2815 | 2484 | 1627 | 782 | 273 GPU is single A800, 80G, vLLM block_size=16, max_num_seqs=512, max_model_len=8192, max_tokens=200. Is that why page attention is accessed more often? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: at why page attention is accessed more often? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 2 | 2815 | 2484 | 1627 | 782 | 273 GPU is single A800, 80G, vLLM block_size=16, max_num_seqs=512, max_model_len=8192, max_tokens=200. Is that why page attention is accessed more often? ### Report of performance regressi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: GPU is single A800, 80G, vLLM block_size=16, max_num_seqs=512, max_model_len=8192, max_tokens=200. Is that why page attention is accessed more often? ### Report of performance regression _No response_ ### Misc discussio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: decoding speed on long context performance;stale ### Proposal to improve performance In our experiments, we found that the decoding speed of vLLM decreases dramatically when the length of the prompt becom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
