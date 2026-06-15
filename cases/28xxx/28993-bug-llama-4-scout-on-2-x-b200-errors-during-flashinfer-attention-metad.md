# vllm-project/vllm#28993: [Bug]: Llama 4 Scout on 2 x B200 errors during FlashInfer attention metadata build

| 字段 | 值 |
| --- | --- |
| Issue | [#28993](https://github.com/vllm-project/vllm/issues/28993) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama 4 Scout on 2 x B200 errors during FlashInfer attention metadata build

### Issue 正文摘录

### Your current environment Docker container, built on top of tag `v0.11.1` plus one small unrelated commit from myself. ### 🐛 Describe the bug I'm running benchmarking with the latest vLLM 0.11.1. I submit 1024 requests and I tried this twice, and both failed, but at different points in the benchmark (I remember the first one did get something like 570 requests done, whereas the second run only got 200-something requests done). I'm really not sure from where to tackle this. Please let me know if I can provide more info. Thanks. vLLM command ``` vllm server meta-llama/Llama-4-Scout-17B-16E-Instruct \ --port 8006 \ --tensor-parallel-size 2 \ --max-num-seqs 128 ``` `config.yaml` ``` async-scheduling: true max-num-batched-tokens: 8192 max-model-len: 20480 enable-expert-parallel: true dtype: bfloat16 trust-remote-code: true api-server-count: 3 ``` Error ``` (Worker_TP0_EP0 pid=794) ERROR 11-18 21:13:52 [v1/executor/multiproc_executor.py:815] Traceback (most recent call last): (Worker_TP0_EP0 pid=794) ERROR 11-18 21:13:52 [v1/executor/multiproc_executor.py:815] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop (Worker_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: Scout on 2 x B200 errors during FlashInfer attention metadata build bug;stale ### Your current environment Docker container, built on top of tag `v0.11.1` plus one small unrelated commit from myself. ### 🐛 Describe the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ]: Llama 4 Scout on 2 x B200 errors during FlashInfer attention metadata build bug;stale ### Your current environment Docker container, built on top of tag `v0.11.1` plus one small unrelated commit from myself. ### 🐛 De...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Llama 4 Scout on 2 x B200 errors during FlashInfer attention metadata build bug;stale ### Your current environment Docker container, built on top of tag `v0.11.1` plus one small unrelated commit from myself. ###...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: m-batched-tokens: 8192 max-model-len: 20480 enable-expert-parallel: true dtype: bfloat16 trust-remote-code: true api-server-count: 3 ``` Error ``` (Worker_TP0_EP0 pid=794) ERROR 11-18 21:13:52 [v1/executor/multiproc_exe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Llama 4 Scout on 2 x B200 errors during FlashInfer attention metadata build bug;stale ### Your current environment Docker container, built on top of tag `v0.11.1` plus one small unrelated commit from myself. ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
