# vllm-project/vllm#30214: [Bug]: DeepSeek V3.2 on B200 fails with "CUTLASS_MLA is not valid... Reason: ['sparse not supported']"

| 字段 | 值 |
| --- | --- |
| Issue | [#30214](https://github.com/vllm-project/vllm/issues/30214) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.2 on B200 fails with "CUTLASS_MLA is not valid... Reason: ['sparse not supported']"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to deploy `deepseek-ai/DeepSeek-V3.2-Exp` on NVIDIA B200 GPUs using the nightly build of vLLM, the server fails to start. The issue appears to be a conflict in the automatic backend selection logic for Blackwell (B200) GPUs. The system defaults to AttentionBackendEnum.CUTLASS_MLA, but this backend seemingly does not support the sparse attention configuration required by the model. The specific error thrown is: `ValueError: Selected backend AttentionBackendEnum.CUTLASS_MLA is not valid for this configuration. Reason: ['sparse not supported']` I installed vLLM and dependencies using the following instructions: ``` uv pip install vllm --extra-index-url https://wheels.vllm.ai/nightly uv pip install git+https://github.com/deepseek-ai/DeepGEMM.git@v2.1.1.post3 --no-build-isolation ``` Reproduction Command: ``` vllm serve deepseek-ai/DeepSeek-V3.2-Exp \ -dp 8 \ --enable-expert-parallel \ --served-model-name deepseek-v32 \ --host 0.0.0.0 \ --port 1544 \ --max-num-seqs 256 \ --gpu-memory-utilization 0.95 \ --trust-remote-code ``` Observed Error Logs: ``` (venv) @ :~/deployment/deepseek$ vllm serve deepseek-ai/DeepSeek-V3.2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: oy `deepseek-ai/DeepSeek-V3.2-Exp` on NVIDIA B200 GPUs using the nightly build of vLLM, the server fails to start. The issue appears to be a conflict in the automatic backend selection logic for Blackwell (B200) GPUs. T...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: rs. (APIServer pid=1575867) INFO 12-07 17:00:22 [config.py:650] Detected quantization_config.scale_fmt=ue8m0; enabling UE8M0 for DeepGEMM. (APIServer pid=1575867) INFO 12-07 17:00:22 [model.py:624] Resolved architecture...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: DeepSeek V3.2 on B200 fails with "CUTLASS_MLA is not valid... Reason: ['sparse not supported']" bug ### Your current environment ### 🐛 Describe the bug When attempting to deploy `deepseek-ai/DeepSeek-V3.2-Exp` on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DeepSeek V3.2 on B200 fails with "CUTLASS_MLA is not valid... Reason: ['sparse not supported']" bug ### Your current environment ### 🐛 Describe the bug When attempting to deploy `deepseek-ai/DeepSeek-V3.2-Exp` on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Using max model len 163840 (APIServer pid=1575867) INFO 12-07 17:00:22 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=1575867) INFO 12-07 17:00:22 [cuda.py:215] Forcing kv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
