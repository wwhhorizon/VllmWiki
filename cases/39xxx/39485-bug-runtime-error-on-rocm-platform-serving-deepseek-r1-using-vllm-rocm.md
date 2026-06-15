# vllm-project/vllm#39485: [Bug]: Runtime error on ROCm platform serving Deepseek-R1 using VLLM_ROCM_USE_AITER=1

| 字段 | 值 |
| --- | --- |
| Issue | [#39485](https://github.com/vllm-project/vllm/issues/39485) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Runtime error on ROCm platform serving Deepseek-R1 using VLLM_ROCM_USE_AITER=1

### Issue 正文摘录

### Your current environment ## 🐛 Describe the bug ### Deepseek serve fails during capturing graph When using AITER v0.1.12, the `gemm_a8w8_blockscale` CK kernel raises `RuntimeError: This GEMM is not supported!` during CUDA graph capture. This does not occur with the older AITER version (v0.10.post2). vllm version tested: main branch commit `55d037e2e5cc56c38a1a4a77a15c347fee380c50` when running the following command: ``` export SAFETENSORS_FAST_GPU=1 export VLLM_ROCM_USE_AITER=1 export VLLM_USE_V2_MODEL_RUNNER=1 vllm serve deepseek-ai/DeepSeek-R1 \ --tensor-parallel-size 8 \ --trust-remote-code \ --compilation_config.pass_config.fuse_act_quant=false ``` The following error occurs ``` Capturing CUDA graphs (PIECEWISE): 78%|███████▊ | 40/51 [00:40 .226", line 725, in forward (Worker_TP4 pid=11842) ERROR 04-10 06:05:12 [multiproc_executor.py:971] submod_16 = self.submod_16(getitem_18, s72, l_self_modules_layers_modules_3_modules_self_attn_modules_mla_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_3_modules_self_attn_modules_mla_attn_modules_o_proj_parameters_weight_scale_inv_, l_self_modules_layers_modules_3_modules_post_attention_layernorm_parameters_weight_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ed!` during CUDA graph capture. This does not occur with the older AITER version (v0.10.post2). vllm version tested: main branch commit `55d037e2e5cc56c38a1a4a77a15c347fee380c50` when running the following command: ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ls during capturing graph When using AITER v0.1.12, the `gemm_a8w8_blockscale` CK kernel raises `RuntimeError: This GEMM is not supported!` during CUDA graph capture. This does not occur with the older AITER version (v0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: : Runtime error on ROCm platform serving Deepseek-R1 using VLLM_ROCM_USE_AITER=1 bug;rocm ### Your current environment ## 🐛 Describe the bug ### Deepseek serve fails during capturing graph When using AITER v0.1.12, the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Runtime error on ROCm platform serving Deepseek-R1 using VLLM_ROCM_USE_AITER=1 bug;rocm ### Your current environment ## 🐛 Describe the bug ### Deepseek serve fails during capturing graph When using AITER v0.1.12,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: pseek serve fails during capturing graph When using AITER v0.1.12, the `gemm_a8w8_blockscale` CK kernel raises `RuntimeError: This GEMM is not supported!` during CUDA graph capture. This does not occur with the older AI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
