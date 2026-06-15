# vllm-project/vllm#9656: [Misc]: huggingface_hub.errors.HFValidationError using LLama3.1-405b

| 字段 | 值 |
| --- | --- |
| Issue | [#9656](https://github.com/vllm-project/vllm/issues/9656) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: huggingface_hub.errors.HFValidationError using LLama3.1-405b

### Issue 正文摘录

### Anything you want to discuss about vllm. Using vllm with LLama3.1-405b, I get the following error: `huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '****/models/Llama-3.1_405B-Instruct'. Use `repo_type` argument if needed. ` The dataset is downloaded from official repo: `https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct` Could you help me to define the problem? Thanks. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Misc]: huggingface_hub.errors.HFValidationError using LLama3.1-405b ### Anything you want to discuss about vllm. Using vllm with LLama3.1-405b, I get the following error: `huggingface_hub.errors.HFValidationError: Repo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Use `repo_type` argument if needed. ` The dataset is downloaded from official repo: `https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct` Could you help me to define the problem? Thanks. ### Before submitting a ne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
