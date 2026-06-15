# vllm-project/vllm#22784: [Bug]: AttributeError when loading Step3 model

| 字段 | 值 |
| --- | --- |
| Issue | [#22784](https://github.com/vllm-project/vllm/issues/22784) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError when loading Step3 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the Step3 model on H20, vLLM fails with an AttributeError during weight loading, as quant_config is unexpectedly None. CMD： vllm serve /mnt/nvme0/step3/ -tp 8 --reasoning-parser step3 --gpu-memory-utilization 0.9 --trust-remote-code ``` Traceback (most recent call last): (VllmWorker TP1 pid=2752171) ERROR 08-12 20:25:18 [multiproc_executor.py:559] Traceback (most recent call last): [376/1902] (VllmWorker TP1 pid=2752171) ERROR 08-12 20:25:18 [multiproc_executor.py:559] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_ executor.py", line 533, in worker_main (VllmWorker TP1 pid=2752171) ERROR 08-12 20:25:18 [multiproc_executor.py:559] worker = WorkerProc(*args, **kwargs) (VllmWorker TP1 pid=2752171) ERROR 08-12 20:25:18 [multiproc_executor.py:559] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker TP1 pid=2752171) ERROR 08-12 20:25:18 [multiproc_executor.py:559] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_ executor.py", line 402, in __init__ (VllmWorker TP1 pid=2752171) ERROR 08-12 20:25:18 [multiproc_executor.py:559] self.worker.load_model() (VllmWorker TP1 pid=2752171) ERROR...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: odel on H20, vLLM fails with an AttributeError during weight loading, as quant_config is unexpectedly None. CMD： vllm serve /mnt/nvme0/step3/ -tp 8 --reasoning-parser step3 --gpu-memory-utilization 0.9 --trust-remote-co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;operator;samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: AttributeError when loading Step3 model bug;stale ### Your current environment ### 🐛 Describe the bug When running the Step3 model on H20, vLLM fails with an AttributeError during weight loading, as quant_config...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/layer.py", line 1080, in weight_loader if not expert_id and self.quant_config.get_name() == "mxfp4": AttributeError: 'NoneType' object has no...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
