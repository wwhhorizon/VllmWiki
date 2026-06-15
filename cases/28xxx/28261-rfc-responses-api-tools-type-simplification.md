# vllm-project/vllm#28261: [RFC]: Responses API Tools Type Simplification

| 字段 | 值 |
| --- | --- |
| Issue | [#28261](https://github.com/vllm-project/vllm/issues/28261) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Responses API Tools Type Simplification

### Issue 正文摘录

### Motivation. The current vLLM implementation of the Responses API has a [large amount of branching logic](https://github.com/vllm-project/vllm/blob/4bf56c79cc252d285d0cb4f5edf323f02af735ca/vllm/entrypoints/openai/serving_responses.py#L1814) to support OpenAI types for their "built-in" tools. These were added during the release of gpt-oss in order to create an implementation similar to OpenAI's using their "[demo tools](https://github.com/openai/gpt-oss/blob/48db88d8e29f48493fe75f084a8c9bd900a2b92f/gpt_oss/tools/simple_browser/simple_browser_tool.py#L319)" While these types and tools are nice for demo purposes, they are: - Incomplete - The browser tool is missing arguments that the model is trained to add, causing errors - Browser tool and web search tool are actually slightly different tools! - The output types are lossy - The Actions for web search do not represent what the model output - [You are expected to convert cursor + state into URL](https://github.com/openai/openai-python/blob/6574bcd612771186995074846253caa0ff1ba517/src/openai/types/responses/response_function_web_search.py#L35) which cannot be reversed - Specific to OpenAI's implementation - You can only configure t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: pes for their "built-in" tools. These were added during the release of gpt-oss in order to create an implementation similar to OpenAI's using their "[demo tools](https://github.com/openai/gpt-oss/blob/48db88d8e29f48493f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Responses API Tools Type Simplification RFC;stale ### Motivation. The current vLLM implementation of the Responses API has a [large amount of branching logic](https://github.com/vllm-project/vllm/blob/4bf56c79cc2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: onses/response_function_web_search.py#L35) which cannot be reversed - Specific to OpenAI's implementation - You can only configure the tool using the [fields OpenAI provides](https://github.com/openai/openai-python/blob...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t the model is trained to add, causing errors - Browser tool and web search tool are actually slightly different tools! - The output types are lossy - The Actions for web search do not represent what the model output -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
