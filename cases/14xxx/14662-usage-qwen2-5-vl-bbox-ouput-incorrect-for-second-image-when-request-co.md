# vllm-project/vllm#14662: [Usage]: Qwen2.5-VL - BBOX Ouput Incorrect for Second Image when Request Contains 2 Images

| 字段 | 值 |
| --- | --- |
| Issue | [#14662](https://github.com/vllm-project/vllm/issues/14662) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen2.5-VL - BBOX Ouput Incorrect for Second Image when Request Contains 2 Images

### Issue 正文摘录

### Your current environment Vllm 0.7.3 Docker ### How would you like to use vllm BBOX Ouput Incorrect for Second Image when Request Contains 2 Images. I tried request with 2 images and describes an object in the 1st one, then asked the mode to find out the same object in the 2nd image. I aksed the model to ouput the object's bbox in both images. The Bounding box values for the second image does not match what was in the image. I'm unsure if this is the problem with the model or with vllm setup. Please help with it if you have any ideas. Appreciated. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t Contains 2 Images usage;stale ### Your current environment Vllm 0.7.3 Docker ### How would you like to use vllm BBOX Ouput Incorrect for Second Image when Request Contains 2 Images. I tried request with 2 images and d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Qwen2.5-VL - BBOX Ouput Incorrect for Second Image when Request Contains 2 Images usage;stale ### Your current environment Vllm 0.7.3 Docker ### How would you like to use vllm BBOX Ouput Incorrect for Second Im...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Qwen2.5-VL - BBOX Ouput Incorrect for Second Image when Request Contains 2 Images usage;stale ### Your current environment Vllm 0.7.3 Docker ### How would you like to use vllm BBOX Ouput Incorrect for Second Im...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
