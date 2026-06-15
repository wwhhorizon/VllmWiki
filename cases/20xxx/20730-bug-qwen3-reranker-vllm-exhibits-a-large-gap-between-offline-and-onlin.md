# vllm-project/vllm#20730: [Bug]: Qwen3-Reranker-vllm exhibits a large gap between offline and online inference.

| 字段 | 值 |
| --- | --- |
| Issue | [#20730](https://github.com/vllm-project/vllm/issues/20730) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Reranker-vllm exhibits a large gap between offline and online inference.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a significant gap between the online inference results and the offline inference results for Qwen3-reranker. Online inference start command： ``` vllm serve Qwen3-Reranker-0.6B --host 0.0.0.0 --port 12501 --gpu_memory_utilization=0.5 --max-model-len 8192 --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' ``` curl： ``` curl -X POST "http://127.0.0.1:12501/rerank" \ -H "accept: application/json" \ -H "Content-Type: application/json" \ -d '{ "query":"信息科电话是多少", "documents":[ "科室名称:客服与投诉中心", "科室代码：10086,科室名称：信息中心本级", "科室代码：10086,科室名称：客服与投诉中心", "科室：机房，电话号码：8888888811；短号：00909090", "科室名称：信息中心本级", "科室：信息中心值班，考勤单元：信息中心；电话号码：13131313131313；短号：090909090；上级科室：行政后勤" ] }' ``` results： ``` { "results": [ { "index": 3, "document": { "text": "科室：机房，电话号码：8888888811；短号：00909090" }, "relevance_score": 0.7431679368019104 }, { "index": 2, "document": { "text": "科室代码：10086,科室名称：客服与投诉中心" }, "relevance_score": 0.7371581792831421 }, { "index": 0, "document": { "text": "科室名称:客服与投诉中心" }, "relevance_score": 0.671470582485199 }, { "index": 1, "document": { "...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Reranker-vllm exhibits a large gap between offline and online inference. bug;stale ### Your current environment ### 🐛 Describe the bug There is a significant gap between the online inference results and the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2501 --gpu_memory_utilization=0.5 --max-model-len 8192 --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' ``` curl： ``` curl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nker-vllm exhibits a large gap between offline and online inference. bug;stale ### Your current environment ### 🐛 Describe the bug There is a significant gap between the online inference results and the offline inferenc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ne inference results, and there is an issue with the online inference. I tested both Qwen3-reranker-0.6 and 4B, and they both have this problem. ### Before submitting a new issue... - [x] Make sure you already searched...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
