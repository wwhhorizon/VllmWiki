# vllm-project/vllm#645: The IPv6 network addresses of (__internal_head__, 18566) cannot be retrieved

| 字段 | 值 |
| --- | --- |
| Issue | [#645](https://github.com/vllm-project/vllm/issues/645) |
| 状态 | closed |
| 标签 |  |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The IPv6 network addresses of (__internal_head__, 18566) cannot be retrieved

### Issue 正文摘录

I run this code ```python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-2-70b-chat-hf", tensor_parallel_size=4) ``` get errors: ``` (Worker pid=816915) [W socket.cpp:601] [c10d] The IPv6 network addresses of (__internal_head__, 18566) cannot be retrieved (gai error: -2 - Name or service not known). [repeated 20x across cluster] (Worker pid=816915) [W socket.cpp:601] [c10d] The IPv6 network addresses of (__internal_head__, 18566) cannot be retrieved (gai error: -2 - Name or service not known). [repeated 20x across cluster] (Worker pid=816915) [W socket.cpp:601] [c10d] The IPv6 network addresses of (__internal_head__, 18566) cannot be retrieved (gai error: -2 - Name or service not known). [repeated 20x across cluster] (Worker pid=816915) [W socket.cpp:601] [c10d] The IPv6 network addresses of (__internal_head__, 18566) cannot be retrieved (gai error: -2 - Name or service not known). [repeated 20x across cluster] ``` I ref #570 this issue, export NCCL_IGNORE_DISABLED_P2P=1,and then wait for 8mins, run code, above error happen again Any help or guidance on how to resolve this issue would be greatly appreciated. Thank you

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: I run this code ```python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-2-70b-chat-hf", tensor_parallel_size=4) ``` get errors: ``` (Worker pid=816915) [W socket.cpp:601] [c10d] The IPv6 network...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l_head__, 18566) cannot be retrieved I run this code ```python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-2-70b-chat-hf", tensor_parallel_size=4) ``` get errors: ``` (Worker pid=816915) [W so...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
