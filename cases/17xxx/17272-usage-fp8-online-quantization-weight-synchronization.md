# vllm-project/vllm#17272: [Usage]: FP8 online quantization weight synchronization

| 字段 | 值 |
| --- | --- |
| Issue | [#17272](https://github.com/vllm-project/vllm/issues/17272) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: FP8 online quantization weight synchronization

### Issue 正文摘录

### Your current environment If we run a vllm instance with ```quantization='fp8'```, how should we update its weight ? I encountered an issue: ``` assert param.size() == loaded_weight.size(), ( [rank10]: AssertionError: Attempted to load weight (torch.Size([3840, 1280])) into parameter (torch.Size([1280, 3840])) ``` this is due to the training models' type is bfloat16. Can we only enable FP8 training if we want to use FP8 inference? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: FP8 online quantization weight synchronization usage;stale ### Your current environment If we run a vllm instance with ```quantization='fp8'```, how should we update its weight ? I encountered an issue: ``` ass...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nto parameter (torch.Size([1280, 3840])) ``` this is due to the training models' type is bfloat16. Can we only enable FP8 training if we want to use FP8 inference? ### How would you like to use vllm I want to run infere...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: FP8 online quantization weight synchronization usage;stale ### Your current environment If we run a vllm instance with ```quantization='fp8'```, how should we update its weight ? I encountered an issue: ``` ass...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
