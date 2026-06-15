# vllm-project/vllm#10391: [Feature]: Enhance offline_inference.py with Configurable Parameters for Greater Flexibility

| 字段 | 值 |
| --- | --- |
| Issue | [#10391](https://github.com/vllm-project/vllm/issues/10391) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enhance offline_inference.py with Configurable Parameters for Greater Flexibility

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current `offline_inference.py` functionality is relatively basic, and developers often need to manually modify the script to meet their specific needs. For example, tasks such as loading models from local paths, running multi-GPU inference, applying specific quantization algorithms, configure LLM engine parameters, or customizing inputs (e.g., batch size, input length, output length, sampling parameters, etc.) require manual intervention. We can enhance the functionality of` offline_inference.py` to support these features while keeping the default behavior unchanged. By introducing configurable parameters, users will be able to adapt the script to their requirements without having to manually modify the code. This enhancement would improve usability and flexibility for a wider range of scenarios. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Enhance offline_inference.py with Configurable Parameters for Greater Flexibility feature request ### 🚀 The feature, motivation and pitch The current `offline_inference.py` functionality is relatively basic,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and developers often need to manually modify the script to meet their specific needs. For example, tasks such as loading models from local paths, running multi-GPU inference, applying specific quantization algorithms, c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: models from local paths, running multi-GPU inference, applying specific quantization algorithms, configure LLM engine parameters, or customizing inputs (e.g., batch size, input length, output length, sampling parameters...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nference.py with Configurable Parameters for Greater Flexibility feature request ### 🚀 The feature, motivation and pitch The current `offline_inference.py` functionality is relatively basic, and developers often need to...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
