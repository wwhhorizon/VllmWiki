# vllm-project/vllm#27390: [Bug]: Inconsistent `finish_reason` and special token handling between V0 and V1 engines

| 字段 | 值 |
| --- | --- |
| Issue | [#27390](https://github.com/vllm-project/vllm/issues/27390) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent `finish_reason` and special token handling between V0 and V1 engines

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The vLLM V0 and V1 engines produce inconsistent `finish_reason` values when generating text with identical parameters. This occurs because V0 engine checks for EOS tokens first during stop determination, while V1 engine prioritizes generation length checks. Additionally, V1 engine incorrectly displays special tokens in output even when properly configured in `tokenizer_config.json`. ## `finish_reason` Inconsistency ### Example 1. Qwen-3.4B-Instruct-2507 When running the following script with both V0 and V1, you can confirm that the finish_reason differs. ```python:test-qwen.py from transformers import AutoTokenizer from vllm import LLM, SamplingParams model = "Qwen/Qwen3-4B-Instruct-2507" tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True) chat = [ {"role": "user", "content": "Hello?"}, ] prompt = tokenizer.apply_chat_template(chat, tokenize=False) llm = LLM(model=model, trust_remote_code=True) outputs = llm.generate( prompt, sampling_params=SamplingParams(temperature=0.0, max_tokens=16), ) print(outputs[0].outputs[0].text) print(outputs[0].outputs[0].token_ids) print(outputs[0].outputs[0].finish_reason) outp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Inconsistent `finish_reason` and special token handling between V0 and V1 engines bug ### Your current environment ### 🐛 Describe the bug The vLLM V0 and V1 engines produce inconsistent `finish_reason` values whe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: engine incorrectly displays special tokens in output even when properly configured in `tokenizer_config.json`. ## `finish_reason` Inconsistency ### Example 1. Qwen-3.4B-Instruct-2507 When running the following script wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nish_reason) ``` ```bash % VLLM_USE_V1=0 python test-qwen.py ... Adding requests: 100%|██████████████████████████████████| 1/1 [00:00 dataset translation input lang=English Hello, how are you today? output lang=Japanese...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
