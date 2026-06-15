# vllm-project/vllm#10408: [Bug]: 使用vllm和transformer部署Qwen2vl，同一张图片输出结果不一致

| 字段 | 值 |
| --- | --- |
| Issue | [#10408](https://github.com/vllm-project/vllm/issues/10408) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 使用vllm和transformer部署Qwen2vl，同一张图片输出结果不一致

### Issue 正文摘录

### Your current environment ### Model Input Dumps transformer=4.45.0.dev0 vllm=0.6.1.post2+cu118 torch=2.4.1+cu118 flash-attn=2.6.3 ### 🐛 Describe the bug 使用Qwen2-VL-7B-Instruct模型做ocr信息抽取任务，微调后使用同样的权重，vllm和transformer部署的服务同一张图片输出结果不一致。transformer能够正确输出的文本信息，使用vllm会出现叠字、信息提取不到的情况，具体表现为： transformer输出：{“公司名称”：“xxx布艺有限公司”，“支付方式”：“银行承兑汇票”} vllm输出：{“公司名称”：“xxx布艺艺有限公司”，“支付方式”：NaN} 尝试调整temperature、repetition_penalty等参数，vllm总无法完全去除叠字的问题，而且还会影响别的字段的结果。 transformer的调用代码参考了：https://github.com/QwenLM/Qwen2-VL/blob/main/README.md#using---transformers-to-chat vllm的调用代码参考了：https://github.com/QwenLM/Qwen2-VL/blob/main/README.md#inference-locally 请问有大佬遇到过同样的情况吗？是如何解决的，感谢！ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 使用vllm和transformer部署Qwen2vl，同一张图片输出结果不一致 bug;stale ### Your current environment ### Model Input Dumps transformer=4.45.0.dev0 vllm=0.6.1.post2+cu118 torch=2.4.1+cu118 flash-attn=2.6.3 ### 🐛 Describe the bug 使用Qwe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 感谢！ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 使用vllm和transformer部署Qwen2vl，同一张图片输出结果不一致 bug;stale ### Your current environment ### Model Input Dumps transformer=4.45.0.dev0 vllm=0.6.1.post2+cu118 torch=2.4.1+cu118 flash-attn=2.6.3 ### 🐛 Describe the bug 使用Qwe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
