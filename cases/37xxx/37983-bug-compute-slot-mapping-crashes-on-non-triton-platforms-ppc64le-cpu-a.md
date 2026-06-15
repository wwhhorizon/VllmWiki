# vllm-project/vllm#37983: [Bug]: compute_slot_mapping crashes on non-Triton platforms (ppc64le/CPU) after PR #32951

| 字段 | 值 |
| --- | --- |
| Issue | [#37983](https://github.com/vllm-project/vllm/issues/37983) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: compute_slot_mapping crashes on non-Triton platforms (ppc64le/CPU) after PR #32951

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug PR #32951 replaced the numpy-based `compute_slot_mapping` with a Triton-only kernel launch (_compute_slot_mapping_kernel[(grid,)](...)) with no fallback — when Triton is absent, `@triton.jit` becomes the `TritonPlaceholder` no-op decorator which leaves the function as a plain Python function, making it non-subscriptable ```bash (APIServer pid=1328759) INFO: Started server process [1328759] (APIServer pid=1328759) INFO: Waiting for application startup. (APIServer pid=1328759) INFO: Application startup complete. (APIServer pid=1328759) INFO: 127.0.0.1:40838 - "GET /metrics HTTP/1.1" 200 OK (APIServer pid=1328759) INFO: 127.0.0.1:40838 - "POST /v1/completions HTTP/1.1" 200 OK (EngineCore pid=1328911) ERROR 03-24 03:32:45 [core.py:1110] EngineCore encountered a fatal error. (EngineCore pid=1328911) ERROR 03-24 03:32:45 [core.py:1110] Traceback (most recent call last): (EngineCore pid=1328911) ERROR 03-24 03:32:45 [core.py:1110] File "/home/akashk/vllm_workspace/vllm-wheel-managment/v0.11.1/vllm_env/lib64/python3.12/site-packages/vllm-0.18.1rc1.dev69+g2e67fa756.cpu-py3.12-linux-ppc64le.egg/vllm/v1/engine/core.py", line 1101, in run_en...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: R 03-24 03:32:45 [core.py:1110] File "/home/akashk/vllm_workspace/vllm-wheel-managment/v0.11.1/vllm_env/lib64/python3.12/site-packages/vllm-0.18.1rc1.dev69+g2e67fa756.cpu-py3.12-linux-ppc64le.egg/vllm/v1/engine/core.py"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: compute_slot_mapping crashes on non-Triton platforms (ppc64le/CPU) after PR #32951 bug ### Your current environment ### 🐛 Describe the bug PR #32951 replaced the numpy-based `compute_slot_mapping` with a Triton-o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: : Started server process [1328759] (APIServer pid=1328759) INFO: Waiting for application startup. (APIServer pid=1328759) INFO: Application startup complete. (APIServer pid=1328759) INFO: 127.0.0.1:40838 - "GET /metrics...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: compute_slot_mapping crashes on non-Triton platforms (ppc64le/CPU) after PR #32951 bug ### Your current environment ### 🐛 Describe the bug PR #32951 replaced the numpy-based `compute_slot_mapping` with a Triton-o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
