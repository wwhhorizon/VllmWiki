# vllm-project/vllm#41027: [Bug]: can't run deepseek v4 flash

| 字段 | 值 |
| --- | --- |
| Issue | [#41027](https://github.com/vllm-project/vllm/issues/41027) |
| 状态 | open |
| 标签 | bug;DSv4 |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can't run deepseek v4 flash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` VLLM_USE_MODELSCOPE=true VLLM_DISABLE_DEEP_GEMM=1 vllm serve /mnt/nvme1n1/DeepSeek-V4-Flash/hub/models/deepseek-ai/DeepSeek-V4-Flash\ --served-model-name "DeepSeek-V4-Flash" \ --gpu-memory-utilization 0.96 \ --trust-remote-code \ --tensor-parallel-size $(ls /proc/driver/nvidia/gpus | wc -l) \ --kv-cache-dtype fp8 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 \ --disable-custom-all-reduce \ --enforce-eager \ --host 0.0.0.0 \ --port 8000 (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:299] (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.20.0 (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:299] █▄█▀ █ █ █ █ model /mnt/nvme1n1/DeepSeek-V4-Flash/hub/models/deepseek-ai/DeepSeek-V4-Flash (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:299] (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:233] non-default args: {'model_tag': '/mnt/nvme1n1/DeepSeek-V4-Flash/h...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: or-parallel-size $(ls /proc/driver/nvidia/gpus | wc -l) \ --kv-cache-dtype fp8 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 \ --disable-cus...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d=100113) INFO 04-27 23:39:58 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.20.0 (APIServer pid=100113) INFO 04-27 23:39:58 [utils.py:299] █▄█▀ █ █ █ █ model /mnt/nvme1n1/DeepSeek-V4-Flash/hub/models/deepseek-ai/DeepSeek-V...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor (APIServer pid=100113) INFO 04-27 23:40:06 [scheduler.py:239] Chunked prefill is enabled with max_nu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: l_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=True, quantization=deepseek_v4_fp8, quantization_config=None, enforce_eager=True, enable_return_routed_ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: lable (APIServer pid=100113) INFO 04-27 23:40:06 [model.py:555] Resolved architecture: DeepseekV4ForCausalLM (APIServer pid=100113) INFO 04-27 23:40:06 [model.py:1680] Using max model len 1048576 (APIServer pid=100113)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
