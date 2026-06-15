# vllm-project/vllm#28334: [Bug][LoRA]: Custom AR IMA during CG Capture with LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#28334](https://github.com/vllm-project/vllm/issues/28334) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][LoRA]: Custom AR IMA during CG Capture with LoRA

### Issue 正文摘录

### 🐛 Describe the bug The custom AllReduce kernel fails with an illegal memory access error if is called within a capture cudagraph before the [`CustomAllReduce.capture` context manager](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/device_communicators/custom_all_reduce.py#L200) exits. This was previously not a problem since no cudagraphs were replayed until after `CustomAllReduce.capture` exited; but after https://github.com/vllm-project/vllm/pull/25914 enabled LoRA cudagraph specialization, the dummy run is executed twice for each `num_tokens` (once for `activate_lora=True`, and once for `activate_lora=False`). If spec decoding is enabled this second dummy run triggers a replay of the draft model cudagraph (since it does not depend on the value of `activate_lora`) and thus an illegal memory access error. A temporary fix for this was introduced by https://github.com/vllm-project/vllm/pull/28318, but I'm creating this issue to track a longer term resolution. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/lat...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fails with an illegal memory access error if is called within a capture cudagraph before the [`CustomAllReduce.capture` context manager](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/device_communicato...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug][LoRA]: Custom AR IMA during CG Capture with LoRA bug;stale ### 🐛 Describe the bug The custom AllReduce kernel fails with an illegal memory access error if is called within a capture cudagraph before the [`CustomAl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ttps://github.com/vllm-project/vllm/pull/25914 enabled LoRA cudagraph specialization, the dummy run is executed twice for each `num_tokens` (once for `activate_lora=True`, and once for `activate_lora=False`). If spec de...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: um_tokens` (once for `activate_lora=True`, and once for `activate_lora=False`). If spec decoding is enabled this second dummy run triggers a replay of the draft model cudagraph (since it does not depend on the value of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: decoding is enabled this second dummy run triggers a replay of the draft model cudagraph (since it does not depend on the value of `activate_lora`) and thus an illegal memory access error. A temporary fix for this was i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
