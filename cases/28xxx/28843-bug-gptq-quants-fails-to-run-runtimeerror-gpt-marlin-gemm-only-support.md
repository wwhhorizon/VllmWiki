# vllm-project/vllm#28843: [Bug]: GPTQ quants fails to run ( RuntimeError: gpt_marlin_gemm only supports bfloat16 and float16 )

| 字段 | 值 |
| --- | --- |
| Issue | [#28843](https://github.com/vllm-project/vllm/issues/28843) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPTQ quants fails to run ( RuntimeError: gpt_marlin_gemm only supports bfloat16 and float16 )

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GPTQ (and i believe derived from gptq i.e. Intel's autoround) quants not working anymore. Tried with Qwen3-Next-Instruct - both Intel autoround int4 and GPTQ fails with error `RuntimeError: gpt_marlin_gemm only supports bfloat16 and float16` despite beeing run with `--dtype float16` full run command: `vllm serve /mnt/nfs-share/LLM/Qwen3-Next-80B-A3B-Instruct-Int4-GPTQ/ --host 0.0.0.0 --port 30000 --tensor-parallel-size 2 --served-model-name Qwen3-30B o3 --max-model-len 214880 --gpu-memory-utilization 0.95 --dtype float16 --max-num-seqs 8 --tool-call-parser hermes --enable-auto-tool-choice --enable-expert-parallel --generation-config auto --override-generation-config '{"min_p":0.0,"max_new_tokens":32768}'` Stacktrace: ``` Loading safetensors checkpoint shards: 100% Completed | 9/9 [02:54 ... (Worker_TP1_EP1 pid=110163) ERROR 11-17 07:54:19 [multiproc_executor.py:815] **model_kwargs, (Worker_TP1_EP1 pid=110163) ERROR 11-17 07:54:19 [multiproc_executor.py:815] ) (Worker_TP1_EP1 pid=110163) ERROR 11-17 07:54:19 [multiproc_executor.py:815] File "/home/drros/vllm.313/.venv/lib/python3.13/site-packages/vllm/compilation/cuda_graph.py", l...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: GPTQ quants fails to run ( RuntimeError: gpt_marlin_gemm only supports bfloat16 and float16 ) bug;stale ### Your current environment ### 🐛 Describe the bug GPTQ (and i believe derived from gptq i.e. Intel's autor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0163) ERROR 11-17 07:54:19 [multiproc_executor.py:815] output = TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs) (Worker_TP0_EP0 pid=110162) ERROR 11-17 07:54:19 [multiproc_executor.py:815] return func(*a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: from gptq i.e. Intel's autoround) quants not working anymore. Tried with Qwen3-Next-Instruct - both Intel autoround int4 and GPTQ fails with error `RuntimeError: gpt_marlin_gemm only supports bfloat16 and float16` despi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: GPTQ quants fails to run ( RuntimeError: gpt_marlin_gemm only supports bfloat16 and float16 ) bug;stale ### Your current environment ### 🐛 Describe the bug GPTQ (and i believe derived from gptq i.e. Intel's autor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 11-17 07:54:19 [multiproc_executor.py:815] self.model_runner.profile_run() (Worker_TP1_EP1 pid=110163) ERROR 11-17 07:54:19 [multiproc_executor.py:815] ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^ (Worker_TP0_EP0 pi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
