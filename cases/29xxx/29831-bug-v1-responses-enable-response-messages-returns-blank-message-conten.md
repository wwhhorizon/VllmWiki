# vllm-project/vllm#29831: [Bug]: v1/responses `enable_response_messages` returns blank message `content`

| 字段 | 值 |
| --- | --- |
| Issue | [#29831](https://github.com/vllm-project/vllm/issues/29831) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: v1/responses `enable_response_messages` returns blank message `content`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `extra_body={"enable_response_messages": True}` is set, vLLM returns `input_messages` and `output_messages`, but the `content` of each message is `[{}]`- a list containing an empty dictionary. ``` {'author': {'name': None, 'role': 'system'}, 'channel': None, 'content': [{}], 'content_type': None, ...} ``` A prior pull request (vLLM #26185) tried to solve this issue ([openai/harmony#78](https://github.com/openai/harmony/issues/78)) but did not fully address the `vllm serve` use case. Specifically, #26185 specified `when_used="json"` in the fix, which would not be triggered when the `vllm serve` FastAPI path [invokes](https://github.com/vllm-project/vllm/blob/a0003b56b0b822c52bb0f3035c164370a802e6f5/vllm/entrypoints/openai/api_server.py#L527-L529) `model_dump()` on the response object. Tests [added](https://github.com/vllm-project/vllm/pull/26185/files#diff-0027d7c5f28f44ef829e676d79b35d4c2724e116ed99ce28b37ee54fc3f58d94) in #26185 did not go through the FastAPI logic, and hence did not trigger the `model_dump()` in CI. To highlight this error, consider adding the following validations to the existing unit test `test_output_me...

## 现有链接修复摘要

#29830 Added regression test for openai/harmony/issues/78

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mony/issues/78)) but did not fully address the `vllm serve` use case. Specifically, #26185 specified `when_used="json"` in the fix, which would not be triggered when the `vllm serve` FastAPI path [invokes](https://githu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: responses `enable_response_messages` returns blank message `content` bug;stale ### Your current environment ### 🐛 Describe the bug When `extra_body={"enable_response_messages": True}` is set, vLLM returns `input_message...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ted_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;kernel;moe;operator;quantization;sampling;triton build_err...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;kernel;moe;...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29830](https://github.com/vllm-project/vllm/pull/29830) | mentioned | 0.45 | Added regression test for openai/harmony/issues/78 | armony.py`. see #29830 for full diff of the proposed test changes. ~~#29830~~ (edit: #27377) would fix this issue. <details><summary>full log (<code>pytest -sv ...</code>)</summar… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
