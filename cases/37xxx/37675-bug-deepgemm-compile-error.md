# vllm-project/vllm#37675: [Bug]: deepgemm compile error

| 字段 | 值 |
| --- | --- |
| Issue | [#37675](https://github.com/vllm-project/vllm/issues/37675) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepgemm compile error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running GLM 5 FP8 on 8xB200 with above config, results in the following exception: proc_executor.py:948] Traceback (most recent call last): (Worker_TP2_EP2 pid=1935304) ERROR 03-20 19:05:09 [multiproc_executor.py:948] File "/srv/workspace/work_dir/.vllm_venv/lib/python3.13/site-packages/vllm/v1/executor/multiproc_executor.py", line 943, in worker_busy_loop (Worker_TP2_EP2 pid=1935304) ERROR 03-20 19:05:09 [multiproc_executor.py:948] output = func(*args, **kwargs) (Worker_TP2_EP2 pid=1935304) ERROR 03-20 19:05:09 [multiproc_executor.py:948] File "/srv/workspace/work_dir/.vllm_venv/lib/python3.13/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context (Worker_TP2_EP2 pid=1935304) ERROR 03-20 19:05:09 [multiproc_executor.py:948] return func(*args, **kwargs) (Worker_TP2_EP2 pid=1935304) ERROR 03-20 19:05:09 [multiproc_executor.py:948] File "/srv/workspace/work_dir/.vllm_venv/lib/python3.13/site-packages/vllm/v1/worker/gpu_worker.py", line 388, in determine_available_memory (Worker_TP2_EP2 pid=1935304) ERROR 03-20 19:05:09 [multiproc_executor.py:948] self.model_runner.profile_run() (Worker_TP2_EP2 pid=1935304) ERROR 0...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: [Bug]: deepgemm compile error bug ### Your current environment ### 🐛 Describe the bug Running GLM 5 FP8 on 8xB200 with above config, results in the following exception: proc_executor.py:948] Traceback (most recent call...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: deepgemm compile error bug ### Your current environment ### 🐛 Describe the bug Running GLM 5 FP8 on 8xB200 with above config, results in the following exception: proc_executor.py:948] Traceback (most recent call...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: g ### Your current environment ### 🐛 Describe the bug Running GLM 5 FP8 on 8xB200 with above config, results in the following exception: proc_executor.py:948] Traceback (most recent call last): (Worker_TP2_EP2 pid=19353...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: r current environment ### 🐛 Describe the bug Running GLM 5 FP8 on 8xB200 with above config, results in the following exception: proc_executor.py:948] Traceback (most recent call last): (Worker_TP2_EP2 pid=1935304) ERROR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: k_dir/.vllm_venv/lib/python3.13/site-packages/vllm/compilation/piecewise_backend.py", line 367, in __call__ (Worker_TP2_EP2 pid=1935304) ERROR 03-20 19:05:09 [multiproc_executor.py:948] return range_entry.runnable(*args...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
