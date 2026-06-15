# vllm-project/vllm#19493: [Bug]: Corrupted output when using JSON structured response (v0.9.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#19493](https://github.com/vllm-project/vllm/issues/19493) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Corrupted output when using JSON structured response (v0.9.1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm seeing a lot of the following errors: ``` [backend_xgrammar.py:160] Failed to advance FSM for request chatcmpl-XXX for tokens 500. Please file an issue. ``` This happens when specifying the `response_format` to be of `{'type': 'json_object'}`, but only when multiple requests are received. See bellow to reproduce. #### Reproduce ``` pip install vllm==0.9.1 vllm serve mediainbox/cogito-14b-gptq-q4 \ --port=8098 \ --host=0.0.0.0 \ --max-model-len 4K \ --disable-fastapi-docs ``` Now run the following script: ```py import concurrent.futures import requests OPTIONS = {"temperature": 0.0, "max_tokens": 256, "response_format": {"type": "json_object"}} PROMPT = [ {"role": "system", "content": "You are a Named Entity Recognition system. Output should be JSON in a single line."}, {"role": "user", "content": "Extract entities from this sentence: 'Hi Robert did you go to TacoBox?'"}, ] def call_vllm(): resp = requests.post( "http://localhost:8098/v1/chat/completions", json={ "model": "mediainbox/cogito-14b-gptq-q4", "messages": PROMPT, **OPTIONS, }, timeout=10, ) return resp.json()["choices"][0]["message"]["content"] if __name__ == "__mai...

## 现有链接修复摘要

#19565 [V1] Resolve failed concurrent structred output requests

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cmpl-XXX for tokens 500. Please file an issue. ``` This happens when specifying the `response_format` to be of `{'type': 'json_object'}`, but only when multiple requests are received. See bellow to reproduce. #### Repro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the following errors: ``` [backend_xgrammar.py:160] Failed to advance FSM for request chatcmpl-XXX for tokens 500. Please file an issue. ``` This happens when specifying the `response_format` to be of `{'type': 'json_ob...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ### 🐛 Describe the bug I'm seeing a lot of the following errors: ``` [backend_xgrammar.py:160] Failed to advance FSM for request chatcmpl-XXX for tokens 500. Please file an issue. ``` This happens when specifying the `r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 0. Please file an issue. ``` This happens when specifying the `response_format` to be of `{'type': 'json_object'}`, but only when multiple requests are received. See bellow to reproduce. #### Reproduce ``` pip install v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: llowing errors: ``` [backend_xgrammar.py:160] Failed to advance FSM for request chatcmpl-XXX for tokens 500. Please file an issue. ``` This happens when specifying the `response_format` to be of `{'type': 'json_object'}...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19565](https://github.com/vllm-project/vllm/pull/19565) | closes_keyword | 0.95 | [V1] Resolve failed concurrent structred output requests | Closes #19493 Closes #18376 Related to #18780 Several people have noticed errors when using both the `xgrammar` and `guidance` backends where we would start generating invalid tok |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
