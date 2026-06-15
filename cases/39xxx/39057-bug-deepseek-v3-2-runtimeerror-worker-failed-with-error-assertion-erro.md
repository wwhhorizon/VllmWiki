# vllm-project/vllm#39057: [Bug]: Deepseek v3.2 RuntimeError: Worker failed with error "Assertion error"

| 字段 | 值 |
| --- | --- |
| Issue | [#39057](https://github.com/vllm-project/vllm/issues/39057) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek v3.2 RuntimeError: Worker failed with error "Assertion error"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run new deepseek but failed: uv run vllm serve deepseek-ai/DeepSeek-V3.2 -dp 8 --enable-expert-parallel how i build the environment: https://github.com/vllm-project/recipes/blob/main/DeepSeek/DeepSeek-V3_2.md error messages ``` (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] hidden_states, last_hidden_states = self._dummy_run( (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] ^^^^^^^^^^^^^^^^ (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] File "/hpfs/mzidni/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] return func(*args, **kwargs) (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] ^^^^^^^^^^^^^^^^^^^^^ (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] File "/hpfs/mzidni/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5477, in _dummy_run (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] outputs = self.model( (...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: pfs/mzidni/.venv/lib/python3.12/site-packages/vllm/compilation/piecewise_backend.py", line 367, in __call__ (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] return range_entry.runnable(*args...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lm serve deepseek-ai/DeepSeek-V3.2 -dp 8 --enable-expert-parallel how i build the environment: https://github.com/vllm-project/recipes/blob/main/DeepSeek/DeepSeek-V3_2.md error messages ``` (Worker_DP5_EP5 pid=2198454)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: es_0_modules_self_attn_modules_mla_attn_modules_o_proj_parameters_weight_scale_inv_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, getitem_8, l_self_modules_layers_modules_0_module...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: File "/hpfs/mzidni/.venv/lib/python3.12/site-packages/vllm/compilation/cuda_graph.py", line 254, in __call__ (Worker_DP5_EP5 pid=2198454) ERROR 04-06 13:20:34 [multiproc_executor.py:963] return self.runnable(*args, **kw...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: but failed: uv run vllm serve deepseek-ai/DeepSeek-V3.2 -dp 8 --enable-expert-parallel how i build the environment: https://github.com/vllm-project/recipes/blob/main/DeepSeek/DeepSeek-V3_2.md error messages ``` (Worker_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
