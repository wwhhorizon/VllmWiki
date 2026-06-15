# vllm-project/vllm#1247: Quantization is not supported for <class 'vllm.model_executor.models.mistral.MistralForCausalLM'>

| 字段 | 值 |
| --- | --- |
| Issue | [#1247](https://github.com/vllm-project/vllm/issues/1247) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Quantization is not supported for <class 'vllm.model_executor.models.mistral.MistralForCausalLM'>

### Issue 正文摘录

Hi, Thanks for this great repo! I tried to run inference on AWQ `casperhansen/mistral-7b-instruct-v0.1-awq` model: ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="casperhansen/mistral-7b-instruct-v0.1-awq", quantization="awq", dtype="half") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` And got the following error: ``` Downloading (…)lve/main/config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 716/716 [00:00 llm = LLM(model="casperhansen/mistral-7b-instruct-v0.1-awq", quantization="awq", dtype="half") File "/home/matthieu/anaconda3/envs/vllm_gpu118/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 89, in __init__ self.llm_engine = LLMEngine.from_eng...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Quantization is not supported for <class 'vllm.model_executor.models.mistral.MistralForCausalLM'> Hi, Thanks for this great repo! I tried to run inference on AWQ `casperhansen/mistral-7b-instruct-v0.1-awq` model: ``` f
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Quantization is not supported for <class 'vllm.model_executor.models.mistral.MistralForCausalLM'> Hi, Thanks for this great repo! I tried to run inference on AWQ `casperhansen/mistral-7b-instruct-v0.1-awq` model: ``` fr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on AWQ `casperhansen/mistral-7b-instruct-v0.1-awq` model: ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
