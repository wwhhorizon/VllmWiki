# vllm-project/vllm#31768: [Bug]: Run RedHatAI/Qwen3-30B-A3B-FP8-block failed

| 字段 | 值 |
| --- | --- |
| Issue | [#31768](https://github.com/vllm-project/vllm/issues/31768) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Run RedHatAI/Qwen3-30B-A3B-FP8-block failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` root@gpu-dev1:/vllm-workspace/test# CUDA_VISIBLE_DEVICES=3 python3 -m vllm.entrypoints.openai.api_server --trust-remote-code --model=/home/wangjiancheng/models/Qwen3-30B-A3B-FP8-block/ (APIServer pid=4354) INFO 01-05 19:53:24 [api_server.py:1351] vLLM API server version 0.13.0 (APIServer pid=4354) INFO 01-05 19:53:24 [utils.py:253] non-default args: {'model': '/home/wangjiancheng/models/Qwen3-30B-A3B-FP8-block/', 'trust_remote_code': True} (APIServer pid=4354) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=4354) INFO 01-05 19:53:24 [model.py:514] Resolved architecture: Qwen3MoeForCausalLM (APIServer pid=4354) INFO 01-05 19:53:24 [model.py:1661] Using max model len 40960 (APIServer pid=4354) INFO 01-05 19:53:25 [scheduler.py:230] Chunked prefill is enabled with max_num_batched_tokens=8192. (EngineCore_DP0 pid=4490) INFO 01-05 19:53:32 [core.py:93] Initializing a V1 LLM engine (v0.13.0) with config: model='/home/wangjiancheng/models/Qwen3-30B-A3B-FP8-block/', speculative_config=None, tokenizer='/home/wangjiancheng/models/Qwen3-30B-A3B-FP8-block/', skip_toke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: erver pid=4354) INFO 01-05 19:53:24 [api_server.py:1351] vLLM API server version 0.13.0 (APIServer pid=4354) INFO 01-05 19:53:24 [utils.py:253] non-default args: {'model': '/home/wangjiancheng/models/Qwen3-30B-A3B-FP8-b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Run RedHatAI/Qwen3-30B-A3B-FP8-block failed bug ### Your current environment ### 🐛 Describe the bug ``` root@gpu-dev1:/vllm-workspace/test# CUDA_VISIBLE_DEVICES=3 python3 -m vllm.entrypoints.openai.api_server --t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Run RedHatAI/Qwen3-30B-A3B-FP8-block failed bug ### Your current environment ### 🐛 Describe the bug ``` root@gpu-dev1:/vllm-workspace/test# CUDA_VISIBLE_DEVICES=3 python3 -m vllm.entrypoints.openai.api_server --t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Run RedHatAI/Qwen3-30B-A3B-FP8-block failed bug ### Your current environment ### 🐛 Describe the bug ``` root@gpu-dev1:/vllm-workspace/test# CUDA_VISIBLE_DEVICES=3 python3 -m vllm.entrypoints.openai.api_server --t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
