# vllm-project/vllm#4881: [Installation]: Do we have the plan to update the pip package installation method for the CPU backend.

| 字段 | 值 |
| --- | --- |
| Issue | [#4881](https://github.com/vllm-project/vllm/issues/4881) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Do we have the plan to update the pip package installation method for the CPU backend.

### Issue 正文摘录

### CPU Backend Hi, https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html Seems I have to install the vLLM from the souce code, but I want to use the vllm by `pip install vllm=0.4.2+cpu`. Do we have the plan to update the pip install method for the CPU backend~? ### How you are installing vllm ```sh pip install vllm=0.4.2+cpu ```

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: have the plan to update the pip package installation method for the CPU backend. installation;stale ### CPU Backend Hi, https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html Seems I have to install the vL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: Do we have the plan to update the pip package installation method for the CPU backend. installation;stale ### CPU Backend Hi, https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html Seems I
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: te the pip package installation method for the CPU backend. installation;stale ### CPU Backend Hi, https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html Seems I have to install the vLLM from the souce cod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ckend. installation;stale ### CPU Backend Hi, https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html Seems I have to install the vLLM from the souce code, but I want to use the vllm by `pip install vllm=0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
