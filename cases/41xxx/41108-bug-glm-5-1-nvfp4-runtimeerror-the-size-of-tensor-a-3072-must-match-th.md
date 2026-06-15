# vllm-project/vllm#41108: [Bug]: GLM-5.1-NVFP4 RuntimeError: The size of tensor a (3072) must match the size of tensor b (6144) at non-singleton dimension 1

| 字段 | 值 |
| --- | --- |
| Issue | [#41108](https://github.com/vllm-project/vllm/issues/41108) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-5.1-NVFP4 RuntimeError: The size of tensor a (3072) must match the size of tensor b (6144) at non-singleton dimension 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run GLM-5.1-NVFP4 on 4x H200 like this ```bash vllm serve /vllm-workspace/models/GLM-5.1-NVFP4 --tensor-parallel-size 4 --speculative-config.method mtp --speculative-config.num_speculative_tokens 3 --tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice --chat-template-content-format=string --served-model-name glm-5.1 ``` Unfortunately, I encounter the following error: ```bash (Worker_TP3 pid=1270) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py:857] WorkerProc failed to start. (Worker_TP3 pid=1270) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py:857] Traceback (most recent call last): (Worker_TP3 pid=1270) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py:857] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 826, in worker_main (Worker_TP3 pid=1270) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py:857] worker = WorkerProc(*args, **kwargs) (Worker_TP3 pid=1270) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py:857] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP3 pid=1270) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: GLM-5.1-NVFP4 RuntimeError: The size of tensor a (3072) must match the size of tensor b (6144) at non-singleton dimension 1 bug ### Your current environment ### 🐛 Describe the bug I am trying to run GLM-5.1-NVFP4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: executor.py:857] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker_TP3 pid=1270) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py:857] return func(*args, **kwa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: GLM-5.1-NVFP4 on 4x H200 like this ```bash vllm serve /vllm-workspace/models/GLM-5.1-NVFP4 --tensor-parallel-size 4 --speculative-config.method mtp --speculative-config.num_speculative_tokens 3 --tool-call-parser glm47...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/layer.py", line 1222, in weight_loader (Worker_TP0 pid=1267) ERROR 04-28 07:10:22 [v1/executor/multiproc_executor.py:857] File "/usr/local/lib...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: vllm-workspace/models/GLM-5.1-NVFP4 --tensor-parallel-size 4 --speculative-config.method mtp --speculative-config.num_speculative_tokens 3 --tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice --ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
