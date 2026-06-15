# vllm-project/vllm#7693: [Bug]: Inconsistent Output Behavior with and without tools and tool_choice Parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#7693](https://github.com/vllm-project/vllm/issues/7693) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistent Output Behavior with and without tools and tool_choice Parameters

### Issue 正文摘录

### Your current environment v0.5.4 In the VLLM server setup, specifying tools and tool_choice parameters produces a direct output, while omitting them leads to a descriptive response about the intended function call. This inconsistency arises regardless of identical token inputs, highlighting a potential issue in handling these parameters. ### 🐛 Describe the bug This is how my prompt looks after applying chat template: ``` You have access to a range of tools designed to assist you with various tasks. These tools enable you to perform specific functions and provide more precise and effective responses. Here are the tools you can utilize: \n {'name': 'get_current_weather', 'description': 'Get the current weather', 'parameters': {'type': 'object', 'properties': {'location': {'type': 'string', 'description': 'The city and state, e.g. San Francisco, CA'}}, 'required': ['location']}} \n [INST] What is the weather for Istanbul? [/INST] ``` Here are the token IDs for the above prompt: ``` [1, 529, 8504, 29958, 887, 505, 2130, 304, 263, 3464, 310, 8492, 8688, 304, 6985, 366, 411, 5164, 9595, 29889, 4525, 8492, 9025, 366, 304, 2189, 2702, 3168, 322, 3867, 901, 18378, 322, 11828, 20890, 298...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: and tool_choice parameters along with a dummy message: ``` data = { "model": "allam", "messages": [ { "role": "user", "content": """What is the weather for Istanbul?""", } ], "tools": [ { "my_function" } ]
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nt Output Behavior with and without tools and tool_choice Parameters bug;stale ### Your current environment v0.5.4 In the VLLM server setup, specifying tools and tool_choice parameters produces a direct output, while om...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ;stale ### Your current environment v0.5.4 In the VLLM server setup, specifying tools and tool_choice parameters produces a direct output, while omitting them leads to a descriptive response about the intended function...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: get_current_weather"}, "type": "function"}, "skip_special_tokens": False, } response = requests.post(url, headers=headers, json=data) ``` Output: ``` "{ \"location\": \"Istanbul\" } ``` Scenario 2. Do not pass tools and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 4, 25580, 29962] ``` Now, the same token IDs are passed for inference. I tested two scenarios as follows: Scenario 1: Pass tools and tool_choice parameters along with a dummy message: ``` data = { "model": "allam", "mes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
