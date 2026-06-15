# vllm-project/vllm#27129: [Feature]: Allow picking input, output lengths and prefix overlaps from a distribution for PrefixRandom dataset

| 字段 | 值 |
| --- | --- |
| Issue | [#27129](https://github.com/vllm-project/vllm/issues/27129) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow picking input, output lengths and prefix overlaps from a distribution for PrefixRandom dataset

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM’s bench serve currently supports a [PrefixRepetitionRandomDataset](https://github.com/vllm-project/vllm/blob/f50cc221ea7861686fec5ae9e949018c9628f328/vllm/benchmarks/datasets.py#L2945) for generating prompts with fixed-length prefix and suffix lengths. It also has support for a [RandomDataset](https://github.com/vllm-project/vllm/blob/f50cc221ea7861686fec5ae9e949018c9628f328/vllm/benchmarks/datasets.py#L441) which samples input and expected output lengths from a distribution and a fixed prefix length. For my use case benchmarking [llm-d ](https://github.com/llm-d/llm-d)which uses vLLM, I would like to combine the two into a PrefixRepetitionRandomLengthsDataset, which allows the following: * sampling input lengths from a distribution, given input length mean and standard deviation * sampling expected output lengths from a distribution, given output length mean and standard deviation * sampling prefix hit ratio from a distribution, given prefix hit ratio mean and standard deviation. Prefix length is calculated as follows: ``` prefix hit ratio = random.sample(prefix hit ratio mean, prefix hit ratio std) prefix length = prefix hit ratio * i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: and prefix overlaps from a distribution for PrefixRandom dataset feature request;stale ### 🚀 The feature, motivation and pitch vLLM’s bench serve currently supports a [PrefixRepetitionRandomDataset](https://github.com/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: com/vllm-project/vllm/blob/f50cc221ea7861686fec5ae9e949018c9628f328/vllm/benchmarks/datasets.py#L2945) for generating prompts with fixed-length prefix and suffix lengths. It also has support for a [RandomDataset](https:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: prefix_hit_ratio_std: int, num_prefixes: int, max_model_len: int, ... ) -> list[SampleRequest]: for _ in range(num_prefixes): prefix_tokens = _generate_tokens(MAX_PREFIX_LEN) all_prefixes.append(prefix_tokens) for ind

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
