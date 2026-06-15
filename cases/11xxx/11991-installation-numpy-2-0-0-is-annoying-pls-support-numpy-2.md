# vllm-project/vllm#11991: [Installation]: `numpy < 2.0.0` is annoying. Pls support `numpy == 2`

| 字段 | 值 |
| --- | --- |
| Issue | [#11991](https://github.com/vllm-project/vllm/issues/11991) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: `numpy < 2.0.0` is annoying. Pls support `numpy == 2`

### Issue 正文摘录

### Your current environment it is not a bug in vllm, but it is annoying to see that vllm still insists on `numpy < 2.0.0` which distorts my environment build. Almost everyone else already supports numpy==2 ref https://github.com/vllm-project/vllm/blob/cf6bbcb49324c24fc0f6f9381400c299c9c2d7ac/requirements-common.txt#L3 there are a few related issues, like https://github.com/vllm-project/vllm/issues/5594 but perhaps by today all relevant components are supportingn numpy=2 ### How you are installing vllm ```sh pip install -i https://pypi.org/simple vllm ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: `numpy < 2.0.0` is annoying. Pls support `numpy == 2` installation;stale ### Your current environment it is not a bug in vllm, but it is annoying to see that vllm still insists on `numpy < 2.0.0` which di
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: on `numpy < 2.0.0` which distorts my environment build. Almost everyone else already supports numpy==2 ref https://github.com/vllm-project/vllm/blob/cf6bbcb49324c24fc0f6f9381400c299c9c2d7ac/requirements-common.txt#L3 th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ion]: `numpy < 2.0.0` is annoying. Pls support `numpy == 2` installation;stale ### Your current environment it is not a bug in vllm, but it is annoying to see that vllm still insists on `numpy < 2.0.0` which distorts my...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
