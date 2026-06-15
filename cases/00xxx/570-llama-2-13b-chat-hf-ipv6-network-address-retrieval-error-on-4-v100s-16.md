# vllm-project/vllm#570: [Llama-2-13b-chat-hf] IPv6 Network Address Retrieval Error on 4 V100s 16GB

| 字段 | 值 |
| --- | --- |
| Issue | [#570](https://github.com/vllm-project/vllm/issues/570) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Llama-2-13b-chat-hf] IPv6 Network Address Retrieval Error on 4 V100s 16GB

### Issue 正文摘录

Hello, I'm encountering an issue while running the following code: ```python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-2-13b-chat-hf", tensor_parallel_size=2) ``` The hardware I'm using is 4 V100s with 16GB each. The error I'm receiving is as follows: ``` (Worker pid=22514) [W socket.cpp:601] [c10d] The IPv6 network addresses of (__internal_head__, 16516) cannot be retrieved (gai error: -2 - Name or service not known). (Worker pid=22513) [W socket.cpp:601] [c10d] The IPv6 network addresses of (__internal_head__, 16516) cannot be retrieved (gai error: -2 - Name or service not known). [repeated 10x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/ray-logging.html#log-deduplication for more options.) (Worker pid=22513) [W socket.cpp:601] [c10d] The IPv6 network addresses of (__internal_head__, 16516) cannot be retrieved (gai error: -2 - Name or service not known). [repeated 10x across cluster] ``` Any help or guidance on how to resolve this issue would be greatly appreciated. Thank you

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Llama-2-13b-chat-hf] IPv6 Network Address Retrieval Error on 4 V100s 16GB Hello, I'm encountering an issue while running the following code: ```python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Ll
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: untering an issue while running the following code: ```python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-2-13b-chat-hf", tensor_parallel_size=2) ``` The hardware I'm using is 4 V100s with 16G...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Llama-2-13b-chat-hf] IPv6 Network Address Retrieval Error on 4 V100s 16GB Hello, I'm encountering an issue while running the following code: ```python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Ll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
