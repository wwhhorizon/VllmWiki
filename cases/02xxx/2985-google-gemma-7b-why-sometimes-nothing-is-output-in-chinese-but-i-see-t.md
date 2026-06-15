# vllm-project/vllm#2985: google/gemma-7b：Why sometimes nothing is output in Chinese, but I see that the official demo can output it.

| 字段 | 值 |
| --- | --- |
| Issue | [#2985](https://github.com/vllm-project/vllm/issues/2985) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> google/gemma-7b：Why sometimes nothing is output in Chinese, but I see that the official demo can output it.

### Issue 正文摘录

``` curl --location 'http://ip/v1/chat/completions' \ --header 'authorization: [secure]' \ --header 'Content-Type: application/json' \ --data '{ "model":"google/gemma-7b", "messages":[ { "role":"user", "content":"讲个笑话" } ], "temperature":0.1, "stream":true, "stop":[" "," "], "skip_special_tokens":false }' data: {"id":"cmpl-09824a3e1b9d4674aac1d11c14a42317","object":"chat.completion.chunk","created":2540668,"model":"google/gemma-7b","choices":[{"index":0,"delta":{"role":"assistant"},"finish_reason":null}]} data: {"id":"cmpl-09824a3e1b9d4674aac1d11c14a42317","object":"chat.completion.chunk","created":2540668,"model":"google/gemma-7b","choices":[{"index":0,"delta":{"content":"<"},"finish_reason":null}]} data: {"id":"cmpl-09824a3e1b9d4674aac1d11c14a42317","object":"chat.completion.chunk","created":2540668,"model":"google/gemma-7b","choices":[{"index":0,"delta":{"content":"|"},"finish_reason":null}]} data: {"id":"cmpl-09824a3e1b9d4674aac1d11c14a42317","object":"chat.completion.chunk","created":2540668,"model":"google/gemma-7b","choices":[{"index":0,"delta":{"content":"im"},"finish_reason":null}]} data: {"id":"cmpl-09824a3e1b9d4674aac1d11c14a42317","object":"chat.completion.chunk","crea...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: google/gemma-7b：Why sometimes nothing is output in Chinese, but I see that the official demo can output it. ``` curl --location 'http://ip/v1/chat/completions' \ --header 'authorization: [secure]' \ --header 'Content-Ty...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ma-7b：Why sometimes nothing is output in Chinese, but I see that the official demo can output it. ``` curl --location 'http://ip/v1/chat/completions' \ --header 'authorization: [secure]' \ --header 'Content-Type: applic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .1, "stream":true, "stop":[" "," "], "skip_special_tokens":false }' data: {"id":"cmpl-09824a3e1b9d4674aac1d11c14a42317","object":"chat.completion.chunk","created":2540668,"model":"google/gemma-7b","choices":[{"index":0,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: google/gemma-7b：Why sometimes nothing is output in Chinese, but I see that the official demo can output it. ``` curl --location 'http://ip/v1/chat/completions' \ --header 'authorization: [secure]' \ --header 'Content-Ty...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
