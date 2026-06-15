# vllm-project/vllm#28115: [Installation]: Request to include vllm==0.10.2 for cuda 11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#28115](https://github.com/vllm-project/vllm/issues/28115) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Request to include vllm==0.10.2 for cuda 11.8

### Issue 正文摘录

### Your current environment cuda 11.8 ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. Could you please support CUDA 11.8? https://github.com/vllm-project/vllm/releases/tag/v0.10.2 Thanks!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Request to include vllm==0.10.2 for cuda 11.8 installation;stale ### Your current environment cuda 11.8 ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Request to include vllm==0.10.2 for cuda 11.8 installation;stale ### Your current environment cuda 11.8 ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue.....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: Request to include vllm==0.10.2 for cuda 11.8 installation;stale ### Your current environment cuda 11.8 ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue.....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. Could you please support CUDA 11.8? https://github.com/vllm-project/vllm/releases/tag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
