# vllm-project/vllm#5944: [Bug]: "work_use_ray" not work anymore in the latest version

| 字段 | 值 |
| --- | --- |
| Issue | [#5944](https://github.com/vllm-project/vllm/issues/5944) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "work_use_ray" not work anymore in the latest version

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug So, `work_use_ray` do not work anymore? check the code: https://github.com/vllm-project/vllm/blob/c3dde367f16111b8968948a1f8e1a26bdac6ffdd/vllm/engine/llm_engine.py#L371 To leverage `ray` or not seems turn to: `engine_config.parallel_config.distributed_executor_backend` I think at least we need document the change.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: r not seems turn to: `engine_config.parallel_config.distributed_executor_backend` I think at least we need document the change.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: "work_use_ray" not work anymore in the latest version bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug So, `work_use_ray` do not work anymore? check the co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gine/llm_engine.py#L371 To leverage `ray` or not seems turn to: `engine_config.parallel_config.distributed_executor_backend` I think at least we need document the change.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: "work_use_ray" not work anymore in the latest version bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug So, `work_use_ray` do not work anymore? check the co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
