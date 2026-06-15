# vllm-project/vllm#21163: [Usage]: Does benchmark_serving.py support setting the number of repeated prompt num?

| 字段 | 值 |
| --- | --- |
| Issue | [#21163](https://github.com/vllm-project/vllm/issues/21163) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does benchmark_serving.py support setting the number of repeated prompt num?

### Issue 正文摘录

### Your current environment I want to verify the effect of setting the number of repeated prompt words on service performance parameters, but I found that there are no relevant parameters in benchmark_serving.py. How can I achieve this? Of course, the benchmark_prefix_caching.py script is currently provided, but there is no performance parameter index such as ttft. More importantly, its service and test are not separated. I saw this function and felt it was possible, but currently benchmark_serving.py does not support it! https://github.com/vllm-project/vllm/tree/main/benchmarks/benchmark_long_document_qa_throughput.py ``` def repeat_prompts(prompts, repeat_count, mode: str): """ Repeat each prompt in the list for a specified number of times. The order of prompts in the output list depends on the mode. Args: prompts: A list of prompts to be repeated. repeat_count: The number of times each prompt is repeated. mode: The mode of repetition. Supported modes are: - 'random': Shuffle the prompts randomly after repetition. - 'tile': Repeat the entire prompt list in sequence. Example: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]. - 'interleave': Repeat each prompt consecutively before moving to the n...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: provided, but there is no performance parameter index such as ttft. More importantly, its service and test are not separated. I saw this function and felt it was possible, but currently benchmark_serving.py does not sup...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: Does benchmark_serving.py support setting the number of repeated prompt num? usage;stale ### Your current environment I want to verify the effect of setting the number of repeated prompt words on service perfor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pts.extend([prompt] * repeat_count) return repeated_prompts else: raise ValueError( f"Invalid mode: {mode}, only support 'random', 'tile', 'interleave'" ) ``` ### How would you like to use vllm I want to run inference o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
