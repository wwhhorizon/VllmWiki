# vllm-project/vllm#901: Qwen-7b-Chat Test

| 字段 | 值 |
| --- | --- |
| Issue | [#901](https://github.com/vllm-project/vllm/issues/901) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen-7b-Chat Test

### Issue 正文摘录

My test code is as follows： from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM, AutoTokenizer import time model_path="Qwen_chat" model = LLM(model=model_path, tokenizer=model_path,tokenizer_mode='slow',tensor_parallel_size=1,trust_remote_code=True) tokenizer = AutoTokenizer.from_pretrained(model_path, legacy=True, trust_remote_code=True) sampling_params = SamplingParams(temperature=0,max_tokens=400) start=time.time() prompts = ["你好！"] outputs = model.generate(prompts, sampling_params) end = time.time() for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text length = len(generated_text) print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") print(end-start) cost = end-start print(f"{length/cost}tokens/s") The output is all： \n \n \n \n \n \n \n \n \n \n \n \n \n When I set sampling_params = SamplingParams(temperature=0,max_tokens=400,stop=[" ", " ", " "]) The model outputs nothing. how to solve this problem please？ Thanks！

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Qwen-7b-Chat Test My test code is as follows： from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM, AutoTokenizer import time model_path="Qwen_chat" model = LLM(model=model_path, tokenizer=m
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Qwen-7b-Chat Test My test code is as follows： from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM, AutoTokenizer import time model_path="Qwen_chat" model = LLM(model=model_path, tokenizer=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Qwen-7b-Chat Test My test code is as follows： from vllm import LLM, SamplingParams from transformers import AutoModelForCausalLM, AutoTokenizer import time model_path="Qwen_chat" model = LLM(model=model_path, tokenizer=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
