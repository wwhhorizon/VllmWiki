# vllm-project/vllm#9831: [Feature]: host wheel via pypi index?

| 字段 | 值 |
| --- | --- |
| Issue | [#9831](https://github.com/vllm-project/vllm/issues/9831) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: host wheel via pypi index?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently we host vllm wheels in aws, and ask users to install wheels via a long link: `pip install https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl` I have been thinking about various ways to improve it: 1. make the link shorter, e.g. `pip install https://wheels.vllm.ai/nightly.whl` , and redirect the url to https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl . It does not work because `pip` will use `nightly.whl` as the wheel filename, and cannot recognize the version. It refuses to install the wheel. 2. host a pypi index, and install via `pip install vllm --index-url https://wheels.vllm.ai/` . This is the way for [pytorch](https://pytorch.org/). It needs to host the dependent libraries as well, which is too complicated. 3. we can have a script to download the wheel, and let `pip` install that wheel directly. it can work, just like [oh my zsh](https://ohmyz.sh/#install) . however, it is not simpler than current approach. In summary, I think current approach works pretty well, and we don't need to change it. If we need to distribute nightl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: host wheel via pypi index? feature request;stale ### 🚀 The feature, motivation and pitch Currently we host vllm wheels in aws, and ask users to install wheels via a long link: `pip install https://vllm-wheels...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: host wheel via pypi index? feature request;stale ### 🚀 The feature, motivation and pitch Currently we host vllm wheels in aws, and ask users to install wheels via a long link: `pip install https://vllm-wheels...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: reate a short alias https://install.vllm.ai to https://docs.vllm.ai/en/latest/getting_started/installation.html , so that we can describe the installation in one line, in our slides. cc @simon-mo @khluu , just FYI, no a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
