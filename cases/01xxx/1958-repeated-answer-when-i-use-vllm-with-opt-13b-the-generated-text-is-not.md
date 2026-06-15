# vllm-project/vllm#1958: Repeated answer: When I use vllm with opt-13b, the generated text is not end until the max length, with the repeated answer

| 字段 | 值 |
| --- | --- |
| Issue | [#1958](https://github.com/vllm-project/vllm/issues/1958) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Repeated answer: When I use vllm with opt-13b, the generated text is not end until the max length, with the repeated answer

### Issue 正文摘录

hi, I use vllm in greedy SamplingType, I meet the repeated answer: `sampling_params = SamplingParams(temperature=0, top_p=1, max_tokens=2048)` `from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Give three tips for staying healthy.", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0, top_p=1, max_tokens=2048) # Create an LLM. llm = LLM(model="/workspace/opt-13b/", tensor_parallel_size=4) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}", len(output.out puts[0].token_ids))` The answer is follow, the same text is repreated, also to other prompts. ![截屏2023-12-07 下午3 59 51](https://github.com/vllm-project/vllm/assets/8213143/dd316200-1c6b-420e-abbf-2fd07dbd8283) So is there any way to solve this problem? Thanks.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s = SamplingParams(temperature=0, top_p=1, max_tokens=2048)` `from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Give three tips for staying healthy.", ] # Create a sampling params object. sampling_para...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ams(temperature=0, top_p=1, max_tokens=2048) # Create an LLM. llm = LLM(model="/workspace/opt-13b/", tensor_parallel_size=4) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
