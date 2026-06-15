# vllm-project/vllm#27877: [Usage]: How to install nightly version??? Why this command doesn't work?

| 字段 | 值 |
| --- | --- |
| Issue | [#27877](https://github.com/vllm-project/vllm/issues/27877) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to install nightly version??? Why this command doesn't work?

### Issue 正文摘录

### Your current environment I run this to install vllm with the latest code. But, the installed vllm doesn't include the code I need. I check the `siglip.py` file, it's modified 4 days ago. But in the vllm installed, it doesn't contain this commit! https://github.com/vllm-project/vllm/pull/27566/files#diff-ca771e5a262cbf32fb481c518bea41d0e341414e021d6542e421abb98cceec61 why is this? I use this command. ```text pip install -U vllm \ --pre \ --extra-index-url https://wheels.vllm.ai/nightly``` `pip install -U vllm \ --pre \ --extra-index-url https://wheels.vllm.ai/nightly Defaulting to user installation because normal site-packages is not writeable Looking in indexes: https://bytedpypi.byted.org/simple, https://bytedpypi.byted.org/simple, https://wheels.vllm.ai/nightly Requirement already satisfied: vllm in /home/alice/.local/lib/python3.10/site-packages (0.11.0) Collecting vllm Downloading https://wheels.vllm.ai/nightly/vllm-0.11.1rc6.dev16%2Bg933cdea44.cu129-cp38-abi3-manylinux1_x86_64.whl (479.0 MB) ━╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.8/479.0 MB 575.3 kB/s eta 0:13:22` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Usage]: How to install nightly version??? Why this command doesn't work? usage;stale ### Your current environment I run this to install vllm with the latest code. But, the installed vllm doesn't include the code I need...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : How to install nightly version??? Why this command doesn't work? usage;stale ### Your current environment I run this to install vllm with the latest code. But, the installed vllm doesn't include the code I need. I che...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tale ### Your current environment I run this to install vllm with the latest code. But, the installed vllm doesn't include the code I need. I check the `siglip.py` file, it's modified 4 days ago. But in the vllm install...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
