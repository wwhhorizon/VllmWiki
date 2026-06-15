# vllm-project/vllm#26293: [RFC]: replace deprecated torch_dtype by dtype

| 字段 | 值 |
| --- | --- |
| Issue | [#26293](https://github.com/vllm-project/vllm/issues/26293) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: replace deprecated torch_dtype by dtype

### Issue 正文摘录

### Motivation. Huggingface recently updated the argument from `torch_dtype` to a simple `dtype` to be coherent with PyTorch (see PR [here](https://github.com/huggingface/transformers/pull/39782)). Although their implementation is backward compatible, we could consider also making the change `torch_dtype` -> `dtype` to not trigger the warning: ``` `torch_dtype` is deprecated! Use `dtype` instead! ``` The warning is triggered for every call that involves huggingface (even if it is just for loading the model). For example: ``` vllm bench latency --model "any_model_from_hf_hub" . . . ``` triggers the above warning. ### Proposed Change. Following changes are suggested: - Replace `torch_dtype` with `dtype` to silence above warning and be prepared to when `torch_dtype` is fully removed in hf. - Ensure backwards compatibility from vLLM user perspective. - (Optional) add a test for backwards compatibility. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://do...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: replace deprecated torch_dtype by dtype RFC ### Motivation. Huggingface recently updated the argument from `torch_dtype` to a simple `dtype` to be coherent with PyTorch (see PR [here](https://github.com/huggingfa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: even if it is just for loading the model). For example: ``` vllm bench latency --model "any_model_from_hf_hub" . . . ``` triggers the above warning. ### Proposed Change. Following changes are suggested: - Replace `torch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [RFC]: replace deprecated torch_dtype by dtype RFC ### Motivation. Huggingface recently updated the argument from `torch_dtype` to a simple `dtype` to be coherent with PyTorch (see PR [here](https://github.com/huggingfa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
