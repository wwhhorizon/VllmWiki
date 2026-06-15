# vllm-project/vllm#9840: [Bug]: api_server.py: error: unrecognized arguments: --task embedding

| 字段 | 值 |
| --- | --- |
| Issue | [#9840](https://github.com/vllm-project/vllm/issues/9840) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: api_server.py: error: unrecognized arguments: --task embedding

### Issue 正文摘录

### Your current environment I'm running in a Kubernetes environment vllm docker image vllm/vllm-openai:latest . The latest version is supposed to support --task embedding flag. https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html ### Model Input Dumps _No response_ ### 🐛 Describe the bug I start the server with the following command: `python3 -m vllm.entrypoints.openai.api_server ` and arguments: `--served-model-name BAAI/bge-m3 --enforce-eager --task embedding` . The pod fails to run. **Error message:** `api_server.py: error: unrecognized arguments: --task embedding ` Any suggestions please? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: # Your current environment I'm running in a Kubernetes environment vllm docker image vllm/vllm-openai:latest . The latest version is supposed to support --task embedding flag. https://docs.vllm.ai/en/latest/serving/open...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tps://docs.vllm.ai/en/latest/serving/openai_compatible_server.html ### Model Input Dumps _No response_ ### 🐛 Describe the bug I start the server with the following command: `python3 -m vllm.entrypoints.openai.api_server...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: running in a Kubernetes environment vllm docker image vllm/vllm-openai:latest . The latest version is supposed to support --task embedding flag. https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html ### M...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
