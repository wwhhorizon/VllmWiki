# vllm-project/vllm#31648: [Bug][CPU Backend]: torch.compile fails for MoE models on CPU backend with `-dp 2`

| 字段 | 值 |
| --- | --- |
| Issue | [#31648](https://github.com/vllm-project/vllm/issues/31648) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CPU Backend]: torch.compile fails for MoE models on CPU backend with `-dp 2`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running a MoE model on the CPU backend with data parallelism enabled (`-dp 2`) without `--enforce-eager`, torch.compile will failed at `fused_moe/layer.py:forward_impl -> has_flashinfer_trtllm_fused_moe() -> has_flashinfer_moe() -> has_flashinfer()`. ### Reproduction Script ``` export VLLM_LOGGING_LEVEL="DEBUG" export TORCH_LOGS="+dynamo" vllm serve "Qwen/Qwen1.5-MoE-A2.7B-Chat" -dp 2 ``` ### Output Part of the output ``` [0/0] File "/workspace/vllm/vllm/model_executor/models/qwen2_moe.py", line 184, in forward [0/0] final_hidden_states = self.experts( [0/0] File "/workspace/vllm/vllm/model_executor/layers/fused_moe/shared_fused_moe.py", line 84, in forward [0/0] shared_out, fused_out = super().forward( [0/0] File "/workspace/vllm/vllm/model_executor/custom_op.py", line 47, in forward [0/0] return self._forward_method(*args, **kwargs) [0/0] File "/workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1707, in forward_native [0/0] shared_output, fused_output = self.forward_impl( [0/0] File "/workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1902, in forward_impl [0/0] has_flashinfer_trtllm_fuse...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug][CPU Backend]: torch.compile fails for MoE models on CPU backend with `-dp 2` bug;cpu ### Your current environment ### 🐛 Describe the bug When running a MoE model on the CPU backend with data parallelism enabled (`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][CPU Backend]: torch.compile fails for MoE models on CPU backend with `-dp 2` bug;cpu ### Your current environment ### 🐛 Describe the bug When running a MoE model on the CPU backend with data parallelism enabled (`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the bug When running a MoE model on the CPU backend with data parallelism enabled (`-dp 2`) without `--enforce-eager`, torch.compile will failed at `fused_moe/layer.py:forward_impl -> has_flashinfer_trtllm_fused_moe() -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ns. correctness ci_build;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;moe;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your cur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][CPU Backend]: torch.compile fails for MoE models on CPU backend with `-dp 2` bug;cpu ### Your current environment ### 🐛 Describe the bug When running a MoE model on the CPU backend with data parallelism enabled (`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
