# vllm-project/vllm#1538: ValueError: Quantization is not supported for <class 'vllm.model_executor.models.aquila.AquilaForCausalLM'>.

| 字段 | 值 |
| --- | --- |
| Issue | [#1538](https://github.com/vllm-project/vllm/issues/1538) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Quantization is not supported for <class 'vllm.model_executor.models.aquila.AquilaForCausalLM'>.

### Issue 正文摘录

# I tried using the following code to test the AquilaChat2-34B-16K-AWQ model launched by vllm, but it failed. ’‘’ from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", ] prompt_template=f'''System: A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions. Human: {prompts} Assistant: ''' prompts = [prompt_template.format(prompt=prompt) for prompt in prompts] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="TheBloke/AquilaChat2-34B-16K-AWQ", quantization="awq", dtype="auto", trust_remote_code=True) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ‘’‘ # My system environment was built with reference to the official documentation of vllm.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ValueError: Quantization is not supported for <class 'vllm.model_executor.models.aquila.AquilaForCausalLM'>. # I tried using the following code to test the AquilaChat2-34B-16K-AWQ model launched by vllm, but it failed....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: laChat2-34B-16K-AWQ model launched by vllm, but it failed. ’‘’ from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood would a woodchuck ch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ValueError: Quantization is not supported for <class 'vllm.model_executor.models.aquila.AquilaForCausalLM'>. # I tried using the following code to test the AquilaChat2-34B-16K-AWQ model launched by vllm, but it failed....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: models.aquila.AquilaForCausalLM'>. # I tried using the following code to test the AquilaChat2-34B-16K-AWQ model launched by vllm, but it failed. ’‘’ from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
