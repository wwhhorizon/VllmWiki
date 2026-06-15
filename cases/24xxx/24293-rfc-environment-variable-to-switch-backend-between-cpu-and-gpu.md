# vllm-project/vllm#24293: [RFC]: Environment variable to switch backend between CPU and GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#24293](https://github.com/vllm-project/vllm/issues/24293) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Environment variable to switch backend between CPU and GPU

### Issue 正文摘录

### Motivation. I have observed that I could install VLLM for either CPU or CUDA, but not both. Is it possible for a single VLLM instance to support both of them? This way, I can use some env variable to specify the backend. Or even otherwise, provide more flexibility to allow me to run prefill phase on GPU and decode phase on CPU without any hassles. This would be faster and and memory/compute efficient solution. This would also avoid usage of disaggregated prefill serving, which creates two instances and also does not support a connector between GPU and CPU currently. ### Proposed Change. This would require changing the build system to have optimal CPU and GPU kernels in single installed VLLM instance. Further, the dispatch mechanism to support CPU and GPU kernels depending on the tensor's current residing device may be needed. Might be extended to support heterogenous GPUs too such as NVIDIA and AMD. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd between CPU and GPU RFC ### Motivation. I have observed that I could install VLLM for either CPU or CUDA, but not both. Is it possible for a single VLLM instance to support both of them? This way, I can use some env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Motivation. I have observed that I could install VLLM for either CPU or CUDA, but not both. Is it possible for a single VLLM instance to support both of them? This way, I can use some env variable to specify the backend...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Environment variable to switch backend between CPU and GPU RFC ### Motivation. I have observed that I could install VLLM for either CPU or CUDA, but not both. Is it possible for a single VLLM instance to support...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: backend. Or even otherwise, provide more flexibility to allow me to run prefill phase on GPU and decode phase on CPU without any hassles. This would be faster and and memory/compute efficient solution. This would also a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel cuda;kernel build_error Motivation.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
