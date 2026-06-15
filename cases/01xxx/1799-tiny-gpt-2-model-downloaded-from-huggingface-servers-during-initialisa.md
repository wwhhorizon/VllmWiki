# vllm-project/vllm#1799: Tiny GPT-2 model downloaded from HuggingFace servers during initialisation

| 字段 | 值 |
| --- | --- |
| Issue | [#1799](https://github.com/vllm-project/vllm/issues/1799) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tiny GPT-2 model downloaded from HuggingFace servers during initialisation

### Issue 正文摘录

Hi, (I use vLLM via LangChain, so I hope I'm looking for answers in the right place.) During initialisation of vLLM when running various models, such as Mistral 7B, vLLM downloads some kind of fake tiny GPT-2 model (about 3MB size on disk) from HuggingFace's servers. This is not a problem in development environment, but our production environment doesn't have access to HF servers (and we cannot change this behaviour, the data we work with being too sensitive to tolerate access to internet) and so it hangs during init, and just restarts the process forever after timeouts. What is this GPT-2 model? What can I do to prevent vLLM from trying to download it? Thanks in advance for your help!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Tiny GPT-2 model downloaded from HuggingFace servers during initialisation Hi, (I use vLLM via LangChain, so I hope I'm looking for answers in the right place.) During initialisation of vLLM when running various models,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
