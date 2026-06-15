# vllm-project/vllm#40790: [Bug]: dpsk v4 on 8* H20-96G

| 字段 | 值 |
| --- | --- |
| Issue | [#40790](https://github.com/vllm-project/vllm/issues/40790) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: dpsk v4 on 8* H20-96G

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] return func(*args, **kwargs) (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/default_loader.py", line 381, in load_weights (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] loaded_weights = model.load_weights(self.get_all_weights(model_config, model)) (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/deepseek_v4.py", line 846, in load_weights (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper) (Worker_DP3_EP3 pid=2376) E...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: oc_executor.py:879] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/model_loader/default_loader.py", line 381, in load_weights (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879]...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/layer.py", line 1304, in weight_loader (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] self._load_model_weight_or_g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Describe the bug File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] return func(*args, **kwargs) (Wo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [multiproc_executor.py:879] self._load_model_weight_or_group_weight_scale( (Worker_DP3_EP3 pid=2376) ERROR 04-24 08:02:05 [multiproc_executor.py:879] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/lay...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /s] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
