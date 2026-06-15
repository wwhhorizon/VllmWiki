# vllm-project/vllm#21846: [Bug]: vLLM 0.10.0 breaks skip_tokenizer_init=True

| 字段 | 值 |
| --- | --- |
| Issue | [#21846](https://github.com/vllm-project/vllm/issues/21846) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.10.0 breaks skip_tokenizer_init=True

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Repro: ```python import vllm from transformers import AutoTokenizer model_name = "Qwen/Qwen2.5-1.5B" llm = vllm.LLM(model_name, skip_tokenizer_init=True) tokenizer = AutoTokenizer.from_pretrained(model_name) input_ids = tokenizer.encode("test") print(llm.generate([{"prompt_token_ids": input_ids}])) ``` Error log: ```bash Adding requests: 0%| | 0/1 [00:00 print(llm.generate([{"prompt_token_ids": input_ids}])) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/scratch.yukih_gpu/depot/reinforcer/.venv/lib/python3.12/site-packages/vllm/utils/__init__.py", line 1514, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/home/scratch.yukih_gpu/depot/reinforcer/.venv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 495, in generate self._validate_and_add_requests( File "/home/scratch.yukih_gpu/depot/reinforcer/.venv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 1629, in _validate_and_add_requests self._add_request( File "/home/scratch.yukih_gpu/depot/reinforcer/.venv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 1647, in _add_request self.llm_engine.add_request( File "/home/scratc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ## Your current environment ### 🐛 Describe the bug Repro: ```python import vllm from transformers import AutoTokenizer model_name = "Qwen/Qwen2.5-1.5B" llm = vllm.LLM(model_name, skip_tokenizer_init=True) tokenizer = Au...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ug Repro: ```python import vllm from transformers import AutoTokenizer model_name = "Qwen/Qwen2.5-1.5B" llm = vllm.LLM(model_name, skip_tokenizer_init=True) tokenizer = AutoTokenizer.from_pretrained(model_name) input_id...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: erate([{"prompt_token_ids": input_ids}])) ``` Error log: ```bash Adding requests: 0%| | 0/1 [00:00 print(llm.generate([{"prompt_token_ids": input_ids}])) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
