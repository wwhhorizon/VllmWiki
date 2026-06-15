# vllm-project/vllm#21425: [Performance]: With exactly the same setting, two sets of data with similar average length have a large difference in inference speed

| 字段 | 值 |
| --- | --- |
| Issue | [#21425](https://github.com/vllm-project/vllm/issues/21425) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: With exactly the same setting, two sets of data with similar average length have a large difference in inference speed

### Issue 正文摘录

### Proposal to improve performance ```python llm = LLM( model=model_name_or_path, trust_remote_code=True, tensor_parallel_size=world_size, gpu_memory_utilization=0.6, swap_space=0 ) inference_params = { "temperature": 0.6, "max_tokens": 2048, "top_k": -1, "top_p": 1, "presence_penalty": 0, "frequency_penalty": 0, } sampling_params = SamplingParams(**inference_params) outputs = llm.generate(inputs, sampling_params) ``` - data_1 1. average_length : 1246.00 2. data_num : 3000 3. inference time : 390.836 secs - data_2 1. average_length : 1136.66 2. data_num : 3000 3. inference time : 78.150 secs I understand that if the average input length is shorter, we should have greater throughput and faster inference time for the same setup, but the experimental results do not follow this rule. In addition, the average length of the output of the two sets of data is also consistent. Why the difference? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: tand that if the average input length is shorter, we should have greater throughput and faster inference time for the same setup, but the experimental results do not follow this rule. In addition, the average length of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rmance ### Proposal to improve performance ```python llm = LLM( model=model_name_or_path, trust_remote_code=True, tensor_parallel_size=world_size, gpu_memory_utilization=0.6, swap_space=0 ) inference_params = { "tempera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
