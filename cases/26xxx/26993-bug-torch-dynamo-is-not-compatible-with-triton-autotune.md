# vllm-project/vllm#26993: [Bug]: torch dynamo is not compatible with triton autotune

| 字段 | 值 |
| --- | --- |
| Issue | [#26993](https://github.com/vllm-project/vllm/issues/26993) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch dynamo is not compatible with triton autotune

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **when I ran the deepseek-v3 on 0.10.0 with v1 engine, it crashed when capturing cuda graph. When inferring, the optimal config for matmul is selected based on the size of M. This conflicts with the static graph requirement of Dynamo. How should this problem be solved?** command: ```python VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_MLA_DISABLE=1 VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve DeepSeek-V3-0324-BF16-Cast-To-Blockwise-Int8 \ --block-size 16 \ --enable-chunked-prefill \ --max-num-seqs 256 \ --max-num-batched-tokens 4096 \ --gpu-memory-utilization 0.97 \ --max-model-len 8192 \ --trust-remote-code \ -tp 8 \ -pp 4 \ --enable-expert-parallel \ --distributed-executor-backend ray ``` error: ``` 2025-10-16 05:51:05,844 ERROR worker.py:420 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.execute_method() (pid=1990, ip=192.168.23.10, actor_id=4cd629363da9989a8b12942002000000, repr= ) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/worker/worker_base.py", line 620, in execute_method raise e File "/opt/conda/envs/p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vllm/compilation/decorators.py", line 272, in __call__ output = self.compiled_callable(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/torch/_dynamo/ev...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: MLA_DISABLE=1 VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve DeepSeek-V3-0324-BF16-Cast-To-Blockwise-Int8 \ --block-size 16 \ --enable-chunked-prefill \ --max-num-seqs 256 \ --max-num-batched-tokens 4096 \ --gpu-memory-utiliza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: torch dynamo is not compatible with triton autotune bug;rocm ### Your current environment ### 🐛 Describe the bug **when I ran the deepseek-v3 on 0.10.0 with v1 engine, it crashed when capturing cuda graph. When i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: -max-model-len 8192 \ --trust-remote-code \ -tp 8 \ -pp 4 \ --enable-expert-parallel \ --distributed-executor-backend ray ``` error: ``` 2025-10-16 05:51:05,844 ERROR worker.py:420 -- Unhandled error (suppress with 'RAY...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: orker.py", line 233, in determine_available_memory self.model_runner.profile_run() File "/opt/conda/envs/py_3.12/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 2422, in profile_run = self._dummy_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
