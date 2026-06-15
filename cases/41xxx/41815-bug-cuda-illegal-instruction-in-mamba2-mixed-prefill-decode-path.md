# vllm-project/vllm#41815: [Bug]: CUDA illegal instruction in Mamba2 mixed prefill/decode path

| 字段 | 值 |
| --- | --- |
| Issue | [#41815](https://github.com/vllm-project/vllm/issues/41815) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;moe;multimodal_vlm |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe |
| 症状 | mismatch |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal instruction in Mamba2 mixed prefill/decode path

### Issue 正文摘录

### 🐛 Describe the bug CUDA illegal instruction in Mamba2 mixed prefill/decode path; local fence before decode avoids it I am seeing an intermittent CUDA illegal instruction when running a NemotronH Nano Omni VLM with vLLM V1 on H100s. The error surfaces in `GPUModelRunner._to_list()` at `self.transfer_event.synchronize()`, but the failing kernel appears to be upstream. A very small local workaround appears to make the issue stable: add `torch.cuda.synchronize()` in `MambaMixer2.conv_ssm_forward()` after the prefill SSM-state writeback and before entering the decode branch, only when the batch contains both prefill and decode work. I pushed an annotated commit showing the exact surfaced-error location and the narrow workaround: https://github.com/vllm-project/vllm/commit/6bcdc655a0f8090205be1c08d9e4fbcb3d39ae0f ## Environment - GPU: NVIDIA H100 80GB - vLLM: 0.20.0 / V1 engine - Model: `NemotronH_Nano_VL_V2` - Model type: hybrid Mamba2 + Attention + MoE multimodal VLM - Workload: NeMo-RL GRPO rollout generation - Relevant vLLM settings: - `enforce_eager=True` - `attention_backend='FLASHINFER'` - `mamba_ssm_cache_dtype='float32'` - `max_num_batched_tokens=16384` ## Error The failure...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA illegal instruction in Mamba2 mixed prefill/decode path bug ### 🐛 Describe the bug CUDA illegal instruction in Mamba2 mixed prefill/decode path; local fence before decode avoids it I am seeing an intermitten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: intermittent CUDA illegal instruction when running a NemotronH Nano Omni VLM with vLLM V1 on H100s. The error surfaces in `GPUModelRunner._to_list()` at `self.transfer_event.synchronize()`, but the failing kernel appear...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ration - Relevant vLLM settings: - `enforce_eager=True` - `attention_backend='FLASHINFER'` - `mamba_ssm_cache_dtype='float32'` - `max_num_batched_tokens=16384` ## Error The failure consistently surfaces here: ```text Fi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ce_eager=True` - `attention_backend='FLASHINFER'` - `mamba_ssm_cache_dtype='float32'` - `max_num_batched_tokens=16384` ## Error The failure consistently surfaces here: ```text File ".../vllm/v1/worker/gpu_model_runner.p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: CUDA illegal instruction in Mamba2 mixed prefill/decode path bug ### 🐛 Describe the bug CUDA illegal instruction in Mamba2 mixed prefill/decode path; local fence before decode avoids it I am seeing an intermitten...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
