# vllm-project/vllm#15274: [Bug]:streming is lost in arguments in tool_calls 

| 字段 | 值 |
| --- | --- |
| Issue | [#15274](https://github.com/vllm-project/vllm/issues/15274) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:streming is lost in arguments in tool_calls 

### Issue 正文摘录

### Your current environment vllm 0.7.3 version QwQ-32 model When using stream=true to receive a return, You can see that the arguments argument is followed by half a curly brace. But I'm not passing temperature, or I'm just calling a utility function. It's normal again. I don't know why that is. Does it depend on the temperature parameter? My python client-side code： ``` stream = client.chat.completions.create( model=client.models.list().data[0].id, messages=message, # temperature=0, tools=tools, tool_choice='auto', stream=True ) func_call_list = [] for part in stream: delta= part.choices[0].delta if delta.tool_calls: for tcchunk in delta.tool_calls: print(f"tool_calls: {tcchunk}") ``` ### 🐛 Describe the bug My tools calls two utility functions, and calling one doesn't seem to matter. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: arguments in tool_calls bug ### Your current environment vllm 0.7.3 version QwQ-32 model When using stream=true to receive a return, You can see that the arguments argument is followed by half a curly brace. But I'm not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l_calls bug ### Your current environment vllm 0.7.3 version QwQ-32 model When using stream=true to receive a return, You can see that the arguments argument is followed by half a curly brace. But I'm not passing tempera...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
