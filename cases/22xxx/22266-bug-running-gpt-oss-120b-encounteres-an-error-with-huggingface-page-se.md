# vllm-project/vllm#22266: [Bug]: Running gpt-oss-120b encounteres an error with huggingface page setup

| 字段 | 值 |
| --- | --- |
| Issue | [#22266](https://github.com/vllm-project/vllm/issues/22266) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Running gpt-oss-120b encounteres an error with huggingface page setup

### Issue 正文摘录

### Your current environment [full_error.txt](https://github.com/user-attachments/files/21604484/error.txt) ### 🐛 Describe the bug I tried to trun [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b#vllm) as described in huggingface. ```bash uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ --index-strategy unsafe-best-match vllm serve openai/gpt-oss-120b ``` and got an error. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: o/openai/gpt-oss-120b#vllm) as described in huggingface. ```bash uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Running gpt-oss-120b encounteres an error with huggingface page setup bug;stale ### Your current environment [full_error.txt](https://github.com/user-attachments/files/21604484/error.txt) ### 🐛 Describe the bug I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: unning gpt-oss-120b encounteres an error with huggingface page setup bug;stale ### Your current environment [full_error.txt](https://github.com/user-attachments/files/21604484/error.txt) ### 🐛 Describe the bug I tried t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
