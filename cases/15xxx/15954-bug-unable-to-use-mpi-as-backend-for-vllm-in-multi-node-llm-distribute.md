# vllm-project/vllm#15954: [Bug]: Unable to Use MPI as Backend for vLLM  in Multi-Node LLM distributed Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#15954](https://github.com/vllm-project/vllm/issues/15954) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to Use MPI as Backend for vLLM  in Multi-Node LLM distributed Inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm attempting to achieve distributed inference for LLM model on multi-node environment(don't support NCCL), using MPI to manage inter-node communication. My goal is to use model parallelism(tensor parallel,pipeline parallel ,expert parallel) on my 2 nodes. I can successfully launch correct vllm server on each single node with MPI and everything ok. However, when launching the distributed service, MPI can not get the right world_size and rank at the runtime. my script `run_distributed_serving.sh`: ```bash #!/bin/bash # API startup parameters MODEL="/models/DeepSeek-R1-Distill-Qwen-1.5B" GPU_MEMORY_UTILIZATION=0.2 MAX_NUM_BATCHED_TOKENS=256 TENSOR_PARALLEL_SIZE=1 PIPELINE_PARALLEL_SIZE=2 # SERVED_MODEL_NAME="deepseek" # undefined # Start API server echo "Starting API server..." python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8080 \ --trust-remote-code \ --model $MODEL \ --gpu-memory-utilization $GPU_MEMORY_UTILIZATION \ --max-num-batched-tokens $MAX_NUM_BATCHED_TOKENS \ --distributed-executor-backend ray \ --tensor-parallel-size $TENSOR_PARALLEL_SIZE \ --pipeline-parallel-size $PIPELINE_PARALLEL_SIZE ``` Lau...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Wrapper pid=72389) ERROR [worker_base.py:620] File "[...]/ray/util/tracing/tracing_helper.py", line 463, in *resume*span (RayWorkerWrapper pid=72389) ERROR [worker_base.py:620] return method(self, *args, **kwargs) (RayW...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: escribe the bug I'm attempting to achieve distributed inference for LLM model on multi-node environment(don't support NCCL), using MPI to manage inter-node communication. My goal is to use model parallelism(tensor paral...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: MPI to manage inter-node communication. My goal is to use model parallelism(tensor parallel,pipeline parallel ,expert parallel) on my 2 nodes. I can successfully launch correct vllm server on each single node with MPI a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: . My goal is to use model parallelism(tensor parallel,pipeline parallel ,expert parallel) on my 2 nodes. I can successfully launch correct vllm server on each single node with MPI and everything ok. However, when launch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Use MPI as Backend for vLLM in Multi-Node LLM distributed Inference bug;stale ### Your current environment ### 🐛 Describe the bug I'm attempting to achieve distributed inference for LLM model on multi-node environment(d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
