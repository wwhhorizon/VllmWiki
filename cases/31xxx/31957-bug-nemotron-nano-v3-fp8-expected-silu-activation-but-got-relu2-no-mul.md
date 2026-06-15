# vllm-project/vllm#31957: [Bug]: Nemotron Nano V3 FP8 - Expected 'silu' activation but got relu2_no_mul

| 字段 | 值 |
| --- | --- |
| Issue | [#31957](https://github.com/vllm-project/vllm/issues/31957) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nemotron Nano V3 FP8 - Expected 'silu' activation but got relu2_no_mul

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running `vllm serve` with this model fails: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 vLLM commit: https://github.com/vllm-project/vllm/commit/791b2fc30a25cc48e06a6bd7ce4fd62d765ac004 Command: ``` export MODEL_PATH=/hf_models/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8/ vllm serve $MODEL_PATH --served-model-name my_model --trust-remote-code --no-enable-prefix-caching --tensor-parallel-size 1 ``` Error message: ``` (EngineCore_DP0 pid=3425608) File "/my_home/workspace/my_vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2102, in moe_forward_shared (EngineCore_DP0 pid=3425608) return self.forward_impl(hidden_states, router_logits) (EngineCore_DP0 pid=3425608) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=3425608) File "/my_home/workspace/my_vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1951, in forward_impl (EngineCore_DP0 pid=3425608) final_hidden_states = self.quant_method.apply( (EngineCore_DP0 pid=3425608) ^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=3425608) File "/my_home/workspace/my_vllm/vllm/model_executor/layers/quantization/modelopt.py", line 948, in apply (E...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n answer lots of frequently asked questions. correctness activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding activa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Nemotron Nano V3 FP8 - Expected 'silu' activation but got relu2_no_mul bug ### Your current environment ### 🐛 Describe the bug Running `vllm serve` with this model fails: https://huggingface.co/nvidia/NVIDIA-Nemo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t environment ### 🐛 Describe the bug Running `vllm serve` with this model fails: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 vLLM commit: https://github.com/vllm-project/vllm/commit/791b2fc30a25cc48...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 608) File "/my_home/workspace/my_vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2102, in moe_forward_shared (EngineCore_DP0 pid=3425608) return self.forward_impl(hidden_states, router_logits) (EngineCore_DP0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 253 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
