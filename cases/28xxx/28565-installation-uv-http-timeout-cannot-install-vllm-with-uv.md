# vllm-project/vllm#28565: [Installation]: UV_HTTP_TIMEOUT cannot install vllm with uv

| 字段 | 值 |
| --- | --- |
| Issue | [#28565](https://github.com/vllm-project/vllm/issues/28565) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: UV_HTTP_TIMEOUT cannot install vllm with uv

### Issue 正文摘录

### Your current environment Ubuntu 24.04.2 LTS ``` ~/project/vllm uv pip install vllm --torch-backend=auto Resolved 142 packages in 1.54s × Failed to download `torch==2.8.0+cu129` ├─▶ Failed to extract archive: torch-2.8.0+cu129-cp312-cp312-manylinux_2_28_x86_64.whl ├─▶ I/O operation failed during extraction ╰─▶ Failed to download distribution due to network timeout. Try increasing UV_HTTP_TIMEOUT (current value: 30s). help: `torch` (v2.8.0+cu129) was included because `vllm` (v0.11.0) depends on `torch` ``` ### How you are installing vllm ```sh uv pip install vllm --torch-backend=auto ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ment Ubuntu 24.04.2 LTS ``` ~/project/vllm uv pip install vllm --torch-backend=auto Resolved 142 packages in 1.54s × Failed to download `torch==2.8.0+cu129` ├─▶ Failed to extract archive: torch-2.8.0+cu129-cp312-cp312-m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: UV_HTTP_TIMEOUT cannot install vllm with uv installation;stale ### Your current environment Ubuntu 24.04.2 LTS ``` ~/project/vllm uv pip install vllm --torch-backend=auto Resolved 142 packages in 1.54s
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .54s × Failed to download `torch==2.8.0+cu129` ├─▶ Failed to extract archive: torch-2.8.0+cu129-cp312-cp312-manylinux_2_28_x86_64.whl ├─▶ I/O operation failed during extraction ╰─▶ Failed to download distribution due to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: UV_HTTP_TIMEOUT cannot install vllm with uv installation;stale ### Your current environment Ubuntu 24.04.2 LTS ``` ~/project/vllm uv pip install vllm --torch-backend=auto Resolved 142 packages in 1.54s ×...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
