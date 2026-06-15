# vllm-project/vllm#23352: [Installation]: Failure to install dependencies for dev environment due to incompatible pydantic version

| 字段 | 值 |
| --- | --- |
| Issue | [#23352](https://github.com/vllm-project/vllm/issues/23352) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Failure to install dependencies for dev environment due to incompatible pydantic version

### Issue 正文摘录

### Your current environment Failed to install Python dependencies for dev environment because pydantic version is incompatible for `openai-harmony>0.0.3` package. It requires pydantic version `2.11.7`. Failure as follows: ```command $ uv pip install -r requirements/common.txt -r requirements/dev.txt --torch-backend=auto × No solution found when resolving dependencies: ╰─▶ Because openai-harmony>=0.0.3 depends on pydantic>=2.11.7 and only the following versions of openai-harmony are available: openai-harmony =0.0.3 depends on pydantic>=2.11.7. And because you require openai-harmony>=0.0.3 and pydantic==2.11.5, we can conclude that your requirements are unsatisfiable. (vllm) root@marty-gpu-dev-l40s:/data/dev/github.com/vllm-project/vllm# vim requirements/common.txt (vllm) root@marty-gpu-dev-l40s:/data/dev/github.com/vllm-project/vllm# vim requirements/common.txt (vllm) root@marty-gpu-dev-l40s:/data/dev/github.com/vllm-project/vllm# uv pip install -r requirements/common.txt -r requirements/dev.txt --torch-backend=auto × No solution found when resolving dependencies: ╰─▶ Because you require pydantic>=2.11.7 and pydantic==2.11.5, we can conclude that your requirements are unsatisfiabl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Failure to install dependencies for dev environment due to incompatible pydantic version installation ### Your current environment Failed to install Python dependencies for dev environment because pydanti
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: v pip install -r requirements/common.txt -r requirements/dev.txt --torch-backend=auto × No solution found when resolving dependencies: ╰─▶ Because openai-harmony>=0.0.3 depends on pydantic>=2.11.7 and only the following...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
