# vllm-project/vllm#2812: Failed on pure ipv6 environment 

| 字段 | 值 |
| --- | --- |
| Issue | [#2812](https://github.com/vllm-project/vllm/issues/2812) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed on pure ipv6 environment 

### Issue 正文摘录

Hello, I am using python3.9 with a pure ipv6 environment. However it seems to break while get_open_port: def get_open_port() -> int: with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: s.bind(("8.8.8.8", 80)) return s.getsockname()[1] This return a unreachable error and stops. BTW: It seems I was able to resolve the problem by fixing it to s.bind("127.0.0.1", 80). I am not sure if this is the best fix.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
