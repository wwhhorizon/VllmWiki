# vllm-project/vllm#19603: [Doc]: Improve CPU documentation for ARM

| 字段 | 值 |
| --- | --- |
| Issue | [#19603](https://github.com/vllm-project/vllm/issues/19603) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Improve CPU documentation for ARM

### Issue 正文摘录

### 📚 The doc issue At the moment, vLLM supports a variety of GPUs, some NPUs/TPUs, and (at the very least) x86 and ARM CPUs. At the moment, however, the documentation is very sparse for ARM CPUs, other than that it *can* be used. As a matter of fact, not including the API docs, I can only find [this one page](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html?h=arm) which mentions it. Notably missing is any mention of ARM in the [Supported Hardware](https://docs.vllm.ai/en/latest/features/quantization/supported_hardware.html) page for quantization. ### Suggest a potential alternative/fix It would be helpful to have at least some indication of what is and isn't supported on ARM CPUs. I would be happy to contribute this myself, but I'm not sure of the best way to determine compatibility. Would it make sense to simply run a small model of every possible quantization format to see what happens? Or is there something a bit more elegant? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: best way to determine compatibility. Would it make sense to simply run a small model of every possible quantization format to see what happens? Or is there something a bit more elegant? ### Before submitting a new issue...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ay to determine compatibility. Would it make sense to simply run a small model of every possible quantization format to see what happens? Or is there something a bit more elegant? ### Before submitting a new issue... -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: only find [this one page](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html?h=arm) which mentions it. Notably missing is any mention of ARM in the [Supported Hardware](https://docs.vllm.ai/en/latest/f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ARM in the [Supported Hardware](https://docs.vllm.ai/en/latest/features/quantization/supported_hardware.html) page for quantization. ### Suggest a potential alternative/fix It would be helpful to have at least some indi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Improve CPU documentation for ARM documentation;stale ### 📚 The doc issue At the moment, vLLM supports a variety of GPUs, some NPUs/TPUs, and (at the very least) x86 and ARM CPUs. At the moment, however, the docu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
