# vllm-project/vllm#22794: [Bug]: openai/gpt-oss-120b NotImplementedError: Pipeline parallelism is not supported for this model. Supported models implement the `SupportsPP` interface.

| 字段 | 值 |
| --- | --- |
| Issue | [#22794](https://github.com/vllm-project/vllm/issues/22794) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openai/gpt-oss-120b NotImplementedError: Pipeline parallelism is not supported for this model. Supported models implement the `SupportsPP` interface.

### Issue 正文摘录

### Your current environment I am trying to deploy gpt-oss-120b model on L4 machines with 4 nodes, 1 l4 gpu each node using ray and vllm. `VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 vllm serve openai/gpt-oss-120b --pipeline-parallel-size 4 --tensor-parallel-size 1 ` I am successfully able to deploy gpt-oss-20b model on a single node machine using command `VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 vllm serve openai/gpt-oss-20b --async-scheduling ` Ray status output shows no issues `ray status ======== Autoscaler status: 2025-08-13 07:07:47.820979 ======== Node status Active: 1 node_3e1b8f54a6b6256489c6b258c173402f132478e217f43d36798e8d4f 1 node_cd574249e56a44c7686f07d3a85b592af8e315ee72ecee89d97e2920 1 node_79500e05f87ef91993b90575302cc66df6920a9a30c5fb880da1a3ca 1 node_cc572383958e6734af3f445bc3c2ec5bfd5bc445598e032163331610 Pending: (no pending nodes) Recent failures: (no failures) Resources Total Usage: 0.0/32.0 CPU 0.0/4.0 GPU 0B/81.95GiB memory 0B/35.12GiB object_store_memory Total Constraints: (no request_resources() constraints) Total Demands: (no resource demands)` ```text VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 vllm serve openai/gpt-oss-120b --pipeline-parallel-size 4...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rver pid=31040) INFO 08-13 06:58:24 [api_server.py:1787] vLLM API server version 0.10.2.dev2+gf5635d62e.d20250807 (APIServer pid=31040) INFO 08-13 06:58:24 [utils.py:326] non-default args: {'model_tag': 'openai/gpt-oss-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: nes with 4 nodes, 1 l4 gpu each node using ray and vllm. `VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 vllm serve openai/gpt-oss-120b --pipeline-parallel-size 4 --tensor-parallel-size 1 ` I am successfully able to deploy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: openai/gpt-oss-120b NotImplementedError: Pipeline parallelism is not supported for this model. Supported models implement the `SupportsPP` interface. bug ### Your current environment I am trying to deploy gpt-oss...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: openai/gpt-oss-120b NotImplementedError: Pipeline parallelism is not supported for this model. Supported models implement the `SupportsPP` interface. bug ### Your current environment I am trying to deploy gpt-oss...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: scheduling ` Ray status output shows no issues `ray status ======== Autoscaler status: 2025-08-13 07:07:47.820979 ======== Node status Active: 1 node_3e1b8f54a6b6256489c6b258c173402f132478e217f43d36798e8d4f 1 node_cd574...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
