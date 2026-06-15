# vllm-project/vllm#9206: [Feature]: Simple Data Parallelism in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#9206](https://github.com/vllm-project/vllm/issues/9206) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 32; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Simple Data Parallelism in vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It is common to have a scenario where folks want to deploy multiple vLLM instances on a single machine due to the machine have several GPUs (commonly 8 GPUs). The work can then be sharded across replicated instances. This issue describes the intended UX for such feature. Notably we might not want to tackle large distributed settings (100s of parallel vLLM instances), which should be better handled by a higher layers. * Offline use case, for the LLM class, a new argument data_parallel_size and support dispatching requests to one engine per GPU (or per tensor parallel size). ```python from vllm import LLM llm = LLM(model="...", data_parallel_size=X) # spawn X number of engine processes and shard the work among them llm = LLM(model="...", data_parallel_size=X, tensor_parallel_size=Y) # this is supported if X*Y <= total number of GPUs ``` For the server, same argument, route requests to different engine processes, we can start with simple round robin load balancing, but a good stretch goal is session affinity or prefix aware routing ```bash vllm serve ... --data-parallel-size X ``` ### Alternatives * LiteLLM + manually creating replicas * Using...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e case, for the LLM class, a new argument data_parallel_size and support dispatching requests to one engine per GPU (or per tensor parallel size). ```python from vllm import LLM llm = LLM(model="...", data_parallel_size...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: o one engine per GPU (or per tensor parallel size). ```python from vllm import LLM llm = LLM(model="...", data_parallel_size=X) # spawn X number of engine processes and shard the work among them llm = LLM(model="...", d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Simple Data Parallelism in vLLM feature request;stale ### 🚀 The feature, motivation and pitch It is common to have a scenario where folks want to deploy multiple vLLM instances on a single machine due to the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Simple Data Parallelism in vLLM feature request;stale ### 🚀 The feature, motivation and pitch It is common to have a scenario where folks want to deploy multiple vLLM instances on a single machine due to the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: * LiteLLM + manually creating replicas * Using ray.data or ray serve to scale out ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
