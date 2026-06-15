# vllm-project/vllm#30026: [Bug]: Failed to deploy Qwen3-Next-80B with LoRA Adpater on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#30026](https://github.com/vllm-project/vllm/issues/30026) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to deploy Qwen3-Next-80B with LoRA Adpater on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Code to reproduce the problem: ```bash vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --served-model-name Qwen3-Next-80B-A3B-Instruct --port 8801 --tensor-parallel-size 8 --max-model-len 6400 --gpu-memory-utilization 0.9 --max-num-seqs 4 --enable-lora --lora-modules sql-lora=/path/to/mylora --tool-call-parser hermes --enable-auto-tool-choice ``` The error message I got: ``` (Worker_TP5 pid=116613) Exception ignored in: . at 0x7f7a0ce67a30> (Worker_TP5 pid=116613) Traceback (most recent call last): (Worker_TP5 pid=116613) File "/home/ec2-user/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 988, in (Worker_TP5 pid=116613) self.refs[idx] = weakref.ref(key, lambda ref: self._remove_id(idx)) (Worker_TP5 pid=116613) File "/home/ec2-user/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 689, in signal_handler (Worker_TP5 pid=116613) raise SystemExit() (Worker_TP5 pid=116613) SystemExit: (Worker_TP5 pid=116613) ERROR 12-04 04:49:03 [multiproc_executor.py:822] WorkerProc hit an exception. (Worker_TP5 pid=116613) ERROR 12-04 04:49:03 [multiproc_executor.py:822] Trac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 6613) ERROR 12-04 04:49:03 [multiproc_executor.py:822] output = TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs) (Worker_TP5 pid=116613) ERROR 12-04 04:49:03 [multiproc_executor.py:822] File "/home/ec2-us...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: OR 12-04 04:49:03 [multiproc_executor.py:822] buf14 = torch.ops.vllm.moe_forward_shared.default(buf12, buf13, 'model.layers.0.mlp.experts') (Worker_TP5 pid=116613) ERROR 12-04 04:49:03 [multiproc_executor.py:822] File "...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: conda3/envs/vllm/lib/python3.10/site-packages/vllm/compilation/piecewise_backend.py", line 93, in __call__ (Worker_TP5 pid=116613) ERROR 12-04 04:49:03 [multiproc_executor.py:822] return self.compiled_graph_for_general_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Failed to deploy Qwen3-Next-80B with LoRA Adpater on H100 bug ### Your current environment ### 🐛 Describe the bug Code to reproduce the problem: ```bash vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --served-model-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 12-04 04:49:03 [multiproc_executor.py:822] self.model_runner.profile_run() (Worker_TP5 pid=116613) ERROR 12-04 04:49:03 [multiproc_executor.py:822] File "/home/ec2-user/miniconda3/envs/vllm/lib/python3.10/site-p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
