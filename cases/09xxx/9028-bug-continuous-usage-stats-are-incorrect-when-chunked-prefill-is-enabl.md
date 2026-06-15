# vllm-project/vllm#9028: [Bug]: Continuous usage stats are incorrect when chunked prefill is enabled 

| 字段 | 值 |
| --- | --- |
| Issue | [#9028](https://github.com/vllm-project/vllm/issues/9028) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Continuous usage stats are incorrect when chunked prefill is enabled 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Start the inference server with: ``` python3 -m vllm.entrypoints.openai.api_server --enable-chunked-prefill ``` Then send a request with a long prompt for a single output token and enable streaming usage stats: ```python import requests import json openai_api_base = "http://localhost:8000/v1" model = requests.get("%s/models" % (openai_api_base)).json()["data"][0]["id"] prompt = "test " * 1_000 request = { "model": model, "prompt": prompt, "max_tokens": 1, "temperature": 0, "stream": True, "stream_options": {"include_usage": True, "continuous_usage_stats": True}, } headers = {"User-Agent": "Test Client"} response = requests.post( "%s/completions" % (openai_api_base), headers=headers, json=request, stream=True, ) finished = False for chunk in response.iter_lines( chunk_size=8192, decode_unicode=False, delimiter=b"\n" ): if chunk and not finished: data = chunk.decode("utf-8").strip().split("data: ")[1] data_parsed = json.loads(data) print(json.dumps(data_parsed, indent=2)) finished = data_parsed["choices"][0]["finish_reason"] is not None ``` produces: ``` { "id": "cmpl-fa1dcd08905f497c9cf514eba80b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pt for a single output token and enable streaming usage stats: ```python import requests import json openai_api_base = "http://localhost:8000/v1" model = requests.get("%s/models" % (openai_api_base)).json()["data"][0]["...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Continuous usage stats are incorrect when chunked prefill is enabled bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Start the inference server with: ``` python3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: o. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ng_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
