# vllm-project/vllm#4338: [Bug]: vllm 0.4.1 broke pip 517 compatability

| 字段 | 值 |
| --- | --- |
| Issue | [#4338](https://github.com/vllm-project/vllm/issues/4338) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.4.1 broke pip 517 compatability

### Issue 正文摘录

### 🐛 Describe the bug vllm now attempts to download a package from github on pip install https://github.com/vllm-project/vllm-nccl/releases/download/v0.1.0/cu12-libnccl.so.2.18.1 This breaks pip 517 compatability. When I install this in an environment without access to the wider internet (but with a pypi proxy), I get the following error ``` Downloading nccl package from https://github.com/vllm-project/vllm-nccl/releases/download/v0.1.0/cu12-libnccl.so.2.18.1 Failed to download nccl package from https://github.com/vllm-project/vllm-nccl/releases/download/v0.1.0/cu12-libnccl.so.2.18.1 ... Note: This error originates from the build backend, and is likely not a problem with poetry but with vllm-nccl-cu12 (2.18.1.0.3.0) not supporting PEP 517 builds. You can verify this by running 'pip wheel --no-cache-dir --use-pep517 "vllm-nccl-cu12 (==2.18.1.0.3.0)"'. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ribe the bug vllm now attempts to download a package from github on pip install https://github.com/vllm-project/vllm-nccl/releases/download/v0.1.0/cu12-libnccl.so.2.18.1 This breaks pip 517 compatability. When I install...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: u12-libnccl.so.2.18.1 ... Note: This error originates from the build backend, and is likely not a problem with poetry but with vllm-nccl-cu12 (2.18.1.0.3.0) not supporting PEP 517 builds. You can verify this by running...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
