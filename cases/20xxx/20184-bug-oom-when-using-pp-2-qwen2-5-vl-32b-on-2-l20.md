# vllm-project/vllm#20184: [Bug]: OOM when using pp=2 qwen2.5 vl 32B on 2 L20

| 字段 | 值 |
| --- | --- |
| Issue | [#20184](https://github.com/vllm-project/vllm/issues/20184) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM when using pp=2 qwen2.5 vl 32B on 2 L20

### Issue 正文摘录

```text WARNING 06-27 13:31:35 [sampling_params.py:344] temperature 1e-06 is less than 0.01, which may cause numerical errors nan or inf in tensors. We have maxed it out to 0.01. (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] WorkerProc hit an exception. (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] Traceback (most recent call last): (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/executor/multiproc_executor.py", line 522, in worker_busy_loop (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] output = func(*args, **kwargs) (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] return func(*args, **kwargs) (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/worker/gpu_worker.py", line 293, in execute_model (Vl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: les_layers_modules_33_modules_self_attn_modules_o_proj_parameters_weight_scale_, getitem_13, l_self_modules_layers_modules_33_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_33_modules...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: OOM when using pp=2 qwen2.5 vl 32B on 2 L20 bug;stale ```text WARNING 06-27 13:31:35 [sampling_params.py:344] temperature 1e-06 is less than 0.01, which may cause numerical errors nan or inf in tensors. We have m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] return self.compiled_graph_for_general_shape(*args) (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:527] File "/usr/local/lib/python3....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: OOM when using pp=2 qwen2.5 vl 32B on 2 L20 bug;stale ```text WARNING 06-27 13:31:35 [sampling_params.py:344] temperature 1e-06 is less than 0.01, which may cause numerical errors nan or inf in tensors. We have m...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ling_params.py:344] temperature 1e-06 is less than 0.01, which may cause numerical errors nan or inf in tensors. We have maxed it out to 0.01. (VllmWorker rank=1 pid=1162710) ERROR 06-27 13:31:36 [multiproc_executor.py:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
