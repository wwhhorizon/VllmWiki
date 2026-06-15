# vllm-project/vllm#44012: [Bug]: Responses API + `text.format` json_schema is not grammar-constrained when a reasoning parser is enabled — output escapes into the unconstrained `reasoning` channel

| 字段 | 值 |
| --- | --- |
| Issue | [#44012](https://github.com/vllm-project/vllm/issues/44012) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | fp8;moe;sampling |
| 症状 | build_error;mismatch;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Responses API + `text.format` json_schema is not grammar-constrained when a reasoning parser is enabled — output escapes into the unconstrained `reasoning` channel

### Issue 正文摘录

## Summary On a server started with `--reasoning-parser`, structured output via the **Responses API** (`/v1/responses`, `text.format.type="json_schema"`) is **not enforced by the structured-outputs backend**. The model's text is emitted into the unconstrained `reasoning` item instead of a grammar-constrained `message`, so xgrammar never binds. With Qwen it intermittently degenerates into bracket-spam (`}]}]}]}...`) and returns invalid JSON in roughly half of runs. The **Chat Completions API** (`/v1/chat/completions`, `response_format.type="json_schema"`) on the *same server, same model, same schema, thinking disabled* keeps the output in the grammar-constrained `content` channel and is valid 100% of the time. This looks like the same failure family as #34650 (` ` detection failure → json_schema not enforced after the thinking phase), but here it is reproducible on the plain Responses path — no speculative decoding required — and is triggered by the reasoning parser being active at all (especially with a custom `reasoning_end_str`). ## Environment - vLLM **v0.21.0** (`vllm/vllm-openai:v0.21.0`) - Model **Qwen/Qwen3.6-35B-A3B-FP8** (MoE, FP8), 1× A100 80 GB - Relevant serve args: ``...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: ure → json_schema not enforced after the thinking phase), but here it is reproducible on the plain Responses path — no speculative decoding required — and is triggered by the reasoning parser being active at all (especi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Responses API + `text.format` json_schema is not grammar-constrained when a reasoning parser is enabled — output escapes into the unconstrained `reasoning` channel ## Summary On a server started with `--reasoning...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: son_schema not enforced after the thinking phase), but here it is reproducible on the plain Responses path — no speculative decoding required — and is triggered by the reasoning parser being active at all (especially wi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: **v0.21.0** (`vllm/vllm-openai:v0.21.0`) - Model **Qwen/Qwen3.6-35B-A3B-FP8** (MoE, FP8), 1× A100 80 GB - Relevant serve args: ``` --enable-auto-tool-choice --tool-call-parser qwen3_coder --structured-outputs-config '{"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ing phase), but here it is reproducible on the plain Responses path — no speculative decoding required — and is triggered by the reasoning parser being active at all (especially with a custom `reasoning_end_str`). ## En...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
