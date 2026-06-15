# vllm-project/vllm#7787: [Bug]: Phi-3-small-128k-instruct on 1 A100 GPUs - Assertion error: Does not support prefix-enabled attention.

| 字段 | 值 |
| --- | --- |
| Issue | [#7787](https://github.com/vllm-project/vllm/issues/7787) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Phi-3-small-128k-instruct on 1 A100 GPUs - Assertion error: Does not support prefix-enabled attention.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. start the vLLM server: `python -m vllm.entrypoints.openai.api_server --model 'microsoft/Phi-3-small-128k-instruct' --dtype auto --trust-remote-code` 2. from another terminal, send a request to the server: `curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{"model": "microsoft/Phi-3-small-128k-instruct","prompt": "Who is the president of the united states?", "max_tokens": 1000,"temperature": 0.2,"top_p": 0.95,"echo": true}'` 3. Server crash with the assertion error below: ``` INFO 08-22 09:36:23 logger.py:36] Received request cmpl-7836154054e34e87a357c3c0f93d50b1-0: prompt: 'Who is the president of the united states?', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.2, top_p=0.95, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 0 GPUs - Assertion error: Does not support prefix-enabled attention. bug;stale ### Your current environment ### 🐛 Describe the bug 1. start the vLLM server: `python -m vllm.entrypoints.openai.api_server --model 'microso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Phi-3-small-128k-instruct on 1 A100 GPUs - Assertion error: Does not support prefix-enabled attention. bug;stale ### Your current environment ### 🐛 Describe the bug 1. start the vLLM server: `python -m vllm.entry...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _tokens=1000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [15546, 374, 279, 4872, 315, 279, 29292, 541...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ature=0.2, top_p=0.95, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1000, mi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 36:23 async_llm_engine.py:65] File "/home/aiscuser/vllm/vllm/attention/backends/blocksparse_attn.py", line 404, in forward ERROR 08-22 09:36:23 async_llm_engine.py:65] or prefill_meta.block_tables.numel() == 0, \ ERROR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
