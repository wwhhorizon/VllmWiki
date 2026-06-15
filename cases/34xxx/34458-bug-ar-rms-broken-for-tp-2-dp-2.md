# vllm-project/vllm#34458: [Bug]: AR+rms broken for TP=2 DP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#34458](https://github.com/vllm-project/vllm/issues/34458) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AR+rms broken for TP=2 DP=2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems like the symmetric memory setup runs into some issues when using DP & TP, note that this is after the fix in https://github.com/vllm-project/vllm/issues/34401#issuecomment-3891510042 ``` $ vllm serve -tp=2 -dp=2 -cc.pass_config.fuse_allreduce_rms qwen/qwen3-30b-a3b (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] WorkerProc hit an exception. (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] Traceback (most recent call last): (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] File "/home/ProExpertProg/git/vllm/vllm/v1/executor/multiproc_executor.py", line 858, in worker_busy_loop (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] output = func(*args, **kwargs) (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] File "/home/ProExpertProg/git/vllm/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ues/34401#issuecomment-3891510042 ``` $ vllm serve -tp=2 -dp=2 -cc.pass_config.fuse_allreduce_rms qwen/qwen3-30b-a3b (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] WorkerProc hit an except...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] self.aot_compiled_fn = self.aot_compile(*args, **kwargs) (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 0859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] compiled_fn = backend( (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] ^^^^^^^^ (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [mul...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 50859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] File "/home/ProExpertProg/git/vllm/vllm/v1/executor/multiproc_executor.py", line 858, in worker_busy_loop (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multip...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ) ERROR 02-12 14:51:17 [multiproc_executor.py:863] self.model_runner.profile_run() (Worker_DP1_TP0 pid=2450859) ERROR 02-12 14:51:17 [multiproc_executor.py:863] File "/home/ProExpertProg/git/vllm/vllm/v1/worker/gpu_mode...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
