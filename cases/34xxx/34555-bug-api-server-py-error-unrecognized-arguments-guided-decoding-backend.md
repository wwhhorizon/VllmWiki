# vllm-project/vllm#34555: [BUG]: api_server.py: error: unrecognized arguments: --guided-decoding-backend

| 字段 | 值 |
| --- | --- |
| Issue | [#34555](https://github.com/vllm-project/vllm/issues/34555) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG]: api_server.py: error: unrecognized arguments: --guided-decoding-backend

### Issue 正文摘录

### Your current environment When starting up the nightly openai docker image with engine arg --guided-decoding-backend, I get this: api_server.py: error: unrecognized arguments: --guided-decoding-backend Any ideas? Is this arg deprecated in nightly? ### How would you like to use vllm I'd like to continue using --guided-decoding-backend arg.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [BUG]: api_server.py: error: unrecognized arguments: --guided-decoding-backend usage ### Your current environment When starting up the nightly openai docker image with engine arg --guided-decoding-backend, I get this: a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: usage ### Your current environment When starting up the nightly openai docker image with engine arg --guided-decoding-backend, I get this: api_server.py: error: unrecognized arguments: --guided-decoding-backend Any idea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
