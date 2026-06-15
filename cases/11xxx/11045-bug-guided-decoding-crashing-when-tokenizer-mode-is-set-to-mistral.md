# vllm-project/vllm#11045: [Bug]: Guided decoding crashing when tokenizer_mode is set to mistral

| 字段 | 值 |
| --- | --- |
| Issue | [#11045](https://github.com/vllm-project/vllm/issues/11045) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Guided decoding crashing when tokenizer_mode is set to mistral

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Recent code on mistral and set xgrammar does not work when users set `--tokenizer-mode=mistral` This script below can repro the crash ```py from openai import OpenAI from vllm.sampling_params import GuidedDecodingParams, SamplingParams import json from vllm import LLM, SamplingParams BACKEND='outlines' # OR # BACKEND=NONE # to use xgrammar MODEL_NAME='mistralai/Mistral-7B-Instruct-v0.3' sample_json_schema = { "type": "object", "properties": { "name": { "type": "string" }, "age": { "type": "integer" }, "skills": { "type": "array", "items": { "type": "string", "maxLength": 10 }, "minItems": 3 }, "work_history": { "type": "array", "items": { "type": "object", "properties": { "company": { "type": "string" }, "duration": { "type": "number" }, "position": { "type": "string" } }, "required": ["company", "position"] } } }, "required": ["name", "age", "skills", "work_history"] } messages = [{ "role": "system", "content": "you are a helpful assistant" }, { "role": "user", "content": f"Give an example JSON for an employee profile that " f"fits this schema: {sample_json_schema}" }] prompts = [ json.dumps(m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mode=mistral` This script below can repro the crash ```py from openai import OpenAI from vllm.sampling_params import GuidedDecodingParams, SamplingParams import json from vllm import LLM, SamplingParams BACKEND='outline...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ^^^^^^^^^^^^^ File "/opt/vllm/lib64/python3.12/site-packages/outlines/fsm/guide.py", line 145, in __init__ ) = create_states_mapping(regex_string, tokenizer) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e-packages/vllm/engine/multiprocessing/client.py", line 582, in _process_request params = await \ ^^^^^^^ File "/opt/vllm/lib64/python3.12/site-packages/vllm/engine/async_llm_engine.py", line 539, in build_guided_decodi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: arams, SamplingParams import json from vllm import LLM, SamplingParams BACKEND='outlines' # OR # BACKEND=NONE # to use xgrammar MODEL_NAME='mistralai/Mistral-7B-Instruct-v0.3' sample_json_schema = { "type": "object", "p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: okenizer_mode is set to mistral bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Recent code on mistral and set xgrammar does not work when users set `--tokenizer-mode=mistral`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
