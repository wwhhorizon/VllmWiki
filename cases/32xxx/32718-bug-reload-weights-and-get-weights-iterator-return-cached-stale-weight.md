# vllm-project/vllm#32718: [Bug]: `reload_weights` and `_get_weights_iterator` return cached/stale weights instead of re-reading from disk

| 字段 | 值 |
| --- | --- |
| Issue | [#32718](https://github.com/vllm-project/vllm/issues/32718) |
| 状态 | closed |
| 标签 | bug;rl |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `reload_weights` and `_get_weights_iterator` return cached/stale weights instead of re-reading from disk

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vLLM for RLHF/GRPO training workflows where model weights are periodically updated on disk and need to be reloaded into the running vLLM server, the `reload_weights` API and `DefaultModelLoader._get_weights_iterator()` return **cached/stale weights** from the initial model load instead of re-reading the updated files from disk. This makes online RLHF training with vLLM impossible, as the inference server continues serving predictions from the old weights even after new weights have been written to disk and `reload_weights` has been called. ## Reproduction Steps 1. Start vLLM server with a model: ```bash vllm serve /path/to/model --enable-sleep-mode --data-parallel-size 4 ``` 2. Save new/modified weights to the same path (overwriting the original files) 3. Call `reload_weights` via the API: ```python import httpx resp = httpx.post("http://localhost:8000/collective_rpc", json={"method": "reload_weights"}, timeout=120) ``` 4. **Expected**: Model should use the new weights 5. **Actual**: Model continues using the original weights ## Diagnostic Evidence I instrumented the code to compare weights loaded directly from disk vs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ing the original files) 3. Call `reload_weights` via the API: ```python import httpx resp = httpx.post("http://localhost:8000/collective_rpc", json={"method": "reload_weights"}, timeout=120) ``` 4. **Expected**: Model s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ur current environment ### 🐛 Describe the bug When using vLLM for RLHF/GRPO training workflows where model weights are periodically updated on disk and need to be reloaded into the running vLLM server, the `reload_weigh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gy. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: `reload_weights` and `_get_weights_iterator` return cached/stale weights instead of re-reading from disk bug;rl ### Your current environment ### 🐛 Describe the bug When using vLLM for RLHF/GRPO training workflows...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
