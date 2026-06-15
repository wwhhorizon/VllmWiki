# vllm-project/vllm#28270: [Bug]: Pipeline parallel doesn't really do the "parallel" among GPUs.

| 字段 | 值 |
| --- | --- |
| Issue | [#28270](https://github.com/vllm-project/vllm/issues/28270) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline parallel doesn't really do the "parallel" among GPUs.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For PP8, after rank0 start a new batch, it won't start the next until rank8 finish the batch, which make the GPUs are not parallel. Typically, for PP, we should split the batch to 8 micro-batch and make sure every GPUs is working on different micro-batch at same time. But I didn't see the implementation in VLLM. Now I'm using a WAR for prefill by `--max-num-seqs $CONCURRENCY --max-num-batched-tokens $((ISL * CONCURRENCY / PP))` which force split batch by `--max-num-batched-tokens`, it works when I'm using `--distributed-executor-backend ray `. for default backend, even this WAR won't make it works. a wired thing is that I do see two batchs run sequential in a rank before wait for the next round. but we should have PP size micro-batch(8 in my case), not 2. my command: ``` vllm serve nvidia/DeepSeek-R1-0528-FP4-v2 --trust-remote-code --host 0.0.0.0 --port 8000 --pipeline-parallel-size 8 --tensor-parallel-size 1 --max-num-seqs 32 --max-cudagraph-capture-size 32 --max-model-len 4011 --max-num-batched-tokens 16000 --enable-chunked-prefill --kv-cache-dtype auto --gpu-memory-utilization 0.7 --no-enable-prefix-caching --distributed-execu...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: in my case), not 2. my command: ``` vllm serve nvidia/DeepSeek-R1-0528-FP4-v2 --trust-remote-code --host 0.0.0.0 --port 8000 --pipeline-parallel-size 8 --tensor-parallel-size 1 --max-num-seqs 32 --max-cudagraph-capture-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;opera...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e. But I didn't see the implementation in VLLM. Now I'm using a WAR for prefill by `--max-num-seqs $CONCURRENCY --max-num-batched-tokens $((ISL * CONCURRENCY / PP))` which force split batch by `--max-num-batched-tokens`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: max-num-batched-tokens`, it works when I'm using `--distributed-executor-backend ray `. for default backend, even this WAR won't make it works. a wired thing is that I do see two batchs run sequential in a rank before w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ipeline-parallel-size 8 --tensor-parallel-size 1 --max-num-seqs 32 --max-cudagraph-capture-size 32 --max-model-len 4011 --max-num-batched-tokens 16000 --enable-chunked-prefill --kv-cache-dtype auto --gpu-memory-utilizat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
