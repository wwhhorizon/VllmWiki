# vllm-project/vllm#12066: [Installation][build][docker]: rocm Dockerfile pinned to stale python torch nightly wheel builds

| 字段 | 值 |
| --- | --- |
| Issue | [#12066](https://github.com/vllm-project/vllm/issues/12066) |
| 状态 | closed |
| 标签 | installation;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation][build][docker]: rocm Dockerfile pinned to stale python torch nightly wheel builds

### Issue 正文摘录

### How you are installing vllm https://github.com/vllm-project/vllm/blob/0794e7446efca1fd7b8ea1cde96777897660cdea/Dockerfile.rocm#L48-L58 Python packages for `torch==2.6.0.dev20241113+rocm6.2` and `torchvision==0.20.0.dev20241113+rocm6.2` are no longer available due to them being outside of the build retention window Wheel Index: https://download.pytorch.org/whl/nightly/torch/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation][build][docker]: rocm Dockerfile pinned to stale python torch nightly wheel builds installation;rocm ### How you are installing vllm https://github.com/vllm-project/vllm/blob/0794e7446efca1fd7b8ea1cde967778
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation][build][docker]: rocm Dockerfile pinned to stale python torch nightly wheel builds installation;rocm ### How you are installing vllm https://github.com/vllm-project/vllm/blob/0794e7446efca1fd7b8ea1cde96777...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation][build][docker]: rocm Dockerfile pinned to stale python torch nightly wheel builds installation;rocm ### How you are installing vllm https://github.com/vllm-project/vllm/blob/0794e7446efca1fd7b8ea1cde96777...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
