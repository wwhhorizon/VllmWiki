# vllm-project/vllm#42407: [Doc]: which version of vllm supports codex ?

| 字段 | 值 |
| --- | --- |
| Issue | [#42407](https://github.com/vllm-project/vllm/issues/42407) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: which version of vllm supports codex ?

### Issue 正文摘录

### 📚 The doc issue I saw in the documentation that [vLLM](https://docs.vllm.ai/en/latest/serving/integrations/codex) supports [Codex CLI](https://github.com/openai/codex). My environment: codex-cli 0.130.0 vllm 0.19.1 However, when I send a message using Codex, I encounter the following error: {"error":{"message":"Unexpected message role.","type":"BadRequestError","param":null,"code":400}} I’m wondering which version of vLLM officially supports Codex CLI compatibility, especially for the /v1/responses API and the developer role messages. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Doc]: which version of vllm supports codex ? documentation ### 📚 The doc issue I saw in the documentation that [vLLM](https://docs.vllm.ai/en/latest/serving/integrations/codex) supports [Codex CLI](https://github.com/o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lowing error: {"error":{"message":"Unexpected message role.","type":"BadRequestError","param":null,"code":400}} I’m wondering which version of vLLM officially supports Codex CLI compatibility, especially for the /v1/res...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: issue I saw in the documentation that [vLLM](https://docs.vllm.ai/en/latest/serving/integrations/codex) supports [Codex CLI](https://github.com/openai/codex). My environment: codex-cli 0.130.0 vllm 0.19.1 However, when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
