# vllm-project/vllm#27901: [Feature]: Get confirmation on pending request(s) from vLLM V1 AsyncLLM servers

| 字段 | 值 |
| --- | --- |
| Issue | [#27901](https://github.com/vllm-project/vllm/issues/27901) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Get confirmation on pending request(s) from vLLM V1 AsyncLLM servers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi team, We are using V1 AsyncLLM servers to support partial rollout in the colocated Async RL training. In this use case, we load vllm servers with generate requests and keep collecting completed trajectories. When we have enough trajectories, we will send out signals to abort all ongoing requests in vLLM servers, forcing all requests to return the full or partial generated token ids. After the request abort process, we will put the vllm servers to sleep so that GPU resources can be used by training stage. While partial token return is already supported in https://github.com/vllm-project/vllm/issues/22197, we noticed one issue with current API is that as `abort()` being async, it immediately returns without guarantees all TP works and DP ranks have completed all request abort operations. This leads to race condition where we are attempting to put servers to sleep while abort requests are still being processed in some workers, causing CUDA illegal memory access errors. Locally, we implemented a solution exposing scheduler unfinished request count in the `vllm/v1/engine/core.py`: ``` def get_num_unfinished_requests(self) -> int: return self.s...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: while abort requests are still being processed in some workers, causing CUDA illegal memory access errors. Locally, we implemented a solution exposing scheduler unfinished request count in the `vllm/v1/engine/core.py`:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Get confirmation on pending request(s) from vLLM V1 AsyncLLM servers feature request;stale ### 🚀 The feature, motivation and pitch Hi team, We are using V1 AsyncLLM servers to support partial rollout in the c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: will send out signals to abort all ongoing requests in vLLM servers, forcing all requests to return the full or partial generated token ids. After the request abort process, we will put the vllm servers to sleep so that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ]) ``` We did not see there is a current API available to expose this information yet. Opening an issue asking for some suggestion here, if there a better approach we can support our use case here? If this approach work...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;scheduler_memory cuda;operator race_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
