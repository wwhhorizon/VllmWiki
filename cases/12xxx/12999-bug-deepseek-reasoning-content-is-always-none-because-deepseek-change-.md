# vllm-project/vllm#12999: [Bug]: deepseek reasoning_content is always None , because deepseek change the chat template

| 字段 | 值 |
| --- | --- |
| Issue | [#12999](https://github.com/vllm-project/vllm/issues/12999) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deepseek reasoning_content is always None , because deepseek change the chat template

### Issue 正文摘录

### Your current environment https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B/commit/3865e12a1eb7cbd641ab3f9dfc28c588c6b0c1e9 ![Image](https://github.com/user-attachments/assets/c2965bc5-8ad8-4333-a4a1-8496c9fb379e) vllm version V0.7.2 input : hello output like ``` Alright, the user just said "hello." That's a friendly greeting. I should respond in a warm and welcoming manner. Maybe say something like, "Hello! How can I assist you today?" That way, I'm open to whatever they need help with. Hello! How can I assist you today? ``` just has '\ ' no '\ ' , so reasoning_content is None ### 🐛 Describe the bug vllm V0.7.2 model https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pseek change the chat template bug ### Your current environment https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B/commit/3865e12a1eb7cbd641ab3f9dfc28c588c6b0c1e9 ![Image](https://github.com/user-attachment...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: .com/user-attachments/assets/c2965bc5-8ad8-4333-a4a1-8496c9fb379e) vllm version V0.7.2 input : hello output like ``` Alright, the user just said "hello." That's a friendly greeting. I should respond in a warm and welcom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 32B ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
