# vllm-project/vllm#557: gai error: -2 - Name or service not known

| 字段 | 值 |
| --- | --- |
| Issue | [#557](https://github.com/vllm-project/vllm/issues/557) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> gai error: -2 - Name or service not known

### Issue 正文摘录

When I deploy a gpt2 model on 4 GPUs with vllm, I got this error: ![image](https://github.com/vllm-project/vllm/assets/63448337/36a91f83-201a-47dc-916d-9aaa2ae028e4) here is my test code: ```python from vllm import LLM, SamplingParams prompts = [ "San Franciso is a" ] llm = LLM(model="gpt2", tensor_parallel_size=2, disable_log_stats=False) outputs = llm.generate(prompts) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` so how can i solve this?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: -201a-47dc-916d-9aaa2ae028e4) here is my test code: ```python from vllm import LLM, SamplingParams prompts = [ "San Franciso is a" ] llm = LLM(model="gpt2", tensor_parallel_size=2, disable_log_stats=False) outputs = llm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: " ] llm = LLM(model="gpt2", tensor_parallel_size=2, disable_log_stats=False) outputs = llm.generate(prompts) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text pri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gai error: -2 - Name or service not known When I deploy a gpt2 model on 4 GPUs with vllm, I got this error: ![image](https://github.com/vllm-project/vllm/assets/63448337/36a91f83-201a-47dc-916d-9aaa2ae028e4) here is my...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t/vllm/assets/63448337/36a91f83-201a-47dc-916d-9aaa2ae028e4) here is my test code: ```python from vllm import LLM, SamplingParams prompts = [ "San Franciso is a" ] llm = LLM(model="gpt2", tensor_parallel_size=2, disable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
