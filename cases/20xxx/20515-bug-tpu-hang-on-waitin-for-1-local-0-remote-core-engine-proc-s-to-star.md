# vllm-project/vllm#20515: [Bug]: TPU Hang on "Waitin for 1 local, 0 remote core engine proc(s) to start.

| 字段 | 值 |
| --- | --- |
| Issue | [#20515](https://github.com/vllm-project/vllm/issues/20515) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TPU Hang on "Waitin for 1 local, 0 remote core engine proc(s) to start.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Model serving hangs when simply trying to serve `meta-llama/Meta-Llama-3.1-8B-Instruct` in a multihost environment (on a v6e-32). This usually doesn't happen if the node were a single-VM node (like v6e-4). This only happens when trying to serve something on multi-host. I have a ray cluster with just a v6e-32. Code: ``` import ray from vllm import LLM @ray.remote def generate_text(): llm = LLM(model="meta-llama/Meta-Llama-3.1-8B-Instruct", tensor_parallel_size=1, max_model_len=1024, distributed_executor_backend="ray", enforce_eager=True) print("Model loaded") if __name__ == "__main__": ray.get(generate_text.remote()) ``` I also turned on `VLLM_TRACE_FUNCTION=1` to see the trace files and it seems like there may be some issues with initializing the distributed environment based on the last couple lines but I'm not sure yet. Any help on this would be great! [vllm_logs.txt](https://github.com/user-attachments/files/21081629/vllm_logs.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.a...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tart. bug;stale ### Your current environment ### 🐛 Describe the bug Model serving hangs when simply trying to serve `meta-llama/Meta-Llama-3.1-8B-Instruct` in a multihost environment (on a v6e-32). This usually doesn't...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: =1, max_model_len=1024, distributed_executor_backend="ray", enforce_eager=True) print("Model loaded") if __name__ == "__main__": ray.get(generate_text.remote()) ``` I also turned on `VLLM_TRACE_FUNCTION=1` to see the tr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: thing on multi-host. I have a ray cluster with just a v6e-32. Code: ``` import ray from vllm import LLM @ray.remote def generate_text(): llm = LLM(model="meta-llama/Meta-Llama-3.1-8B-Instruct", tensor_parallel_size=1, m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Hang on "Waitin for 1 local, 0 remote core engine proc(s) to start. bug;stale ### Your current environment ### 🐛 Describe the bug Model serving hangs when simply trying to serve `meta-llama/Meta-Llama-3.1-8B-Instruct` i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
