# vllm-project/vllm#12256: [Usage]: deepseek v3 can not set tensor_parallel_size=32

| 字段 | 值 |
| --- | --- |
| Issue | [#12256](https://github.com/vllm-project/vllm/issues/12256) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: deepseek v3 can not set tensor_parallel_size=32

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm [rank0]: model = _initialize_model(vllm_config=vllm_config) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/loader.py", line 116, in _initialize_model [rank0]: return model_class(vllm_config=vllm_config, prefix=prefix) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/deepseek_v3.py", line 505, in __init__ [rank0]: self.model = DeepseekV3Model(vllm_config=vllm_config, [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/deepseek_v3.py", line 440, in __init__ [rank0]: self.start_layer, self.end_layer, self.layers = make_layers( [rank0]: ^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/utils.py", line 551, in make_layers [rank0]: maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: odel_executor/layers/linear.py", line 309, in __init__ [rank0]: self.quant_method.create_weights( [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/quantization/fp8.py", line 186, in crea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on collect_env.py` ``` ### How would you like to use vllm [rank0]: model = _initialize_model(vllm_config=vllm_config) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-pac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: deepseek v3 can not set tensor_parallel_size=32 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm [rank0]: model = _initialize_model(v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 28. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: l_executor/models/utils.py", line 551, in make_layers [rank0]: maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
