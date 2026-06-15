# vllm-project/vllm#16887: [Bug]: tool_choice: "required" does not work for mistral

| 字段 | 值 |
| --- | --- |
| Issue | [#16887](https://github.com/vllm-project/vllm/issues/16887) |
| 状态 | closed |
| 标签 | bug;tool-calling |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_choice: "required" does not work for mistral

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using tool calling with mistral-small-24 when I set the `"tool_choice": "auto"` it works fine, however when I set it to `required` I get the error above, based on my research mistral models do not support `required` they use `any` instead. Some how we need to adapt the `required` to `any` for mistral model. Currently when I set the `"tool_choice": "any"` I get a 500 error. ``` INFO: 10.89.212.1:44926 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ``` https://docs.mistral.ai/capabilities/function_calling/ My docker command flags config: ``` --model stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --max-model-len 32768 --task generate --tensor-parallel-size 2 --tool-call-parser mistral --enable-auto-tool-choice --tokenizer-mode mistral --served-model-name mistral-small-24b ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ironment ### 🐛 Describe the bug I'm using tool calling with mistral-small-24 when I set the `"tool_choice": "auto"` it works fine, however when I set it to `required` I get the error above, based on my research mistral...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: set it to `required` I get the error above, based on my research mistral models do not support `required` they use `any` instead. Some how we need to adapt the `required` to `any` for mistral model. Currently when I set...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er Error ``` https://docs.mistral.ai/capabilities/function_calling/ My docker command flags config: ``` --model stelterlab/Mistral-Small-24B-Instruct-2501-AWQ --max-model-len 32768 --task generate --tensor-parallel-size...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
