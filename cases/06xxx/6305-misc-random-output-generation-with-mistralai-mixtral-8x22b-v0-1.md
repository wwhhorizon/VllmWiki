# vllm-project/vllm#6305: [Misc]: Random Output Generation with mistralai/Mixtral-8x22B-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#6305](https://github.com/vllm-project/vllm/issues/6305) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Random Output Generation with mistralai/Mixtral-8x22B-v0.1

### Issue 正文摘录

I am trying to run inference with mistralai/Mixtral-8x22B-v0.1 model, but it is generating random output with an 8-way tensor parallel setup. Below are the details of the configuration and I think there may be an issue with the tokenizer. ```py from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="mistralai/Mixtral-8x22B-v0.1", tensor_parallel_size=8, enforce_eager=True, load_format="auto") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0.1 stale I am trying to run inference with mistralai/Mixtral-8x22B-v0.1 model, but it is generating random output with an 8-way tensor parallel setup. Below are the details of the configuration and I think there may be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: Random Output Generation with mistralai/Mixtral-8x22B-v0.1 stale I am trying to run inference with mistralai/Mixtral-8x22B-v0.1 model, but it is generating random output with an 8-way tensor parallel setup. Belo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n and I think there may be an issue with the tokenizer. ```py from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
