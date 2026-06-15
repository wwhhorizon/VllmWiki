# vllm-project/vllm#33883: [Bug]: DeepSeek-V3.2 NVFP4 with fp8 kvcache reports `src_cache must be uint8`

| 字段 | 值 |
| --- | --- |
| Issue | [#33883](https://github.com/vllm-project/vllm/issues/33883) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.2 NVFP4 with fp8 kvcache reports `src_cache must be uint8`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start vllm with: ``` vllm serve --port=35496 --gpu-memory-utilization=0.85 --kv-cache-dtype=fp8 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --enable-sleep-mode --model /root/workspaces/models/DeepSeek-V3.2-NVFP4 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda"}' -tp 2 -dp 2 -dpl 2 -dpa 10.0.8.12 -dpr 0 ``` When testing with completions, is reports: ``` ^[[0;36m(EngineCore_DP0 pid=2892713)^[[0;0m ERROR 02-05 07:19:46 [core.py:968] File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/engine/core.py", line 1019, in _process_engine_step^M ^[[0;36m(EngineCore_DP0 pid=2892713)^[[0;0m ERROR 02-05 07:19:46 [core.py:968] outputs, model_executed = self.step_fn()^M ^[[0;36m(EngineCore_DP0 pid=2892713)^[[0;0m ERROR 02-05 07:19:46 [core.py:968] ^^^^^^^^^^^^^^^M ^[[0;36m(EngineCore_DP0 pid=2892713)^[[0;0m ERROR 02-05 07:19:46 [core.py:968] File "/root/workspaces/kebe/vllm-824058076c56164a3772a5f5829bd9662507e5a3/vllm/v1/engine/core.py", line 486, in step_with_batch_queue^M ^[[0;36m(EngineCore_DP0 pid=2892713)^[[0;0m ERROR 02-05 07:19:46 [core.py:968]...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: DeepSeek-V3.2 NVFP4 with fp8 kvcache reports `src_cache must be uint8` bug ### Your current environment ### 🐛 Describe the bug start vllm with: ``` vllm serve --port=35496 --gpu-memory-utilization=0.85 --kv-cache...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cuda"}' -tp 2 -dp 2 -dpl 2 -dpa 10.0.8.12 -dpr 0 ``` When testing with completions, is reports: ``` ^[[0;36m(EngineCore_DP0 pid=2892713)^[[0;0m ER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: izer-mode=deepseek_v32 --no-enable-expert-parallel --enable-sleep-mode --model /root/workspaces/models/DeepSeek-V3.2-NVFP4 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_buffer_device":"cu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: tion=0.85 --kv-cache-dtype=fp8 --tokenizer-mode=deepseek_v32 --no-enable-expert-parallel --enable-sleep-mode --model /root/workspaces/models/DeepSeek-V3.2-NVFP4 --kv-transfer-config '{"kv_connector":"NixlConnector","kv_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: allel;frontend_api;model_support;moe;quantization cuda;fp8;moe dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
