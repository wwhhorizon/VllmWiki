# vllm-project/vllm#34650: Bug: Speculative Decoding (MTP) Causes </think> Detection Failure in Structured Output + Reasoning Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#34650](https://github.com/vllm-project/vllm/issues/34650) |
| 状态 | open |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Bug: Speculative Decoding (MTP) Causes </think> Detection Failure in Structured Output + Reasoning Mode

### Issue 正文摘录

# Summary When using MTP speculative decoding together with a reasoning parser and structured output (`response_format={"type": "json_schema"}`), the ` ` token can be silently missed by the `StructuredOutputManager.should_advance()` method. This causes `reasoning_ended` to never become `True`, so JSON schema constraints are never enforced after the thinking phase ends. --- # Root Cause In `vllm/v1/structured_output/__init__.py:324-328`, `should_advance()` computes the delta tokens to check for the ` ` token: ```python delta_from = request.num_computed_tokens - request.num_output_placeholders all_token_ids = request.all_token_ids if self.reasoner.is_reasoning_end_streaming( all_token_ids, all_token_ids[delta_from:] ): structured_req.reasoning_ended = True ``` The problem is a timing mismatch between `num_computed_tokens` and `all_token_ids` in the speculative decoding path: 1. `_update_after_schedule()` (`scheduler.py:943`) increments `num_computed_tokens` by all scheduled tokens, including speculative tokens, **before** the model runs. 2. After model execution, `_update_request_with_output()` (`scheduler.py:1352`) appends the generated tokens (accepted spec tokens + bonus token) t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: e()` so the method doesn't need to recompute the delta. --- # Affected Versions Any version of vLLM V1 with speculative decoding + reasoning parser + structured output. # Environment ``` Collecting environment informati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: structured_req.reasoning_ended = True ``` The problem is a timing mismatch between `num_computed_tokens` and `all_token_ids` in the speculative decoding path: 1. `_update_after_schedule()` (`scheduler.py:943`) increment...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: coding together with a reasoning parser and structured output (`response_format={"type": "json_schema"}`), the ` ` token can be silently missed by the `StructuredOutputManager.should_advance()` method. This causes `reas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Bug: Speculative Decoding (MTP) Causes </think> Detection Failure in Structured Output + Reasoning Mode bug # Summary When using MTP speculative decoding together with a reasoning parser and structured output (`response...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.3 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.9.1.4 [pip3] nvidia-cuda-cupti-cu12==12.9.79 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
