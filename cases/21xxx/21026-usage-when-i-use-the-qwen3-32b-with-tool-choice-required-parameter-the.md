# vllm-project/vllm#21026: [Usage]: When I use the Qwen3-32B with tool_choice='required' parameter, the tool calling gets stuck in a loop

| 字段 | 值 |
| --- | --- |
| Issue | [#21026](https://github.com/vllm-project/vllm/issues/21026) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: When I use the Qwen3-32B with tool_choice='required' parameter, the tool calling gets stuck in a loop

### Issue 正文摘录

### Your current environment ```text vLLM API server version 0.9.2 vllm serve Qwen/Qwen3-32B --tensor-parallel-size 4 --host 0.0.0.0 --enable-auto-tool-choice --tool-call-parser hermes ``` ### How would you like to use vllm I know this might be a bug, a usage issue, or a model problem. Currently, I'm using LangChain version 0.3.25. When I use bind_tools(tools=[xxx], tool_choice="required"), after calling the tool and returning the result to the LLM, it continues to choose to call the same tool again, resulting in an infinite loop. model_params = { "temperature": 0.1, "seed": 42, "timeout": 3600, } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: When I use the Qwen3-32B with tool_choice='required' parameter, the tool calling gets stuck in a loop usage ### Your current environment ```text vLLM API server version 0.9.2 vllm serve Qwen/Qwen3-32B --tensor-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ck in a loop usage ### Your current environment ```text vLLM API server version 0.9.2 vllm serve Qwen/Qwen3-32B --tensor-parallel-size 4 --host 0.0.0.0 --enable-auto-tool-choice --tool-call-parser hermes ``` ### How wou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
