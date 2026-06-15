# vllm-project/vllm#7847: [Misc]: How can I pass `system_prompt` on initialization!?

| 字段 | 值 |
| --- | --- |
| Issue | [#7847](https://github.com/vllm-project/vllm/issues/7847) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How can I pass `system_prompt` on initialization!?

### Issue 正文摘录

### Anything you want to discuss about vllm. So, I run the model using the following Docker command: ``` docker run -d \ --name vllm-container \ -p 8000:8000 \ --shm-size 2G \ -e HF_TOKEN=hf_\ vllm/vllm-openai:v0.5.2 \ --model=name \ --max-model-len=3072 ``` How can I pass the system_prompt here? It's a very long text (~2000 characters). We can pass it with each API request ([4497](https://github.com/vllm-project/vllm/issues/4497))!, but I feel that's not very efficient! So, I'm thinking of adding this in the startup command itself, but I can't find it in the docs. I prefer adding it through a file, like --system_prompt=system_prompt.txt. Is something like this possible? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: you want to discuss about vllm. So, I run the model using the following Docker command: ``` docker run -d \ --name vllm-container \ -p 8000:8000 \ --shm-size 2G \ -e HF_TOKEN=hf_\ vllm/vllm-openai:v0.5.2 \ --model=name...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tion!? stale ### Anything you want to discuss about vllm. So, I run the model using the following Docker command: ``` docker run -d \ --name vllm-container \ -p 8000:8000 \ --shm-size 2G \ -e HF_TOKEN=hf_\ vllm/vllm-ope...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: How can I pass `system_prompt` on initialization!? stale ### Anything you want to discuss about vllm. So, I run the model using the following Docker command: ``` docker run -d \ --name vllm-container \ -p 8000:8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
