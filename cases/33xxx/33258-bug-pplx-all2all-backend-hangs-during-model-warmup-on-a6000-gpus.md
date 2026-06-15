# vllm-project/vllm#33258: [Bug]: pplx all2all backend hangs during model warmup on A6000 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#33258](https://github.com/vllm-project/vllm/issues/33258) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pplx all2all backend hangs during model warmup on A6000 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to serve Qwen3-30B-A3B (MoE model) on 4x NVIDIA RTX A6000 GPUs with expert parallelism enabled. The allgather_reducescatter backend works perfectly, but the pplx backend hangs during initialization. When using --all2all-backend pplx, the server hangs during model initialization. Specifically: 1. Model loading completes successfully 2. PPLXAll2AllManager initializes (intranode mode, no NVSHMEM) 3. torch.compile caching completes successfully 4. Hang occurs here - before CUDA graph capture finishes No errors are logged. The EngineCore processes become completely silent after torch.compile caching - no crash, no error, just a deadlock. ``` vllm serve Qwen/Qwen3-30B-A3B-Instruct-2507 \ --port 8080 \ --data-parallel-size 4 \ --tensor-parallel-size 1 \ --enable-expert-parallel \ --all2all-backend pplx \ --gpu-memory-utilization 0.9 \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` This is log. ``` [0;36m(APIServer pid=8295)[0;0m INFO 01-28 20:31:43 [api_server.py:1351] vLLM API server version 0.13.1.dev19+gf9a21ae6a.d20260127 [0;36m(APIServer pid=8295)[0;0m INFO 01-28 20:31:43 [utils.py:253] non-default args: {...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: --all2all-backend pplx, the server hangs during model initialization. Specifically: 1. Model loading completes successfully 2. PPLXAll2AllManager initializes (intranode mode, no NVSHMEM) 3. torch.compile caching complet...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: pplx all2all backend hangs during model warmup on A6000 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to serve Qwen3-30B-A3B (MoE model) on 4x NVIDIA RTX A6000 GPUs with expert par...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: pplx all2all backend hangs during model warmup on A6000 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug I'm trying to serve Qwen3-30B-A3B (MoE model) on 4x NVIDIA RTX A6000 GPUs with expert par...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ribe the bug I'm trying to serve Qwen3-30B-A3B (MoE model) on 4x NVIDIA RTX A6000 GPUs with expert parallelism enabled. The allgather_reducescatter backend works perfectly, but the pplx backend hangs during initializati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
