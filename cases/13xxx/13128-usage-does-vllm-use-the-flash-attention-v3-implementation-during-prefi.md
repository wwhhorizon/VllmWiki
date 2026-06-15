# vllm-project/vllm#13128: [Usage]: Does vllm use the Flash Attention v3 implementation during prefill and decoding? and How？

| 字段 | 值 |
| --- | --- |
| Issue | [#13128](https://github.com/vllm-project/vllm/issues/13128) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vllm use the Flash Attention v3 implementation during prefill and decoding? and How？

### Issue 正文摘录

### Your current environment python3.10.12 torch 2.5.1 vllm 0.7.2 H800 GPU ```text my code from vllm import LLM, SamplingParams from transformers import AutoTokenizer import torch import time import sys model_path="./Qwen1.5-4B" tokenizer = AutoTokenizer.from_pretrained(model_path) prompts = [ "The future of AI is", ] test_len=6000 output_len = 52 prompt_token_ids=tokenizer.encode(prompts[0]) print(len(prompt_token_ids)) prompt_token_ids=prompt_token_ids*(test_len // len(prompt_token_ids)) print(len(prompt_token_ids)) sampling_params = SamplingParams(top_k=1, temperature=1, top_p=1, repetition_penalty=1, max_tokens=output_len) llm = LLM( model=model_path, tensor_parallel_size=1, ) print('warm up done') for i in range(10): outputs = llm.generate(prompts=None, prompt_token_ids=[prompt_token_ids], sampling_params=sampling_params) ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m transformers import AutoTokenizer import torch import time import sys model_path="./Qwen1.5-4B" tokenizer = AutoTokenizer.from_pretrained(model_path) prompts = [ "The future of AI is", ] test_len=6000 output_len = 52...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: Does vllm use the Flash Attention v3 implementation during prefill and decoding? and How？ usage ### Your current environment python3.10.12 torch 2.5.1 vllm 0.7.2 H800 GPU ```text my code from vllm import LLM, S...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: on3.10.12 torch 2.5.1 vllm 0.7.2 H800 GPU ```text my code from vllm import LLM, SamplingParams from transformers import AutoTokenizer import torch import time import sys model_path="./Qwen1.5-4B" tokenizer = AutoTokeniz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Does vllm use the Flash Attention v3 implementation during prefill and decoding? and How？ usage ### Your current environment python3.10.12 torch 2.5.1 vllm 0.7.2 H800 GPU ```text my code from vllm import LLM, S...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: er.from_pretrained(model_path) prompts = [ "The future of AI is", ] test_len=6000 output_len = 52 prompt_token_ids=tokenizer.encode(prompts[0]) print(len(prompt_token_ids)) prompt_token_ids=prompt_token_ids*(test_len //...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
