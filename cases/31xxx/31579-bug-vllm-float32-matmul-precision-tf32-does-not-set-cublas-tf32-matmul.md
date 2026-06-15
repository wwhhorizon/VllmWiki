# vllm-project/vllm#31579: [Bug]: `VLLM_FLOAT32_MATMUL_PRECISION=tf32` does not set cublas tf32 matmul

| 字段 | 值 |
| --- | --- |
| Issue | [#31579](https://github.com/vllm-project/vllm/issues/31579) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `VLLM_FLOAT32_MATMUL_PRECISION=tf32` does not set cublas tf32 matmul

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While I ran GLM-4.7 FP8 checkpoint, I got the following error when the environment variable `VLLM_FLOAT32_MATMUL_PRECISION=tf32` is set. # Reproducer ```shell VLLM_FLOAT32_MATMUL_PRECISION=tf32 vllm serve zai-org/GLM-4.7-FP8 \ --trust-remote-code \ --gpu-memory-utilization 0.93 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --all2all-backehd deepep_low_latency \ --max-model-len 131072 \ --max-num-batched-tokens 16384 \ --max-num-seqs 32 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --enable-auto-tool-choice \ --tool-call-parser glm47 \ --reasoning-parser deepseek_r1 ``` ```log ... (Worker_TP6_EP6 pid=946) INFO 12-31 21:34:44 [backend.py:261] Cache the graph of compile range (1, 16384) for later use (Worker_TP7_EP7 pid=958) INFO 12-31 21:34:44 [backend.py:261] Cache the graph of compile range (1, 16384) for later use (Worker_TP4_EP4 pid=922) ERROR 12-31 21:34:52 [multiproc_executor.py:824] WorkerProc hit an exception. (Worker_TP4_EP4 pid=922) ERROR 12-31 21:34:52 [multiproc_executor.py:824] Traceback (most recent call last): (Worker_TP4_EP4 pid=922) ERROR 12-31 21:34:52 [multiproc_exe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: `VLLM_FLOAT32_MATMUL_PRECISION=tf32` does not set cublas tf32 matmul bug ### Your current environment ### 🐛 Describe the bug While I ran GLM-4.7 FP8 checkpoint, I got the following error when the environment vari...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: `VLLM_FLOAT32_MATMUL_PRECISION=tf32` does not set cublas tf32 matmul bug ### Your current environment ### 🐛 Describe the bug While I ran GLM-4.7 FP8 checkpoint, I got the following error when the environment vari...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: lel-size 8 \ --enable-expert-parallel \ --all2all-backehd deepep_low_latency \ --max-model-len 131072 \ --max-num-batched-tokens 16384 \ --max-num-seqs 32 \ --speculative-config.method mtp \ --speculative-config.num_spe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: py:824] File "/app/.venv/lib/python3.12/site-packaged/vllm/compilation/cuda_graph.py", line 220, in __call__ (Worker_TP4_EP4 pid=922) ERROR 12-31 21:34:52 [multiproc_executor.py:824] return self.runnable(*args, **kwargs...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --gpu-memory-utilization 0.93 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --all2all-backehd deepep_low_latency \ --max-model-len 131072 \ --max-num-batched-tokens 16384 \ --max-num-seqs 32 \ --speculative-co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
