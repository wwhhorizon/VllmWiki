# vllm-project/vllm#10540: [Installation]: can't get the cu118 version of vllm 0.6.3 by https://github.com/vllm-project/vllm/releases/download/v0.6.3/vllm-0.6.3+cu118-cp310-cp310-manylinux1_x86_64.whl

| 字段 | 值 |
| --- | --- |
| Issue | [#10540](https://github.com/vllm-project/vllm/issues/10540) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: can't get the cu118 version of vllm 0.6.3 by https://github.com/vllm-project/vllm/releases/download/v0.6.3/vllm-0.6.3+cu118-cp310-cp310-manylinux1_x86_64.whl

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: can't get the cu118 version of vllm 0.6.3 by https://github.com/vllm-project/vllm/releases/download/v0.6.3/vllm-0.6.3+cu118-cp310-cp310-manylinux1_x86_64.whl installation;stale ### Your current environme...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d/v0.6.3/vllm-0.6.3+cu118-cp310-cp310-manylinux1_x86_64.whl installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
