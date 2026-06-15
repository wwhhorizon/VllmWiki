# vllm-project/vllm#27486: [Bug]: Llama-3.2-1b-instruct prepending extra bos token

| 字段 | 值 |
| --- | --- |
| Issue | [#27486](https://github.com/vllm-project/vllm/issues/27486) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama-3.2-1b-instruct prepending extra bos token

### Issue 正文摘录

### Your current environment ### Your current environment ### 🐛 Describe the bug ### 🐛 Describe the bug I think vLLM is accidentally prepending a bos token because the prompt token ids has an additional begin of text token. Min repro below: ``` def min_repro(): from vllm import LLM, SamplingParams from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct") MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct" prompt = "hello, how are you?" prompt_with_template = tokenizer.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True) llm = LLM(MODEL_NAME, max_model_len=1024, gpu_memory_utilization=0.60) outputs = llm.generate([prompt_with_template], sampling_params=SamplingParams(temperature=0.0, top_p=1.0, logprobs=1)) print(outputs[0].prompt_token_ids) prompt_with_template_tokens = tokenizer.apply_chat_template([{"role": "user", "content": prompt}], tokenize=True, add_generation_prompt=True) print(prompt_with_template_tokens) assert len(outputs[0].prompt_token_ids) == len(prompt_with_template_tokens) if __name__ == "__main__": min_repro() ``` ``` [128000, 128000, 128006, 9125, 128007, 271,...

## 现有链接修复摘要

#27517 fix: double bos token

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt ### 🐛 Describe the bug ### 🐛 Describe the bug I think vLLM is accidentally prepending a bos token because the prompt token ids has an additional begin of text token. Min repro below: ``` def min_repro(): from vllm im...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues and checked the [documentation page](https://github.com/vllm-project/tpu-inference/tree/main/docs), which can answer lots...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama-3.2-1b-instruct prepending extra bos token bug;stale ### Your current environment ### Your current environment ### 🐛 Describe the bug ### 🐛 Describe the bug I think vLLM is accidentally prepending a bos toke
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Llama-3.2-1b-instruct prepending extra bos token bug;stale ### Your current environment ### Your current environment ### 🐛 Describe the bug ### 🐛 Describe the bug I think vLLM is accidentally prepending a bos tok...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash env_dependency #27517 fix: double bos token Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27517](https://github.com/vllm-project/vllm/pull/27517) | closes_keyword | 0.95 | fix: double bos token | Resolves #27486 ## Test Plan ``` def min_repro(): from vllm import LLM, SamplingParams from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pre |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
