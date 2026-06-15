# vllm-project/vllm#25576: [Doc]: https://docs.vllm.ai/en/v0.6.5/getting_started/installation.html

| 字段 | 值 |
| --- | --- |
| Issue | [#25576](https://github.com/vllm-project/vllm/issues/25576) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: https://docs.vllm.ai/en/v0.6.5/getting_started/installation.html

### Issue 正文摘录

### 📚 The doc issue I am not shure, if i am correct, but please check, thanx. git clone https://github.com/vllm-project/vllm.git cd vllm python use_existing_torch.py **pip install -r requirements-build.txt** >> **pip install -r requirements/build.txt** pip install -e . --no-build-isolation ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Doc]: https://docs.vllm.ai/en/v0.6.5/getting_started/installation.html documentation;stale ### 📚 The doc issue I am not shure, if i am correct, but please check, thanx. git clone https://github.com/vllm-project/vllm.gi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: //docs.vllm.ai/en/v0.6.5/getting_started/installation.html documentation;stale ### 📚 The doc issue I am not shure, if i am correct, but please check, thanx. git clone https://github.com/vllm-project/vllm.git cd vllm pyt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
