# vllm-project/vllm#17056: [Bug]: Issue with SpecDecode when using data parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#17056](https://github.com/vllm-project/vllm/issues/17056) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue with SpecDecode when using data parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running SpecDecode on VLLM with Qwen 2.5 Coder 32B AWQ model and 7B AWQ model as the parent and draft models. When using 4 H-200s on Modal and I try to launch the server it get's stuck and eventually times out with the following error ```torch.distributed.DistStoreError: Timed out after 601 seconds waiting for clients. 1/4 clients joined.``` Any help would be appreciated. The nccl test script works and passes! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Issue with SpecDecode when using data parallel bug;stale ### Your current environment ### 🐛 Describe the bug I am running SpecDecode on VLLM with Qwen 2.5 Coder 32B AWQ model and 7B AWQ model as the parent and dr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: onds waiting for clients. 1/4 clients joined.``` Any help would be appreciated. The nccl test script works and passes! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ronment ### 🐛 Describe the bug I am running SpecDecode on VLLM with Qwen 2.5 Coder 32B AWQ model and 7B AWQ model as the parent and draft models. When using 4 H-200s on Modal and I try to launch the server it get's stuc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ogits;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;crash;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
