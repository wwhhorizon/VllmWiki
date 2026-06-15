# vllm-project/vllm#37996: [Bug]: Qwen3.5 397B GPTQ model outputs all exclamation points on ROCM

| 字段 | 值 |
| --- | --- |
| Issue | [#37996](https://github.com/vllm-project/vllm/issues/37996) |
| 状态 | open |
| 标签 | bug;rocm;quantization |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 397B GPTQ model outputs all exclamation points on ROCM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm only outputs exclamation points for the Qwen3.5 397B GPTQ model. Following is the log. I tried smaller models like the Qwen 122B model, and no decode error found. The two models have the same structure, so it is confusing. ./vllm_397.sh WARNING 03-24 10:45:08 [gpt_oss_triton_kernels_moe.py:56] Using legacy triton_kernels on ROCm (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:293] (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:293] █ █ █▄ ▄█ (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:293] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.1rc1.dev151+gd3bab5eb0 (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:293] █▄█▀ █ █ █ █ model /models/Qwen3.5-397B-A17B-GPTQ-Int4/snapshots/hash (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:293] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:293] (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:229] non-default args: {'model_tag': '/models/Qwen3.5-397B-A17B-GPTQ-Int4/snapshots/hash', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'api_key': ['xxxxxx'], 'model': '/models/Qwen3.5-397B-A17B-GPTQ-Int4/snapshots/hash', 'dtype': 'float16', 'max_model_len': 8000, 'enf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen3.5 397B GPTQ model outputs all exclamation points on ROCM bug;rocm;quantization ### Your current environment ### 🐛 Describe the bug vllm only outputs exclamation points for the Qwen3.5 397B GPTQ model. Follo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: er pid=1) INFO 03-24 10:45:12 [utils.py:293] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.1rc1.dev151+gd3bab5eb0 (APIServer pid=1) INFO 03-24 10:45:12 [utils.py:293] █▄█▀ █ █ █ █ model /models/Qwen3.5-397B-A17B-GPTQ-Int4/snapshots/ha...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: Qwen3.5 397B GPTQ model outputs all exclamation points on ROCM bug;rocm;quantization ### Your current environment ### 🐛 Describe the bug vllm only outputs exclamation points for the Qwen3.5 397B GPTQ model. Following is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Qwen3.5 397B GPTQ model outputs all exclamation points on ROCM bug;rocm;quantization ### Your current environment ### 🐛 Describe the bug vllm only outputs exclamation points for the Qwen3.5 397B GPTQ model. Follo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ing is the log. I tried smaller models like the Qwen 122B model, and no decode error found. The two models have the same structure, so it is confusing. ./vllm_397.sh WARNING 03-24 10:45:08 [gpt_oss_triton_kernels_moe.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
