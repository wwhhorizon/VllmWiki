# vllm-project/vllm#12678: [Bug]: V1 engine ignores logits processors and min-p sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#12678](https://github.com/vllm-project/vllm/issues/12678) |
| 状态 | closed |
| 标签 | bug;stale;v1 |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 engine ignores logits processors and min-p sampling

### Issue 正文摘录

### Your current environment **vLLM Version**: 0.7.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug # Issue: V1 engine ignores custom logits processors **and** does not implement min-p sampling **Problem** 1. **Custom logits processors**: In the new V1 engine, specifying a `logits_processor` in `SamplingParams` for `LLM.generate()` has no effect. The code in [`gpu_model_runner.py`](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py) never passes any sampling metadata into `self.model.compute_logits(...)`, so the logits processor is silently ignored. 2. **Min-p**: Similarly, `min_p` (a sampling parameter supported in V0 akin to `top_k` and `top_p`) is not applied at all in V1. The [`sampler.py`](https://github.com/vllm-project/vllm/blob/main/vllm/v1/sample/sampler.py) for the new engine appears to skip it entirely, so it never factors into the final token selection. If those features are not yet supported, consider at least raising a warning or error to avoid silent failures. **Possible Fix for Logits Processor Issue** 1. **Create a new data class** to hold relevant metadata for `self.model.compute_logits(...)`. - Could simply hold request...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ors and min-p sampling bug;stale;v1 ### Your current environment **vLLM Version**: 0.7.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug # Issue: V1 engine ignores custom logits processors **and** does not im...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: V1 engine ignores logits processors and min-p sampling bug;stale;v1 ### Your current environment **vLLM Version**: 0.7.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug # Issue: V1 engine ignores custo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: /blob/main/vllm/v1/worker/gpu_model_runner.py) never passes any sampling metadata into `self.model.compute_logits(...)`, so the logits processor is silently ignored. 2. **Min-p**: Similarly, `min_p` (a sampling paramete...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bug;stale;v1 ### Your current environment **vLLM Version**: 0.7.0 ### Model Input Dumps _No response_ ### 🐛 Describe the bug # Issue: V1 engine ignores custom logits processors **and** does not implement min-p sampling...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
