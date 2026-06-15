# vllm-project/vllm#10257: [Usage]: How to Use a Public URL for Remote Access to a Deployed vLLM Model?

| 字段 | 值 |
| --- | --- |
| Issue | [#10257](https://github.com/vllm-project/vllm/issues/10257) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to Use a Public URL for Remote Access to a Deployed vLLM Model?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am trying to deploy and remotely access a vLLM model on a supercomputing cluster but am encountering some difficulties. Here are the details: 1. **Running vLLM Service on the Supercomputing Cluster** ```bash vllm serve "meta-llama/Llama-3.1-8B-Instruct" --port 8002 --api-key my_api_key ``` This command successfully starts the vLLM service on the cluster and listens on port 8002. 2. **Accessing the Model from an External Server Using the OpenAI Interface** ```python client = OpenAI( base_url=base_url, api_key=api_key, ) ``` However, with this configuration, I am unable to properly utilize the `base_url` to connect to the vLLM service deployed on the cluster. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to Use a Public URL for Remote Access to a Deployed vLLM Model? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am trying to d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ow to Use a Public URL for Remote Access to a Deployed vLLM Model? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am trying to deploy and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
