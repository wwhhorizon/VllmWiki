# vllm-project/vllm#32604: [Bug]: LMCache CPU kv offload cause decode speed degrade

| 字段 | 值 |
| --- | --- |
| Issue | [#32604](https://github.com/vllm-project/vllm/issues/32604) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LMCache CPU kv offload cause decode speed degrade

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug performance without lmcache with lm cache both prefill and decode speed degrades this is my config ``` model: models/GLM-4.7-AWQ host: "0.0.0.0" port: 8000 gpu-memory-utilization: 0.90 max-model-len: 202752 tensor-parallel-size: 4 kv-cache-dtype: fp8_e4m3 enable-prefix-caching: true enable-chunked-prefill: true enable-auto-tool-choice: true tool-call-parser: glm47 reasoning-parser: glm45 served-model-name: GLM-4.7-AWQ speculative-config: '{"method":"mtp","num_speculative_tokens":1}' kv-transfer-config: '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}' ``` why LMcache affects decode? I don't think it has anything to do with decode ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: LMCache CPU kv offload cause decode speed degrade bug;stale ### Your current environment ### 🐛 Describe the bug performance without lmcache with lm cache both prefill and decode speed degrades this is my config `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ilization: 0.90 max-model-len: 202752 tensor-parallel-size: 4 kv-cache-dtype: fp8_e4m3 enable-prefix-caching: true enable-chunked-prefill: true enable-auto-tool-choice: true tool-call-parser: glm47 reasoning-parser: glm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ode ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: LMCache CPU kv offload cause decode speed degrade bug;stale ### Your current environment ### 🐛 Describe the bug performance without lmcache with lm cache both prefill and decode speed degrades this is my config `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
