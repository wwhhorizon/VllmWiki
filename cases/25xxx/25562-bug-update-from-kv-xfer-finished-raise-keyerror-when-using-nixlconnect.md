# vllm-project/vllm#25562: [Bug]: update_from_kv_xfer_finished raise KeyError when using NixlConnector

| 字段 | 值 |
| --- | --- |
| Issue | [#25562](https://github.com/vllm-project/vllm/issues/25562) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: update_from_kv_xfer_finished raise KeyError when using NixlConnector

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I am using Nixl to do PD testing, KeyError occurs in some cases. This should be because I canceled some requests, which were released after being timed out by Nixl, but it is not detected here. ``` (EngineCore_DP0 pid=3747544) WARNING 09-24 16:35:21 [nixl_connector.py:1048] Releasing expired KV blocks for request cmpl-3da205a6-1c3c-41b5-aeaa-b8421e81fd5c-0 which were retrieved by 0 decode worker(s) within 120 seconds. (EngineCore_DP0 pid=3747544) WARNING 09-24 16:35:21 [nixl_connector.py:1048] Releasing expired KV blocks for request cmpl-efed6d02-710d-4f07-b643-ffb9a14f0858-0 which were retrieved by 0 decode worker(s) within 120 seconds. (EngineCore_DP0 pid=3747544) WARNING 09-24 16:35:21 [nixl_connector.py:1048] Releasing expired KV blocks for request cmpl-fe226f2e-264c-4fd9-8c57-a115f9641164-0 which were retrieved by 0 decode worker(s) within 120 seconds. (EngineCore_DP0 pid=3747544) WARNING 09-24 16:35:21 [nixl_connector.py:1048] Releasing expired KV blocks for request cmpl-5193325c-c597-4ae6-9cb1-29fa8c08f5d7-0 which were retrieved by 0 decode worker(s) within 120 seconds. (EngineCore_DP0 pid=3747544) WARNING 09-24 16:35...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: update_from_kv_xfer_finished raise KeyError when using NixlConnector bug;stale ### Your current environment ### 🐛 Describe the bug When I am using Nixl to do PD testing, KeyError occurs in some cases. This should be bec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: onnector.py:1048] Releasing expired KV blocks for request cmpl-51748e26-cfa3-4e38-ba34-771f24388a0c-0 which were retrieved by 0 decode worker(s) within 120 seconds. (EngineCore_DP0 pid=3747544) WARNING 09-24 16:35:21 [n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ineCore_DP0 pid=3747544) ERROR 09-24 16:35:21 [core.py:720] outputs, model_executed = self.step_fn() (EngineCore_DP0 pid=3747544) ERROR 09-24 16:35:21 [core.py:720] File "/root/daocloud/kebe/vllm-dev/lib/python3.10/site...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
