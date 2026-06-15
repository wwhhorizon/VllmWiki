# vllm-project/vllm#31859: [Bug]: Intermittent 500 Internal Server Error When Stress-Testing Qwen3-VL-2B-Instruct with vLLM on H20

| 字段 | 值 |
| --- | --- |
| Issue | [#31859](https://github.com/vllm-project/vllm/issues/31859) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Intermittent 500 Internal Server Error When Stress-Testing Qwen3-VL-2B-Instruct with vLLM on H20

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi all, I’m currently deploying the Qwen3-VL-2B-Instruct model on H20 using vLLM for inference services. During stress testing at a constant 16 QPS, an issue occurs after the service runs continuously for a while: The service throws an internal server error and returns HTTP 500 for all incoming requests. No additional manual intervention is required—the service will automatically recover and return to normal operation after some time passes. Has anyone encountered a similar problem before? I’d appreciate any insights into the root causes or troubleshooting directions. Thanks in advance!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Intermittent 500 Internal Server Error When Stress-Testing Qwen3-VL-2B-Instruct with vLLM on H20 bug ### Your current environment ### 🐛 Describe the bug Hi all, I’m currently deploying the Qwen3-VL-2B-Instruct mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e time passes. Has anyone encountered a similar problem before? I’d appreciate any insights into the root causes or troubleshooting directions. Thanks in advance!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ce throws an internal server error and returns HTTP 500 for all incoming requests. No additional manual intervention is required—the service will automatically recover and return to normal operation after some time pass...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Intermittent 500 Internal Server Error When Stress-Testing Qwen3-VL-2B-Instruct with vLLM on H20 bug ### Your current environment ### 🐛 Describe the bug Hi all, I’m currently deploying the Qwen3-VL-2B-Instruct mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
