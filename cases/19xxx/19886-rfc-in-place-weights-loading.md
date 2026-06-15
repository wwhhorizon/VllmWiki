# vllm-project/vllm#19886: [RFC]: In-place weights loading

| 字段 | 值 |
| --- | --- |
| Issue | [#19886](https://github.com/vllm-project/vllm/issues/19886) |
| 状态 | closed |
| 标签 | RFC;rl |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: In-place weights loading

### Issue 正文摘录

### Motivation. We've implemented the initial version of inplace weights loading in #18745 and #19884. Currently `load_model` will decide itself whether to load model from scratch or reload weighs inplace. Should we give users more control? I've been thinking about making the inplace weights loading choice explicit. In addition, a standalone weights reloading API makes it possible to support model swap in the original `load_model` method. ### Proposed Change. * `collective_rpc("load_model")` * this will always recreate model **and** load weights from sractch * `collective_rpc("update_config", overrides)` #20095 * Update any [config](https://github.com/vllm-project/vllm/blob/v0.9.1/vllm/v1/worker/gpu_model_runner.py#L85) in model runner. * For example, `collective_rpc("update_config", overrides={"load_config": {"load_format": "auto"}})` * `collective_rpc("reload_weights")` #20096 * this will explicitly reload weights inplace, without re-initialize the model * Might need to move `process_weights_after_loading` from `load_model` to `load_weights` * Quantized inplace weights loading support: #23014 **Alternative approach** Instead of providing a standalone `update_config` API, we can...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ersion of inplace weights loading in #18745 and #19884. Currently `load_model` will decide itself whether to load model from scratch or reload weighs inplace. Should we give users more control? I've been thinking about...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ce weights loading RFC;rl ### Motivation. We've implemented the initial version of inplace weights loading in #18745 and #19884. Currently `load_model` will decide itself whether to load model from scratch or reload wei...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ve `process_weights_after_loading` from `load_model` to `load_weights` * Quantized inplace weights loading support: #23014 **Alternative approach** Instead of providing a standalone `update_config` API, we can embed the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
