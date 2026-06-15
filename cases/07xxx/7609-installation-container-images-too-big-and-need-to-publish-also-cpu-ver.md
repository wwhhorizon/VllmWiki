# vllm-project/vllm#7609: [Installation]: container images - too big and need to publish also cpu versions

| 字段 | 值 |
| --- | --- |
| Issue | [#7609](https://github.com/vllm-project/vllm/issues/7609) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: container images - too big and need to publish also cpu versions

### Issue 正文摘录

### Your current environment not a problem in my own env ### How you are installing vllm ```sh docker pull vllm/vllm-openai:latest ``` notice that what i want is to have cpu version as well ```sh docker pull vllm/vllm-openai:latest-cpu ``` also the regular (GPU) image is too big, it is 5GB, can we do something about it and make it smaller than < 1GB If this project needs help with this specific issue i can help, i want these container optimizations

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: container images - too big and need to publish also cpu versions installation;stale ### Your current environment not a problem in my own env ### How you are installing vllm ```sh docker pull vllm/vllm-o
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: U) image is too big, it is 5GB, can we do something about it and make it smaller than < 1GB If this project needs help with this specific issue i can help, i want these container optimizations
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: iner images - too big and need to publish also cpu versions installation;stale ### Your current environment not a problem in my own env ### How you are installing vllm ```sh docker pull vllm/vllm-openai:latest ``` notic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: v ### How you are installing vllm ```sh docker pull vllm/vllm-openai:latest ``` notice that what i want is to have cpu version as well ```sh docker pull vllm/vllm-openai:latest-cpu ``` also the regular (GPU) image is to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
