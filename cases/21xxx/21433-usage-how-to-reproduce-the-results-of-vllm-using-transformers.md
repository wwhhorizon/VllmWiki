# vllm-project/vllm#21433: [Usage]: How to reproduce the results of `vllm` using `transformers`

| 字段 | 值 |
| --- | --- |
| Issue | [#21433](https://github.com/vllm-project/vllm/issues/21433) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to reproduce the results of `vllm` using `transformers`

### Issue 正文摘录

### Your current environment ### How would you like to use vllm Hi there, I am using `vllm` for text generation, and I aim to reproduce the results of `vllm` using `transformers` library (.generate method) under the same infrastructure (environment) so that I can use `transformers` to handle some situations that I have to use `transformers` for generation (e.g., disturb the output logits). However, I can not reproduce the results exactly when using the same model under the same infrastructure. Below are my code snippets. Is it possible to find a way to reproduce the results? ```python # vllm-test.py import sys import torch.distributed as dist from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_name = "Qwen/Qwen2.5-0.5B-Instruct" tokenizer = AutoTokenizer.from_pretrained(model_name) chat_prompts = [ [{"role": "user", "content": "Hello, how are you?"}], [{"role": "user", "content": "Please tell me a joke."}], [{"role": "user", "content": "Explain LLM."}], ] prompts = [tokenizer.apply_chat_template( p, tokenize=False) for p in chat_prompts] llm = LLM( model=model_name, dtype="bfloat16", gpu_memory_utilization=0.95, enforce_eager=True ) sampling_params =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: sible to find a way to reproduce the results? ```python # vllm-test.py import sys import torch.distributed as dist from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_name = "Qwen/Qwen2.5-0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nize=False) for p in chat_prompts] llm = LLM( model=model_name, dtype="bfloat16", gpu_memory_utilization=0.95, enforce_eager=True ) sampling_params = SamplingParams( max_tokens=100, skip_special_tokens=True, temperature...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: sage]: How to reproduce the results of `vllm` using `transformers` usage;stale ### Your current environment ### How would you like to use vllm Hi there, I am using `vllm` for text generation, and I aim to reproduce the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ). However, I can not reproduce the results exactly when using the same model under the same infrastructure. Below are my code snippets. Is it possible to find a way to reproduce the results? ```python # vllm-test.py im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
