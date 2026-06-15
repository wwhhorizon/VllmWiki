# vllm-project/vllm#16683: [Installation]: Can we make `csrc` a new/separate wheel?

| 字段 | 值 |
| --- | --- |
| Issue | [#16683](https://github.com/vllm-project/vllm/issues/16683) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Can we make `csrc` a new/separate wheel?

### Issue 正文摘录

### Your current environment For many of the development, we don't need to touch the compiled kernels in `csrc`. We do some repacking stuff in setup.py for this exact purpose but it's a bit hacky. I wonder if we can make a separate wheel like `vllm-kernels` or something for https://github.com/vllm-project/vllm/tree/main/csrc. Effectively, it means move CMakefile.txt one level into csrc and take care of the setup. I wonder if folks think this is something worth doing. ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Can we make `csrc` a new/separate wheel? installation;stale ### Your current environment For many of the development, we don't need to touch the compiled kernels in `csrc`. We do some repacking stuff in s
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Can we make `csrc` a new/separate wheel? installation;stale ### Your current environment For many of the development, we don't need to touch the compiled kernels in `csrc`. We do some repacking stuff in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
