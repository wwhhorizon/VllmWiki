# vllm-project/vllm#18898: [Feature]: Enable setting `leave=False` in `tqdm` progress bars

| 字段 | 值 |
| --- | --- |
| Issue | [#18898](https://github.com/vllm-project/vllm/issues/18898) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable setting `leave=False` in `tqdm` progress bars

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In my use case I'm running many offline evaluations of models, so the terminal quickly gets cluttered with vLLM progress bars. This is due to the progress bar in the `LLM._run_engine` method as well as the newer "Adding requests" progress bar in the `LLM._add_requests_with_fixed_progress_bars` method. I propose adding a new Boolean argument, `tqdm_leave_pbar`, defaulting to `True`, consistent with the current behaviour, to all functions with the `use_tqdm` argument. ### Alternatives I'm currently dealing with this myself in a hacky way by replacing the above-mentioned methods of `LLM` with copied ones where I have set `leave=False` manually. This is of course not sustainable, as I don't get any updates to these methods. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e feature, motivation and pitch In my use case I'm running many offline evaluations of models, so the terminal quickly gets cluttered with vLLM progress bars. This is due to the progress bar in the `LLM._run_engine` met...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ernatives I'm currently dealing with this myself in a hacky way by replacing the above-mentioned methods of `LLM` with copied ones where I have set `leave=False` manually. This is of course not sustainable, as I don't g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Enable setting `leave=False` in `tqdm` progress bars feature request ### 🚀 The feature, motivation and pitch In my use case I'm running many offline evaluations of models, so the terminal quickly gets clutter...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vation and pitch In my use case I'm running many offline evaluations of models, so the terminal quickly gets cluttered with vLLM progress bars. This is due to the progress bar in the `LLM._run_engine` method as well as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
