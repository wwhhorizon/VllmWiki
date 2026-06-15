# vllm-project/vllm#5690: [Installation]: poetry add vllm not working on my Mac -- xformers (0.0.26.post1) not supporting PEP 517 builds.

| 字段 | 值 |
| --- | --- |
| Issue | [#5690](https://github.com/vllm-project/vllm/issues/5690) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: poetry add vllm not working on my Mac -- xformers (0.0.26.post1) not supporting PEP 517 builds.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ``` poetry add vllm ``` Can someone tell me what versions of ray and torch are compatible to add vlllm via poetry? ``` - Installing vllm-flash-attn (2.5.9): Failed - Unable to find installation candidates for ray (2.24.0) Note: This error originates from the build backend, and is likely not a problem with poetry but with xformers (0.0.26.post1) not supporting PEP 517 builds. You can verify this by running 'pip wheel --no-cache-dir --use-pep517 "xformers (==0.0.26.post1)"' ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: poetry add vllm not working on my Mac -- xformers (0.0.26.post1) not supporting PEP 517 builds. installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How y
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n candidates for ray (2.24.0) Note: This error originates from the build backend, and is likely not a problem with poetry but with xformers (0.0.26.post1) not supporting PEP 517 builds. You can verify this by running 'p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: c -- xformers (0.0.26.post1) not supporting PEP 517 builds. installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ``` poetry add vllm ``` Can s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
