# vllm-project/vllm#16851: [Bug]: Invalid json schema disconnect the container from GPU without user notice

| 字段 | 值 |
| --- | --- |
| Issue | [#16851](https://github.com/vllm-project/vllm/issues/16851) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Invalid json schema disconnect the container from GPU without user notice

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using an incorrect type in a JSON schema for guided_json, VLLM fails to parse it (and that is right!) but then the container is disconnected from GPUs. The container is still running and **still reports health ok**. I think the container should either crash entirely or prevalidate the schema without risking to loose all the weights from GPUs. When running with VLLM on CLI, it gets killed correctly. On container, it keeps running. Example payload to reproduce the issue (`str` is used instread of `string`. `str` is not a correct type). This payload should be sent to the `/v1/chat/completions` endpoint. ``` json { "model": "mistralai/Mistral-Small-3.1-24B-Instruct-2503", "messages": [ { "role": "user", "content": "Generate a fake weather report in JSON" } ], "temperature": 0, "guided_json": { "$schema": "http://json-schema.org/draft-07/schema#", "type": "object", "properties": { "temperature": { "type": "str" }, "pressure": { "type": "str" }, "wind": { "type": "str" } }, "required": [ "temperature", "wind", "pressure" ], "additionalProperties": false } } ``` ### Before submitting a new issue... - [x] Make sure you already searc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: chat/completions` endpoint. ``` json { "model": "mistralai/Mistral-Small-3.1-24B-Instruct-2503", "messages": [ { "role": "user", "content": "Generate a fake weather report in JSON" } ], "temperature": 0, "guided_json":...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: id json schema disconnect the container from GPU without user notice bug;stale ### Your current environment ### 🐛 Describe the bug When using an incorrect type in a JSON schema for guided_json, VLLM fails to parse it (a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ts killed correctly. On container, it keeps running. Example payload to reproduce the issue (`str` is used instread of `string`. `str` is not a correct type). This payload should be sent to the `/v1/chat/completions` en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rts health ok**. I think the container should either crash entirely or prevalidate the schema without risking to loose all the weights from GPUs. When running with VLLM on CLI, it gets killed correctly. On container, it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
