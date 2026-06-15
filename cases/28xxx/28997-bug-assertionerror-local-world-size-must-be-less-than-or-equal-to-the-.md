# vllm-project/vllm#28997: [Bug]: AssertionError: local_world_size must be less than or equal to the number of visible devices

| 字段 | 值 |
| --- | --- |
| Issue | [#28997](https://github.com/vllm-project/vllm/issues/28997) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: local_world_size must be less than or equal to the number of visible devices

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running TP8 across two GB200 nodes (4 gpus each) using ray. I'm encountering assertion errors regarding the world size. I only encountered this on 0.11.1; 0.11.0 works fine. Output of `ray status`: ```======== Autoscaler status: 2025-11-18 22:46:37.848831 ======== Node status --------------------------------------------------------------- Active: 1 node_503b8417b7f0e134daceefd694dbbbf80c1b94194a48bb38c2a920cb 1 node_1d1a7daf21dfe323fecb012b70211f8d0de58027abbabd0b6b3576e6 Pending: (no pending nodes) Recent failures: (no failures) Resources --------------------------------------------------------------- Total Usage: 0.0/288.0 CPU 0.0/8.0 GPU 0B/2.80TiB memory 0B/372.53GiB object_store_memory From request_resources: (none) Pending Demands: (no resource demands) ``` Run command: `vllm serve --model --tensor-parallel-size 8 --distributed-executor-backend ray` vLLM debug log output (can't post full log due to character limit, so limiting to relevant stack traces instead): ``` (EngineCore_DP0 pid=1773285) ERROR 11-18 22:45:34 [v1/engine/core.py:842] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1773285) ERROR 11-18 22:45...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: d: `vllm serve --model --tensor-parallel-size 8 --distributed-executor-backend ray` vLLM debug log output (can't post full log due to character limit, so limiting to relevant stack traces instead): ``` (EngineCore_DP0 p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: /__init__.py", line 109, in run (APIServer pid=1773137) return __asyncio.run( (APIServer pid=1773137) ^^^^^^^^^^^^^^ (APIServer pid=1773137) File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run (APIServer pid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rent environment ### 🐛 Describe the bug I'm running TP8 across two GB200 nodes (4 gpus each) using ray. I'm encountering assertion errors regarding the world size. I only encountered this on 0.11.1; 0.11.0 works fine. O...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: on 0.11.1; 0.11.0 works fine. Output of `ray status`: ```======== Autoscaler status: 2025-11-18 22:46:37.848831 ======== Node status --------------------------------------------------------------- Active: 1 node_503b841...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Pending Demands: (no resource demands) ``` Run command: `vllm serve --model --tensor-parallel-size 8 --distributed-executor-backend ray` vLLM debug log output (can't post full log due to character limit, so limiting to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
