# vllm-project/vllm#36526: [Bug]: DeepSeek hangs with overridden num_hidden_layers

| 字段 | 值 |
| --- | --- |
| Issue | [#36526](https://github.com/vllm-project/vllm/issues/36526) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek hangs with overridden num_hidden_layers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Overidding the number of hidden layers is important for debugging DSV3 on a single GPU - while outputs might be wrong, the shapes are right, which is helpful especially for debugging fusion passes (and used in E2E fusion pass testing). When using `--hf-overrides.num_hidden_layers=4`, Deepseek-v3 fails with the following error: ``` $ vllm serve deepseek-ai/DeepSeek-V3 --hf-overrides.num_hidden_layers=4 --load-format=dummy (APIServer pid=2260246) INFO 03-09 13:38:04 [utils.py:292] (APIServer pid=2260246) INFO 03-09 13:38:04 [utils.py:292] █ █ █▄ ▄█ (APIServer pid=2260246) INFO 03-09 13:38:04 [utils.py:292] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0rc1.dev141+g2347661c4.d20260306 (APIServer pid=2260246) INFO 03-09 13:38:04 [utils.py:292] █▄█▀ █ █ █ █ model deepseek-ai/DeepSeek-V3 (APIServer pid=2260246) INFO 03-09 13:38:04 [utils.py:292] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=2260246) INFO 03-09 13:38:04 [utils.py:292] (APIServer pid=2260246) INFO 03-09 13:38:04 [utils.py:228] non-default args: {'model_tag': 'deepseek-ai/DeepSeek-V3', 'model': 'deepseek-ai/DeepSeek-V3', 'hf_overrides': {'num_hidden_layers': 4}, 'load_format': 'dummy'} (APIServer p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: gging fusion passes (and used in E2E fusion pass testing). When using `--hf-overrides.num_hidden_layers=4`, Deepseek-v3 fails with the following error: ``` $ vllm serve deepseek-ai/DeepSeek-V3 --hf-overrides.num_hidden_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: l_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, quantization=fp8, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nt ### 🐛 Describe the bug Overidding the number of hidden layers is important for debugging DSV3 on a single GPU - while outputs might be wrong, the shapes are right, which is helpful especially for debugging fusion pas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 6) INFO 03-09 13:38:04 [compilation.py:286] Enabled custom fusions: norm_quant, act_quant (EngineCore_DP0 pid=2260746) INFO 03-09 13:38:11 [core.py:103] Initializing a V1 LLM engine (v0.17.0rc1.dev141+g2347661c4.d202603...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Using max model len 163840 (APIServer pid=2260246) INFO 03-09 13:38:04 [scheduler.py:231] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=2260246) INFO 03-09 13:38:04 [vllm.py:754] Asynchrono...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
