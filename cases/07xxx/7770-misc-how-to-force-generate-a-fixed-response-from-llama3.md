# vllm-project/vllm#7770: [Misc]: How to force generate a fixed response from llama3

| 字段 | 值 |
| --- | --- |
| Issue | [#7770](https://github.com/vllm-project/vllm/issues/7770) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How to force generate a fixed response from llama3

### Issue 正文摘录

### Anything you want to discuss about vllm. I found the llama generate different response for a static input: 1. Running multiple times 2. Batch it with other input This happen even when I set temp=1 top_k=1 and random seed. The generated test usually same at first few tokens, but after them they will be difference. Anyone knows how to force generate a fixed response? ```python import torch from vllm import LLM, SamplingParams torch.random.manual_seed(999) llm = LLM(model='/home/Meta-Llama-3-8B-Instruct') prompts = [ "Hi my name is", "The capital of France is" ] # generate multiple time texts = [] for i in range(10): sampling_params = SamplingParams(temperature=1, top_k=1, max_tokens=100, top_p=1) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text texts.append(generated_text) for text in texts: print(text) # generate with different batch texts = [] for i in range(5): prompts.append(prompts[0]) prompts.append(prompts[1]) sampling_params = SamplingParams(temperature=1, top_k=1, max_tokens=100) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_te...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Misc]: How to force generate a fixed response from llama3 stale ### Anything you want to discuss about vllm. I found the llama generate different response for a static input: 1. Running multiple times 2. Batch it with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: erence. Anyone knows how to force generate a fixed response? ```python import torch from vllm import LLM, SamplingParams torch.random.manual_seed(999) llm = LLM(model='/home/Meta-Llama-3-8B-Instruct') prompts = [ "Hi my...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: How to force generate a fixed response from llama3 stale ### Anything you want to discuss about vllm. I found the llama generate different response for a static input: 1. Running multiple times 2. Batch it with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: is happen even when I set temp=1 top_k=1 and random seed. The generated test usually same at first few tokens, but after them they will be difference. Anyone knows how to force generate a fixed response? ```python impor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
