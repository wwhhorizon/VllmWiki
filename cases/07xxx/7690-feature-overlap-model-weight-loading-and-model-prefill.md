# vllm-project/vllm#7690: [Feature]: Overlap model weight loading and model prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#7690](https://github.com/vllm-project/vllm/issues/7690) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Overlap model weight loading and model prefill

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For LLM inference, requests per second(QPS) is not constant. It needs launch vllm engine on demand. For elastic instance, it's significance to reduce TTFT(Time to First Token). Hence, it's necessary to overlap model loading and prefill, especially very large model which model loading costs several seconds. ### Alternatives 1. Model cache system for vllm: efficient IO (such as: PCIe, NVLink) 2. Load model weight by LLM topo order and execute model immediately after parameter is ready ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Overlap model weight loading and model prefill feature request;stale ### 🚀 The feature, motivation and pitch For LLM inference, requests per second(QPS) is not constant. It needs launch vllm engine on demand....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Token). Hence, it's necessary to overlap model loading and prefill, especially very large model which model loading costs several seconds. ### Alternatives 1. Model cache system for vllm: efficient IO (such as: PCIe, NV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Overlap model weight loading and model prefill feature request;stale ### 🚀 The feature, motivation and pitch For LLM inference, requests per second(QPS) is not constant. It needs launch vllm engine on demand....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
