# vllm-project/vllm#19020: [Feature]: online bf16->fp8 (and maybe even fp4?) quantization in `load_weights(...)` (so not only from disk checkpoint, but importantly from VRAM or RAM) for weights reloading in GRPO rollout workloads, and speed gains for generating long reasoning rollouts and peak VRAM reduction

| 字段 | 值 |
| --- | --- |
| Issue | [#19020](https://github.com/vllm-project/vllm/issues/19020) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: online bf16->fp8 (and maybe even fp4?) quantization in `load_weights(...)` (so not only from disk checkpoint, but importantly from VRAM or RAM) for weights reloading in GRPO rollout workloads, and speed gains for generating long reasoning rollouts and peak VRAM reduction

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This would be very useful for syncing grpo training weights into the vllm rollout workers. For long reasoning rollouts, the rollout stage can take 50-70%, so being able to do this stage in fp8 (and benefit from fp8 quant improvements in vllm) would be very beneficial. I found that https://github.com/vllm-project/vllm/blob/ebb1ec931871ee1baca23673049865856c44ce4e/examples/offline_inference/rlhf_utils.py#L53 `load_weights` method is recommended for this kind of weight update. It would be nice to have `quantization="fp8"` support directly in this method, as it now exists in `LLM` class argument (https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community#fp8_inference_quickstart) verl does use the `load_weights` API per-tensor (so it does mulitple separate calls): - https://github.com/volcengine/verl/issues/1803#issuecomment-2930587833 Maybe adding fp8 quant option directly to this method would be helpful (especially if the code for this already exists for handling the `LLM(..., quantization="fp8")` online bf16->fp8 checkpoint loading). And if any fp8 calibration methods exist that could improve fp8 quant i...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: online bf16->fp8 (and maybe even fp4?) quantization in `load_weights(...)` (so not only from disk checkpoint, but importantly from VRAM or RAM) for weights reloading in GRPO rollout workloads, and speed gains...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: antization in `load_weights(...)` (so not only from disk checkpoint, but importantly from VRAM or RAM) for weights reloading in GRPO rollout workloads, and speed gains for generating long reasoning rollouts and peak VRA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s for generating long reasoning rollouts and peak VRAM reduction feature request;unstale ### 🚀 The feature, motivation and pitch This would be very useful for syncing grpo training weights into the vllm rollout workers....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ob/ebb1ec931871ee1baca23673049865856c44ce4e/examples/offline_inference/rlhf_utils.py#L53 `load_weights` method is recommended for this kind of weight update. It would be nice to have `quantization="fp8"` support directl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
