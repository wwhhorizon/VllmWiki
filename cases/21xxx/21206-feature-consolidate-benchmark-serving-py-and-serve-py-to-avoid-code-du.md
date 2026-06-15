# vllm-project/vllm#21206: [Feature]: Consolidate benchmark_serving.py and serve.py to avoid code duplication and usage confusions

| 字段 | 值 |
| --- | --- |
| Issue | [#21206](https://github.com/vllm-project/vllm/issues/21206) |
| 状态 | closed |
| 标签 | performance;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Consolidate benchmark_serving.py and serve.py to avoid code duplication and usage confusions

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we have 2 versions of benchmark scripts (e.g. benchmark_serving.py and serve.py). Most of their code are simply duplicated, and sometime it's confusing which should be treated as the source of truth. Discussed with @simon-mo @ywang96 @yeqcharlotte in https://github.com/vllm-project/vllm/pull/21108#issuecomment-3086656585, we all agreed that we should ultimately deprecate benchmark_serving.py and only maintain serve.py as the golden benchmark script. A few action items to address the issue. - [ ] Stop refering benchmark_serving.py in all documentations - [ ] Delete duplicated code in benchmark_serving.py, and reuse serve.py code as much as possible - [ ] [Stretched] Delete benchmark_serving.py ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Consolidate benchmark_serving.py and serve.py to avoid code duplication and usage confusions performance;feature request ### 🚀 The feature, motivation and pitch Currently, we have 2 versions of benchmark scri...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: re request ### 🚀 The feature, motivation and pitch Currently, we have 2 versions of benchmark scripts (e.g. benchmark_serving.py and serve.py). Most of their code are simply duplicated, and sometime it's confusing which...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ve.py to avoid code duplication and usage confusions performance;feature request ### 🚀 The feature, motivation and pitch Currently, we have 2 versions of benchmark scripts (e.g. benchmark_serving.py and serve.py). Most...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
