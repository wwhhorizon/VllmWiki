# vllm-project/vllm#33319: [Bug]: Requests Stuck in Waiting Queue with Zero Running

| 字段 | 值 |
| --- | --- |
| Issue | [#33319](https://github.com/vllm-project/vllm/issues/33319) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Requests Stuck in Waiting Queue with Zero Running

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My vLLM Docker container v0.10.2 has been running for 3 months straight, hosting a Llama-4-Scout FP16 model, but suddenly requests stopped being served. When I checked the Docker logs, it showed that requests were stuck in the "Waiting" queue while no requests were in "Running"

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Requests Stuck in Waiting Queue with Zero Running bug;stale ### Your current environment ### 🐛 Describe the bug My vLLM Docker container v0.10.2 has been running for 3 months straight, hosting a Llama-4-Scout FP1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g;stale ### Your current environment ### 🐛 Describe the bug My vLLM Docker container v0.10.2 has been running for 3 months straight, hosting a Llama-4-Scout FP16 model, but suddenly requests stopped being served. When I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cker container v0.10.2 has been running for 3 months straight, hosting a Llama-4-Scout FP16 model, but suddenly requests stopped being served. When I checked the Docker logs, it showed that requests were stuck in the "W...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
