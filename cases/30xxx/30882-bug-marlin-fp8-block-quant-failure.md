# vllm-project/vllm#30882: [Bug]: Marlin Fp8 Block Quant Failure

| 字段 | 值 |
| --- | --- |
| Issue | [#30882](https://github.com/vllm-project/vllm/issues/30882) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;moe;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Marlin Fp8 Block Quant Failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash MODEL := "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8" #MODEL := "RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8" launch_marlin: VLLM_TEST_FORCE_FP8_MARLIN=1 VLLM_USE_DEEPGEMM=0 chg run --gpus 1 -- vllm serve {{MODEL}} --enforce-eager --max-model-len 8192 eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:8000/v1/completions,num_concurrent=1000,tokenized_requests=False" ``` Result: ```bash (vllm) [robertgshaw2-redhat@nm-automation-h100-standalone-1-preserve vllm]$ just launch_marlin VLLM_TEST_FORCE_FP8_MARLIN=1 VLLM_USE_DEEPGEMM=0 chg run --gpus 1 -- vllm serve Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 --enforce-eager --max-model-len 8192 Reserved 1 GPU(s): [1] for command execution (APIServer pid=3634068) INFO 12-17 15:54:23 [api_server.py:1259] vLLM API server version 0.13.0rc2.dev185+g00a8d7628 (APIServer pid=3634068) INFO 12-17 15:54:23 [utils.py:253] non-default args: {'model_tag': 'Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8', 'model': 'Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8', 'max_model_len': 8192, 'enforce_eager': True} (APIServer pid=3634068) INFO 12-17 15:54:23 [model.py:...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: er pid=3634068) INFO 12-17 15:54:23 [api_server.py:1259] vLLM API server version 0.13.0rc2.dev185+g00a8d7628 (APIServer pid=3634068) INFO 12-17 15:54:23 [utils.py:253] non-default args: {'model_tag': 'Qwen/Qwen3-Coder-3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Marlin Fp8 Block Quant Failure bug;help wanted;good first issue ### Your current environment ### 🐛 Describe the bug ```bash MODEL := "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8" #MODEL := "RedHatAI/Mixtral-8x7B-Instru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: odel-len 8192 eval: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL}},base_url=http://localhost:8000/v1/completions,num_concurrent=1000,tokenized_requests=False" ``` Result: ```bash (vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t issue ### Your current environment ### 🐛 Describe the bug ```bash MODEL := "Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8" #MODEL := "RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8" launch_marlin: VLLM_TEST_FORCE_FP8_MARLIN=1 VLLM_U...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
