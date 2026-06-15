# vllm-project/vllm#12017: [Usage]: Capability gap between open-source models and GPT-4o

| 字段 | 值 |
| --- | --- |
| Issue | [#12017](https://github.com/vllm-project/vllm/issues/12017) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Capability gap between open-source models and GPT-4o

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm On structured output, OpenAI’s doc gave 4 examples in the Example section in https://platform.openai.com/docs/guides/structured-outputs. Although vLLM supports structured output. It seems that the quality/performance of those models are far behind OpenAI gpt-4o models. For example, for the chain of thought example, the output is ``` Step #0: explanation='Start with the given equation: 8x + 31 = 2.' output='8x + 31 = 2' Step #1: explanation='To isolate the term with x, subtract 31 from both sides of the equation.' output='8x + 31 - 31 = 2 - 31' Step #2: explanation='Simplify both sides: 31 - 31 cancels to 0 on the left side.' output='8x = -29' Step #3: explanation='Divide both sides by 8 to solve for x.' output='x = \\frac{-29}{8}' Answer: x = -\frac{29}{8} ``` However, I test several open-source models (llama3.1-70b and 8b-instruct, qwen2.5-72b-instruct), deployed using vLLM. None of these models can perform (reliably) well on these 4 simple tasks. For chain-of-thought example, Sometimes, they might report validationError: ``` ValidationError: 1 validation error for Ma...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Capability gap between open-source models and GPT-4o usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm On structured output, OpenAI’s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Capability gap between open-source models and GPT-4o usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm On structured output, OpenAI’s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Capability gap between open-source models and GPT-4o usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm On structured output, OpenAI’s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: .' output='x = \\frac{-29}{8}' Answer: x = -\frac{29}{8} ``` However, I test several open-source models (llama3.1-70b and 8b-instruct, qwen2.5-72b-instruct), deployed using vLLM. None of these models can perform (reliab...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
