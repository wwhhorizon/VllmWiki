# vllm-project/vllm#8711: [Bug]: 4208 CPU  vllm 0.6.0  启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果

| 字段 | 值 |
| --- | --- |
| Issue | [#8711](https://github.com/vllm-project/vllm/issues/8711) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 4208 CPU  vllm 0.6.0  启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果

### Issue 正文摘录

### Your current environment [Bug]: 4208 CPU vllm 0.6.0 启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果 ### Model Input Dumps [Bug]: 4208 CPU vllm ![捕获](https://github.com/user-attachments/assets/f3962f9e-0ce5-4d67-8677-f303813ee215) 0.6.0 启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果 ### 🐛 Describe the bug [Bug]: 4208 CPU vllm 0.6.0 启动qwen-vl-7b ,报下面图片中的异 ![捕获](https://github.com/user-attachments/assets/a05cab71-3f5e-4f11-a530-d6bb67be5556) 常，模型开始可以正常输出，调用多次后，无返回结果 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 4208 CPU vllm 0.6.0 启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果 bug;stale ### Your current environment [Bug]: 4208 CPU vllm 0.6.0 启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果 ### Model Input Dumps [Bug]: 420...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 回结果 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 4208 CPU vllm 0.6.0 启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果 bug;stale ### Your current environment [Bug]: 4208 CPU vllm 0.6.0 启动qwen-vl-7b ,报下面图片中的异常，模型开始可以正常输出，调用多次后，无返回结果 ### Model Input Dumps [Bug]: 4208 CPU v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
