# vllm-project/vllm#1522: ImportError: cannot import name 'cuda_utils' from partially initialized module 'vllm'

| 字段 | 值 |
| --- | --- |
| Issue | [#1522](https://github.com/vllm-project/vllm/issues/1522) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ImportError: cannot import name 'cuda_utils' from partially initialized module 'vllm'

### Issue 正文摘录

# Here's my test code ' from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", ] prompt_template=f'''System: A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions. Human: {prompt} Assistant: ''' prompts = [prompt_template.format(prompt=prompt) for prompt in prompts] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="TheBloke/AquilaChat2-34B-16K-AWQ", quantization="awq", dtype="auto") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ' # I tried to run and it returned this error for me ImportError: cannot import name 'cuda_utils' from partially initialized module 'vllm' (most likely due to a circular import) (/home/ps/app/edison/vllm/vllm/__init__.py) # environment I followed the docs exactly

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", ] prompt_template=f'''System: A chat between a cur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ImportError: cannot import name 'cuda_utils' from partially initialized module 'vllm' # Here's my test code ' from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas",
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: re=0.8, top_p=0.95) llm = LLM(model="TheBloke/AquilaChat2-34B-16K-AWQ", quantization="awq", dtype="auto") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ImportError: cannot import name 'cuda_utils' from partially initialized module 'vllm' # Here's my test code ' from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ame 'cuda_utils' from partially initialized module 'vllm' # Here's my test code ' from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
