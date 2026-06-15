# vllm-project/vllm#1213: Bugged interference on Vicuna 7B GPTQ 16k

| 字段 | 值 |
| --- | --- |
| Issue | [#1213](https://github.com/vllm-project/vllm/issues/1213) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bugged interference on Vicuna 7B GPTQ 16k

### Issue 正文摘录

I was playing simple example: ``` from vllm.entrypoints.llm import LLM from vllm.sampling_params import SamplingParams MODEL_NAME = "TheBloke/vicuna-7B-v1.5-16k-GPTQ" llm = LLM(model=MODEL_NAME, quantization="gptq", gpu_memory_utilization=0.5) sampling_params = SamplingParams( max_tokens=600, top_p=0.95, temperature=0.7, presence_penalty=0.5, frequency_penalty=0.5, ) outputs = llm.generate( [ """A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\n\n USER: Write Python script converting RGB image to grayscale.\n ASSISTANT: """, ], sampling_params=sampling_params, ) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r},\nGenerated text: {generated_text!r}") print() ``` and I received random output. Either random character or few words looped endlessly. When I switched backed to 4k model, everything was fine. I'm not sure if its related to GPTQ or 16k vicuna in general. I'm not able to check unquantized or AWQ quantized model as it doesn't fit on my GPU during inference. Relevant to GPTQ: https://github.com/vllm-project/vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 7B GPTQ 16k I was playing simple example: ``` from vllm.entrypoints.llm import LLM from vllm.sampling_params import SamplingParams MODEL_NAME = "TheBloke/vicuna-7B-v1.5-16k-GPTQ" llm = LLM(model=MODEL_NAME, quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: L_NAME = "TheBloke/vicuna-7B-v1.5-16k-GPTQ" llm = LLM(model=MODEL_NAME, quantization="gptq", gpu_memory_utilization=0.5) sampling_params = SamplingParams( max_tokens=600, top_p=0.95, temperature=0.7, presence_penalty=0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rypoints.llm import LLM from vllm.sampling_params import SamplingParams MODEL_NAME = "TheBloke/vicuna-7B-v1.5-16k-GPTQ" llm = LLM(model=MODEL_NAME, quantization="gptq", gpu_memory_utilization=0.5) sampling_params = Samp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
