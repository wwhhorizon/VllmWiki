# vllm-project/vllm#44191: Speculative decoding regression in v0.22.0

| 字段 | 值 |
| --- | --- |
| Issue | [#44191](https://github.com/vllm-project/vllm/issues/44191) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Speculative decoding regression in v0.22.0

### Issue 正文摘录

## Summary CPU speculative decoding (draft-model method) is **severely regressed** in v0.22.0 compared to v0.21.0. On the same hardware, same models, same prompts: - **v0.21.0**: SD delivers 2.15–2.72× TPOT speedup across 3 model pairs - **v0.22.0**: SD is 4–25× *slower* than baseline (and intermittently crashes with OOB) ## Environment - **Hardware**: Intel Xeon Platinum 8580 (Emerald Rapids), 2×60 cores, 4 NUMA nodes (SNC2) - **Binding**: `VLLM_CPU_OMP_THREADS_BIND="0-119"`, `OMP_NUM_THREADS=120` (physical cores only, no HT) - **Container**: `vllm/vllm-openai-cpu:v0.21.0` (works) vs source-built v0.22.0 (regressed) - **OS**: Ubuntu 22.04, gcc-12.3.0, torch 2.11.0+cpu - **BS=1**, `--max-num-seqs 1`, `temperature=0`, `max_tokens=512` ## Reproduction ### v0.21.0 (working) ```bash # Using apptainer with the official CPU image apptainer exec \ --env "VLLM_CPU_OMP_THREADS_BIND=0-119" \ --env "OMP_NUM_THREADS=120" \ --env "VLLM_TARGET_DEVICE=cpu" \ vllm-openai-cpu-v0.21.0.sif \ python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-3.1-8B-Instruct \ --dtype bfloat16 \ --max-num-seqs 1 \ --port 8001 \ --max-model-len 4096 \ --speculative-config '{"method":"draft_model",...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: coding regression in v0.22.0 ## Summary CPU speculative decoding (draft-model method) is **severely regressed** in v0.22.0 compared to v0.21.0. On the same hardware, same models, same prompts: - **v0.21.0**: SD delivers...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: openai.api_server \ --model meta-llama/Llama-3.1-8B-Instruct \ --dtype bfloat16 \ --max-num-seqs 1 \ --port 8001 \ --max-model-len 4096 \ --speculative-config '{"method":"draft_model","model":"meta-llama/Llama-3.2-1B-In...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Speculative decoding regression in v0.22.0 ## Summary CPU speculative decoding (draft-model method) is **severely regressed** in v0.22.0 compared to v0.21.0. On the same hardware, same models, same prompts: - **v0.21.0
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: roduction ### v0.21.0 (working) ```bash # Using apptainer with the official CPU image apptainer exec \ --env "VLLM_CPU_OMP_THREADS_BIND=0-119" \ --env "OMP_NUM_THREADS=120" \ --env "VLLM_TARGET_DEVICE=cpu" \ vllm-openai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Speculative decoding regression in v0.22.0 ## Summary CPU speculative decoding (draft-model method) is **severely regressed** in v0.22.0 compared to v0.21.0. On the same hardware, same models, same prompts: - **v0.21.0*...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
