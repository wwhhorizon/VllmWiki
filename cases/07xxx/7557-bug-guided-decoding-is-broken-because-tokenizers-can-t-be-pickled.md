# vllm-project/vllm#7557: [Bug]: Guided decoding is broken because tokenizers can't be pickled

| 字段 | 值 |
| --- | --- |
| Issue | [#7557](https://github.com/vllm-project/vllm/issues/7557) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Guided decoding is broken because tokenizers can't be pickled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If I run a small model like this `python -m vllm.entrypoints.openai.api_server --model gpt2` and call it like this ``` curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "gpt2", "prompt": ["An example of a json document: ", "Another example of a json document: "], "max_tokens": 100, "temperature": 0, "guided_decoding_backend": "outlines", "response_format": {"type":"json_object"} }' ``` I get the following error in the server log: ``` Traceback (most recent call last): File "/home/mbayser/.pyenv/versions/3.11.8/lib/python3.11/multiprocessing/queues.py", line 244, in _feed obj = _ForkingPickler.dumps(obj) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/mbayser/.pyenv/versions/3.11.8/lib/python3.11/multiprocessing/reduction.py", line 51, in dumps cls(buf, protocol).dump(obj) AttributeError: Can't pickle local object 'get_cached_tokenizer. .CachedTokenizer' ``` I've tried to disable frontend multiprocessing, but that only changes the place where the error happens: ``` Traceback (most recent call last): File "/home/mbayser/.pyenv/versions/3.11.8/lib/python3.11/multiprocessing/queues.py", line 244, in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: log: ``` Traceback (most recent call last): File "/home/mbayser/.pyenv/versions/3.11.8/lib/python3.11/multiprocessing/queues.py", line 244, in _feed obj = _ForkingPickler.dumps(obj) ^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/hom...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ding is broken because tokenizers can't be pickled bug;structured-output;stale ### Your current environment ### 🐛 Describe the bug If I run a small model like this `python -m vllm.entrypoints.openai.api_server --model g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: t: "], "max_tokens": 100, "temperature": 0, "guided_decoding_backend": "outlines", "response_format": {"type":"json_object"} }' ``` I get the following error in the server log: ``` Traceback (most recent call last): Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tale ### Your current environment ### 🐛 Describe the bug If I run a small model like this `python -m vllm.entrypoints.openai.api_server --model gpt2` and call it like this ``` curl http://localhost:8000/v1/completions -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## Your current environment ### 🐛 Describe the bug If I run a small model like this `python -m vllm.entrypoints.openai.api_server --model gpt2` and call it like this ``` curl http://localhost:8000/v1/completions -H "Con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
