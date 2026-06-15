# vllm-project/vllm#16197: [Bug]: Not able to deploy Llama-4-Scout-17B-16E-Instruct on vllm-openai v0.8.3

| 字段 | 值 |
| --- | --- |
| Issue | [#16197](https://github.com/vllm-project/vllm/issues/16197) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not able to deploy Llama-4-Scout-17B-16E-Instruct on vllm-openai v0.8.3

### Issue 正文摘录

### Your current environment 1) Download the Llama-4-Scout-17B-16E-Instruct on PVC 2) Deploy the model on azure kubernates on A100 with 2 GPUs 80GB each. 3) using below arguments ``` args: - "--model" - "/mnt/models/meta-llama-4-scout-17b-16e-instruct" - "--api-key" - "$(VLLM_API_KEY)" - "--tensor-parallel-size" - "2" - "--dtype" - "bfloat16" - "--port" - "8000" - "--max-model-len" - "32768" - "--max-num-batched-tokens" - "32768" - "--max-num-seqs" - "16" - "--gpu-memory-utilization" - "0.99" - "--served-model-name" - "Llama-4-Scout-17B-16E-Instruct" - "--trust-remote-code" - "--disable-log-requests" - "--enable-chunked-prefill" - "--enable-prefix-caching" ``` 4) Getting fallowing error ``` (VllmWorker rank=0 pid=222) INFO 04-07 08:59:23 [custom_all_reduce_utils.py:244] reading GPU P2P access cache from /root/.cache/vllm/gpu_p2p_access_cache_for_0,1.json (VllmWorker rank=1 pid=239) INFO 04-07 08:59:23 [custom_all_reduce_utils.py:244] reading GPU P2P access cache from /root/.cache/vllm/gpu_p2p_access_cache_for_0,1.json (VllmWorker rank=0 pid=222) INFO 04-07 08:59:23 [shm_broadcast.py:264] vLLM message queue communication handle: Handle(local_reader_ranks=[1], buffer_handle=(1, 4194...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rank=0 pid=222) INFO 04-07 08:59:26 [config.py:3334] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 20...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: out-17B-16E-Instruct on PVC 2) Deploy the model on azure kubernates on A100 with 2 GPUs 80GB each. 3) using below arguments ``` args: - "--model" - "/mnt/models/meta-llama-4-scout-17b-16e-instruct" - "--api-key" - "$(VL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _API_KEY)" - "--tensor-parallel-size" - "2" - "--dtype" - "bfloat16" - "--port" - "8000" - "--max-model-len" - "32768" - "--max-num-batched-tokens" - "32768" - "--max-num-seqs" - "16" - "--
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Not able to deploy Llama-4-Scout-17B-16E-Instruct on vllm-openai v0.8.3 bug ### Your current environment 1) Download the Llama-4-Scout-17B-16E-Instruct on PVC 2) Deploy the model on azure kubernates on A100 with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: B-16E-Instruct" - "--trust-remote-code" - "--disable-log-requests" - "--enable-chunked-prefill" - "--enable-prefix-caching" ``` 4) Getting fallowing error ``` (VllmWorker rank=0 pid=222) INFO 04-07 08:59:23 [custom_all_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
