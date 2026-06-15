# vllm-project/vllm#13817: [Bug]: Qwen2.5-VL-3B Returning Series of !!! for Specific Image when "dtype" Set to "float16"

| 字段 | 值 |
| --- | --- |
| Issue | [#13817](https://github.com/vllm-project/vllm/issues/13817) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL-3B Returning Series of !!! for Specific Image when "dtype" Set to "float16"

### Issue 正文摘录

### Your current environment Vllm-openai docker image 0.7.3 ### 🐛 Describe the bug Hi and I'm testing Qwen2.5-VL-3B-Instruct using vllm-openai docker image. I tried both v0.7.2 & v0.7.3 and got error using this specific image with both based64/url input. ![Image](https://github.com/user-attachments/assets/13d09edd-f7fe-4432-a690-711e23367251) I tested and confirmed this would only happen if I set `--dtype half/float16` and using this image (captured using Snipaste) no matter requesting with base64 or url. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Qwen2.5-VL-3B Returning Series of !!! for Specific Image when "dtype" Set to "float16" bug ### Your current environment Vllm-openai docker image 0.7.3 ### 🐛 Describe the bug Hi and I'm testing Qwen2.5-VL-3B-Instr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Qwen2.5-VL-3B Returning Series of !!! for Specific Image when "dtype" Set to "float16" bug ### Your current environment Vllm-openai docker image 0.7.3 ### 🐛 Describe the bug Hi and I'm testing Qwen2.5-VL-3B-Instr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen2.5-VL-3B Returning Series of !!! for Specific Image when "dtype" Set to "float16" bug ### Your current environment Vllm-openai docker image 0.7.3 ### 🐛 Describe the bug Hi and I'm testing Qwen2.5-VL-3B-Instr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e half/float16` and using this image (captured using Snipaste) no matter requesting with base64 or url. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
