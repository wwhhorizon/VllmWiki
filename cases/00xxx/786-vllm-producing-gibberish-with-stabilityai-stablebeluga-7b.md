# vllm-project/vllm#786: vllm producing gibberish with stabilityai/StableBeluga-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#786](https://github.com/vllm-project/vllm/issues/786) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm producing gibberish with stabilityai/StableBeluga-7B

### Issue 正文摘录

Hey there, I'm using vllm to serve Llama 2 models in production and for most of them it's working well! However, when running the Llama 2 derivative [StableBeluga-7B](https://huggingface.co/stabilityai/StableBeluga-7B) vllm produces gibberish. I've included a minimal repro below: ### Calling the model with `transformers` directly works as expected ```python %pip install transformers sentencepiece accelerate import torch from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline prompt = f"### User: count to 5\n\n### Assistant:\n" tokenizer = AutoTokenizer.from_pretrained("stabilityai/StableBeluga-7B") model = AutoModelForCausalLM.from_pretrained("stabilityai/StableBeluga-7B") inputs = tokenizer(prompt, return_tensors="pt") output = model.generate(**inputs, max_new_tokens=20) print(tokenizer.decode(output[0], skip_special_tokens=True)[len(prompt):]) # Prints "1, 2, 3, 4, 5" ``` ### Calling the model with `vllm` returns gibberish ```python from vllm import LLM, SamplingParams prompt = f"### User: count to 5\n\n### Assistant:\n" llm = LLM(model="stabilityai/StableBeluga-7B") sampling_params = SamplingParams() outputs = llm.generate([prompt], sampling_params) print(outputs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vllm producing gibberish with stabilityai/StableBeluga-7B Hey there, I'm using vllm to serve Llama 2 models in production and for most of them it's working well! However, when running the Llama 2 derivative [StableBelug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ish with stabilityai/StableBeluga-7B Hey there, I'm using vllm to serve Llama 2 models in production and for most of them it's working well! However, when running the Llama 2 derivative [StableBeluga-7B](https://hugging...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ") output = model.generate(**inputs, max_new_tokens=20) print(tokenizer.decode(output[0], skip_special_tokens=True)[len(prompt):]) # Prints "1, 2, 3, 4, 5" ``` ### Calling the model with `vllm` returns gibberish ```pyth...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: m beskrevs PelΤ" ``` Any idea what's going wrong? I've tried both the latest released vllm (0.1.3) and the `main` branch.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
