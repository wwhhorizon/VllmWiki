# vllm-project/vllm#23468: [Bug]: YAML served-model-name list is parsed as a single literal string; aliases not accepted (only single-flag multi-token CLI works)

| 字段 | 值 |
| --- | --- |
| Issue | [#23468](https://github.com/vllm-project/vllm/issues/23468) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: YAML served-model-name list is parsed as a single literal string; aliases not accepted (only single-flag multi-token CLI works)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When launching with a YAML config that specifies multiple served-model-name entries, /v1/models exposes one id that is the stringified list, and requests using an individual alias return 404. Repeating the flag (--served-model-name A then --served-model-name B) also fails (last one wins). Only --served-model-name A B (one flag, multiple tokens) works using the command line. Docs say multiple names should be accepted and the first returned in responses. Reproduce config.yaml: model: Nous-Hermes-2-Yi-34B-AWQ dtype: half gpu-memory-utilization: 0.95 max-num-seqs: 8 max-num-batched-tokens: 16384 tensor-parallel-size: 1 served-model-name: - Nous-Hermes-2-Yi-34B - gpt-4.1-2025-04-14 api-key: EMPTY port: 8000 Launch: vllm serve --config Nous-Hermes-2-Yi-34B-AWQ.yaml Results: curl -s http:// :8000/v1/models -H "Authorization: Bearer EMPTY" | jq -r '.data[].id' => ['Nous-Hermes-2-Yi-34B', 'gpt-4.1-2025-04-14'] (one literal id) curl -s http:// :8000/v1/chat/completions \ -H "Authorization: Bearer EMPTY" -H "Content-Type: application/json" \ -d '{"model":"gpt-4.1-2025-04-14","messages":[{"role":"user","content":"ping"}]}' => 404 The model `...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nt ### 🐛 Describe the bug When launching with a YAML config that specifies multiple served-model-name entries, /v1/models exposes one id that is the stringified list, and requests using an individual alias return 404. R...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tring; aliases not accepted (only single-flag multi-token CLI works) bug;stale ### Your current environment ### 🐛 Describe the bug When launching with a YAML config that specifies multiple served-model-name entries, /v1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: d in responses. Reproduce config.yaml: model: Nous-Hermes-2-Yi-34B-AWQ dtype: half gpu-memory-utilization: 0.95 max-num-seqs: 8 max-num-batched-tokens: 16384 tensor-parallel-size: 1 served-model-name: - Nous-Hermes-2-Yi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: YAML served-model-name list is parsed as a single literal string; aliases not accepted (only single-flag multi-token CLI works) bug;stale ### Your current environment ### 🐛 Describe the bug When launching with a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
