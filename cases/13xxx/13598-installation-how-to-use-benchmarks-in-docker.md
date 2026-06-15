# vllm-project/vllm#13598: [Installation]: how to use benchmarks in docker?

| 字段 | 值 |
| --- | --- |
| Issue | [#13598](https://github.com/vllm-project/vllm/issues/13598) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: how to use benchmarks in docker?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` hello, I successfully ran vllm using docker. Now I want to use benchmarks to test the performance, but there is no such script in the official docker. ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: how to use benchmarks in docker? installation ### Your current environment ```text The output of `python collect_env.py` ``` hello, I successfully ran vllm using docker. Now I want to use benchmarks to t
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Installation]: how to use benchmarks in docker? installation ### Your current environment ```text The output of `python collect_env.py` ``` hello, I successfully ran vllm using docker. Now I want to use benchmarks to t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
