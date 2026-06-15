# vllm-project/vllm#9082: [Bug]: vLLM MQLLMEngine Timeout - Json Schema 

| 字段 | 值 |
| --- | --- |
| Issue | [#9082](https://github.com/vllm-project/vllm/issues/9082) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM MQLLMEngine Timeout - Json Schema 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM crashes without traceback. I am using two guided json templates to generate synthetic data. No errors arise from template 1.... but when I use template 2 with concurrent workers, vLLM crashes like below. A few successful generations may result, but after a couple more requests it fails. Keeping GPU KV cache usage below 15%, I still get this error so it does not appear to be related to load. Here is the json schema, that is causing problems: ``` { "properties": { "rating": { "description": "Rating", "title": "Rating", "type": "integer" }, "rational": { "description": "Rational for rating", "maxLength": 250, "title": "Rational", "type": "string" } }, "required": [ "rating", "rational" ], "title": "QuestionObjective", "type": "object" } ``` Model: qwen2.5-7b-instr vLLM==0.6.2 Engine Args: --max-model-len 8192 --gpu-memory-utilization 0.95 ``` DEBUG 10-04 20:05:16 client.py:148] Heartbeat successful. DEBUG 10-04 20:05:19 client.py:164] Waiting for output from MQLLMEngine. 127.0.0.1 - - [04/Oct/2024 20:05:20] "GET /health HTTP/1.1" 200 - INFO: 10.250.55.3:60232 - "GET /api/v1/pipeline/health HTTP/1.1" 200 OK ERROR 10-04 20:05:26...

## 现有链接修复摘要

#9818 [Bugfix][core] replace heartbeat with pid check

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;operator;sampling build_error;crash;nan_inf e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: below. A few successful generations may result, but after a couple more requests it fails. Keeping GPU KV cache usage below 15%, I still get this error so it does not appear to be related to load. Here is the json schem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: al" ], "title": "QuestionObjective", "type": "object" } ``` Model: qwen2.5-7b-instr vLLM==0.6.2 Engine Args: --max-model-len 8192 --gpu-memory-utilization 0.95 ``` DEBUG 10-04 20:05:16 client.py:148] Heartbeat successfu...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ions may result, but after a couple more requests it fails. Keeping GPU KV cache usage below 15%, I still get this error so it does not appear to be related to load. Here is the json schema, that is causing problems: ``...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9818](https://github.com/vllm-project/vllm/pull/9818) | closes_keyword | 0.95 | [Bugfix][core] replace heartbeat with pid check | FIX #9082 FIX #9238 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
