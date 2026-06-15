# vllm-project/vllm#21983: [Bug]: TTFT increased especially in some Distill Models with small BatchSize in v0.10.0 compared to v0.9.2

| 字段 | 值 |
| --- | --- |
| Issue | [#21983](https://github.com/vllm-project/vllm/issues/21983) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TTFT increased especially in some Distill Models with small BatchSize in v0.10.0 compared to v0.9.2

### Issue 正文摘录

### Your current environment **After Update (v0.10.0):** **Before Update (v0.9.2):** ### 🐛 Describe the bug When running some distilled models (e.g. **DeepSeek-R1-Distill-Llama-70B(W8A8)** and **DeepSeek-R1-Distill-Qwen-32B(BF16)** ), we observe a significant increase in Time-To-First-Token (TTFT) after upgrading to vLLM v0.10.0 compared to vLLM v0.9.2. The degradation is most pronounced with small batch sizes (**bs=1**), where TTFT increases by **33.28%** to **96.73%** (measured across multiple test cases). However, as the batch size gradually increases to **bs=10**, the TTFT difference diminishes and eventually aligns with the performance of the previous version (v0.9.2). If **benchmark code** or **additional testing** is needed to investigate this issue, feel free to contact me. ### Example Case: DeepSeek-R1-Distill-Llama-70B-quantized.w8a8 **Before Update:** Server Log: ``` (vllm092) root@test:/workspace$ vllm serve /root/models/neuralmagic/DeepSeek-R1-Distill-Llama-70B-quantized.w8a8 --tensor-parallel-size 4 --max-num-seqs 1 --max-model-len 10240 --trust-remote-code --gpu-memory-utilization 0.9 INFO 07-25 09:36:40 [__init__.py:244] Automatically detected platform cuda. INFO 0...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: me Distill Models with small BatchSize in v0.10.0 compared to v0.9.2 bug;stale ### Your current environment **After Update (v0.10.0):** **Before Update (v0.9.2):** ### 🐛 Describe the bug When running some distilled mode...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: TTFT increased especially in some Distill Models with small BatchSize in v0.10.0 compared to v0.9.2 bug;stale ### Your current environment **After Update (v0.10.0):** **Before Update (v0.9.2):** ### 🐛 Describe th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: eepSeek-R1-Distill-Llama-70B(W8A8)** and **DeepSeek-R1-Distill-Qwen-32B(BF16)** ), we observe a significant increase in Time-To-First-Token (TTFT) after upgrading to vLLM v0.10.0 compared to vLLM v0.9.2. The degradation...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: TTFT increased especially in some Distill Models with small BatchSize in v0.10.0 compared to v0.9.2 bug;stale ### Your current environment **After Update (v0.10.0):** **Before Update (v0.9.2):** ### 🐛 Describe th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
