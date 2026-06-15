# vllm-project/vllm#1660: Stuck loading model

| 字段 | 值 |
| --- | --- |
| Issue | [#1660](https://github.com/vllm-project/vllm/issues/1660) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stuck loading model

### Issue 正文摘录

When I boot the API server: `python3 -m vllm.entrypoints.openai.api_server --port 9999 --dtype half --trust-remote-code --host 127.0.0.1 ` The API spins up in 10 seconds. However when I download a model or load one locally: `python3 -m vllm.entrypoints.openai.api_server --port 9999 --model TheBloke/Mistral-7B-Instruct-v0.1-AWQ -q awq --dtype half --trust-remote-code --host 127.0.0.1 ` My PC slows down and loading takes forever. I'm using a 3090 and WSL. What could be the issue here?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: PI server: `python3 -m vllm.entrypoints.openai.api_server --port 9999 --dtype half --trust-remote-code --host 127.0.0.1 ` The API spins up in 10 seconds. However when I download a model or load one locally: `python3 -m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Stuck loading model When I boot the API server: `python3 -m vllm.entrypoints.openai.api_server --port 9999 --dtype half --trust-remote-code --host 127.0.0.1 ` The API spins up in 10 seconds. However when I download a mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
