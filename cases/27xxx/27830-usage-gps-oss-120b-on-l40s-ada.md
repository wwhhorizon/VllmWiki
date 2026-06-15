# vllm-project/vllm#27830: [Usage]: GPS OSS 120b on L40S (Ada)

| 字段 | 值 |
| --- | --- |
| Issue | [#27830](https://github.com/vllm-project/vllm/issues/27830) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: GPS OSS 120b on L40S (Ada)

### Issue 正文摘录

### Your current environment (Just a general question) ### How would you like to use vllm I want to run inference of a GPT OSS 120b with multiple L40S. I read the [docs](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html) as it clearly says it is not natively supported yet. After I had no success with vLLM it worked plug-and-play with Ollama. My question is, if there is any road map where I can see the progress? Or is it even possible to contribute on that problem? Unfortunately I am not familiar with GPUs. However I need to get it running. Any suggestion is highly appreciated. Even a clear description of the problem and what would be required to solve, is a real advantage. Thank you. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: I read the [docs](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html) as it clearly says it is not natively supported yet. After I had no success with vLLM it worked plug-and-play with Ollama. My questi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0b with multiple L40S. I read the [docs](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html) as it clearly says it is not natively supported yet. After I had no success with vLLM it worked plug-and-play...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ou. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tiple L40S. I read the [docs](https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html) as it clearly says it is not natively supported yet. After I had no success with vLLM it worked plug-and-play with Ollam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
