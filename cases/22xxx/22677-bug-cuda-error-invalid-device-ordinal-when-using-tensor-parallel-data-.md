# vllm-project/vllm#22677: [Bug]: CUDA error: invalid device ordinal when using tensor parallel + data parallel with data-parallel-backend ray

| 字段 | 值 |
| --- | --- |
| Issue | [#22677](https://github.com/vllm-project/vllm/issues/22677) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: invalid device ordinal when using tensor parallel + data parallel with data-parallel-backend ray

### Issue 正文摘录

### Your current environment vLLM v0.10.0 ### 🐛 Describe the bug I am using [data parallel](https://docs.vllm.ai/en/latest/serving/data_parallel_deployment.html) and ray as backend. Command ``` vllm serve $MODEL --tensor-parallel-size 1 --data-parallel-size 4 --data-parallel-size-local 1 \ --data-parallel-backend=ray ``` works well for me, so that I can run a 4 DP workers server using 4 nodes(each worker uses 1 GPU on its corresponding node) But when I run the below command to leverage 4 GPUs for each worker ``` vllm serve $MODEL --tensor-parallel-size 4 --data-parallel-size 4 --data-parallel-size-local 1 \ --data-parallel-backend=ray ``` I got ``` (DPEngineCoreActor pid=3551736) Exception raised in creation task: The actor died because of an error raised in its creation task, ray::DPEngineCoreActor.init() (pid=3551736, ip=10.0.2.109, actor_id=7b9995853ad2be757c1825e501000000, repr= ) (DPEngineCoreActor pid=3551736) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (DPEngineCoreActor pid=3551736) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (DPEngineCoreActor pid=3551736) File "/workplace/luhansh/AGIModelLens-new/src/AGIModelLens/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1089, in ini...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: olution with the DP solution? Or I can only implement external load balancing for multiple multi-nodes vLLM server? Thanks! development distributed_parallel;frontend_api;model_support cuda env_dependency Your current en...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ta_parallel_deployment.html) and ray as backend. Command ``` vllm serve $MODEL --tensor-parallel-size 1 --data-parallel-size 4 --data-parallel-size-local 1 \ --data-parallel-backend=ray ``` works well for me, so that I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ce ordinal when using tensor parallel + data parallel with data-parallel-backend ray bug;ray ### Your current environment vLLM v0.10.0 ### 🐛 Describe the bug I am using [data parallel](https://docs.vllm.ai/en/latest/ser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: CUDA error: invalid device ordinal when using tensor parallel + data parallel with data-parallel-backend ray bug;ray ### Your current environment vLLM v0.10.0 ### 🐛 Describe the bug I am using [data parallel](htt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 🐛 Describe the bug I am using [data parallel](https://docs.vllm.ai/en/latest/serving/data_parallel_deployment.html) and ray as backend. Command ``` vllm serve $MODEL --tensor-parallel-size 1 --data-parallel-size 4 --dat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
