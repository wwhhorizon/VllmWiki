# vllm-project/vllm#10244: [Installation]: Install Gpu vllm got no module named triton

| 字段 | 值 |
| --- | --- |
| Issue | [#10244](https://github.com/vllm-project/vllm/issues/10244) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Install Gpu vllm got no module named triton

### Issue 正文摘录

### Your current environment ```text Install Gpu vllm 0.6.3 post6 with tesla v100and cuda 12.4,when import vllm got no module named triton ``` ### How you are installing vllm ```sh install with source code ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Install Gpu vllm got no module named triton installation;stale ### Your current environment ```text Install Gpu vllm 0.6.3 post6 with tesla v100and cuda 12.4,when import vllm got no module named triton ``
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent environment ```text Install Gpu vllm 0.6.3 post6 with tesla v100and cuda 12.4,when import vllm got no module named triton ``` ### How you are installing vllm ```sh install with source code ``` ### Before submitting...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Installation]: Install Gpu vllm got no module named triton installation;stale ### Your current environment ```text Install Gpu vllm 0.6.3 post6 with tesla v100and cuda 12.4,when import vllm got no module named triton `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Install Gpu vllm got no module named triton installation;stale ### Your current environment ```text Install Gpu vllm 0.6.3 post6 with tesla v100and cuda 12.4,when import vllm got no module named triton `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development cuda;triton Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
