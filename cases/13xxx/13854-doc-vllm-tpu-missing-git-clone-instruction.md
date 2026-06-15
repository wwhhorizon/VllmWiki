# vllm-project/vllm#13854: [Doc]: vLLM TPU missing git clone instruction

| 字段 | 值 |
| --- | --- |
| Issue | [#13854](https://github.com/vllm-project/vllm/issues/13854) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: vLLM TPU missing git clone instruction

### Issue 正文摘录

### 📚 The doc issue In the section for installation vLLM on TPU -https://docs.vllm.ai/en/v0.5.5/getting_started/tpu-installation.html#build-from-source The last steps fails as we have cloned the vllm repo ``` pip install -r requirements-tpu.txt ``` This must be cloned on all the workers before the above can be run. Else it fails. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: instruction documentation;stale ### 📚 The doc issue In the section for installation vLLM on TPU -https://docs.vllm.ai/en/v0.5.5/getting_started/tpu-installation.html#build-from-source The last steps fails as we have clo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ``` This must be cloned on all the workers before the above can be run. Else it fails. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: vLLM TPU missing git clone instruction documentation;stale ### 📚 The doc issue In the section for installation vLLM on TPU -https://docs.vllm.ai/en/v0.5.5/getting_started/tpu-installation.html#build-from-source T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
