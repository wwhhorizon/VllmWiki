# vllm-project/vllm#27879: [Bug]: significantly poor performance of gpt-oss on blackwell b200

| 字段 | 值 |
| --- | --- |
| Issue | [#27879](https://github.com/vllm-project/vllm/issues/27879) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;hardware_porting;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: significantly poor performance of gpt-oss on blackwell b200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` export VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB='{"2":32,"4":32,"8":8}' export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 vllm serve openai/gpt-oss-120b --compilation-config {"pass_config":{"enable_fi_allreduce_fusion":true,"enable_noop":true},"custom_ops":["+rms_norm"],"cudagraph_mode":"FULL_AND_PIECEWISE"} --async-scheduling --cuda-graph-sizes 2048 --host 0.0.0.0 --port 8000 ``` I am only getting around 30-35 generation tps. ``` (APIServer pid=4) INFO 10-31 13:02:01 [loggers.py:215] Engine 000: Avg prompt throughput: 154.3 tokens/s, Avg generation throughput: 31.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 3.9% (APIServer pid=4) INFO 10-31 13:02:11 [loggers.py:215] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 33.9 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 3.9% (APIServer pid=4) INFO 10-31 13:02:21 [loggers.py:215] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 34.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 3.9% ```...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: significantly poor performance of gpt-oss on blackwell b200 bug ### Your current environment ### 🐛 Describe the bug ``` export VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB='{"2":32,"4":32,"8":8}' export VLLM_US...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ION_THRESHOLDS_MB='{"2":32,"4":32,"8":8}' export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 vllm serve openai/gpt-oss-120b --compilation-config {"pass_config":{"enable_fi_allreduce_fusion":true,"enable_noop":true},"custom_op...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ion_norm;attention_kv_cache;hardware_porting;scheduler_memory cache;cuda build_error;slowdown env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: eration throughput: 31.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 3.9% (APIServer pid=4) INFO 10-31 13:02:11 [loggers.py:215] Engine 000: Avg prompt throughput: 0.0 to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: significantly poor performance of gpt-oss on blackwell b200 bug ### Your current environment ### 🐛 Describe the bug ``` export VLLM_FLASHINFER_ALLREDUCE_FUSION_THRESHOLDS_MB='{"2":32,"4":32,"8":8}' export VLLM_US...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
