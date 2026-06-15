# vllm-project/vllm#29317: [Bug]: triton 3.5 for gpt-oss fails on sm11.0a cu130

| 字段 | 值 |
| --- | --- |
| Issue | [#29317](https://github.com/vllm-project/vllm/issues/29317) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: triton 3.5 for gpt-oss fails on sm11.0a cu130

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug triton 3.5.0 on gpt-oss fails: ``` (EngineCore_DP0 pid=19102) File "/opt/local/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/compilation/cuda_graph.py", line 126, in __call__ (EngineCore_DP0 pid=19102) return self.runnable(*args, **kwargs) (EngineCore_DP0 pid=19102) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19102) File "/opt/local/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/compilation/piecewise_backend.py", line 99, in __call__ (EngineCore_DP0 pid=19102) return self.compiled_graph_for_general_shape(*args) (EngineCore_DP0 pid=19102) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19102) File "/opt/local/miniconda3/envs/vllm/lib/python3.12/site-packages/torch/_inductor/standalone_compile.py", line 63, in __call__ (EngineCore_DP0 pid=19102) return self._compiled_fn(*args) (EngineCore_DP0 pid=19102) ^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19102) File "/opt/local/miniconda3/envs/vllm/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 1044, in _fn (EngineCore_DP0 pid=19102) return fn(*args, **kwargs) (EngineCore_DP0 pid=19102) ^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19102...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: n forward_impl (EngineCore_DP0 pid=19102) final_hidden_states = self.quant_method.apply( (EngineCore_DP0 pid=19102) ^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19102) File "/opt/local/miniconda3/envs/vllm/lib/python3.1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: end.py", line 99, in __call__ (EngineCore_DP0 pid=19102) return self.compiled_graph_for_general_shape(*args) (EngineCore_DP0 pid=19102) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=19102) File "/opt/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: triton 3.5 for gpt-oss fails on sm11.0a cu130 bug;unstale ### Your current environment ### 🐛 Describe the bug triton 3.5.0 on gpt-oss fails: ``` (EngineCore_DP0 pid=19102) File "/opt/local/miniconda3/envs/vllm/li...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: , line 926, in call (EngineCore_DP0 pid=19102) buf4 = torch.ops.vllm.moe_forward.default(buf2, buf3, 'model.layers.0.mlp.experts') (EngineCore_DP0 pid=19102) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: triton 3.5 for gpt-oss fails on sm11.0a cu130 bug;unstale ### Your current environment ### 🐛 Describe the bug triton 3.5.0 on gpt-oss fails: ``` (EngineCore_DP0 pid=19102) File "/opt/local/miniconda3/envs/vllm/li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
