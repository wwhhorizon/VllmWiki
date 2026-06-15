# vllm-project/vllm#21603: [Bug]: DeepEP with Qwen3-Coder Fails

| 字段 | 值 |
| --- | --- |
| Issue | [#21603](https://github.com/vllm-project/vllm/issues/21603) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepEP with Qwen3-Coder Fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Reproduce Script ```shell VLLM_ALL2ALL_BACKEND=deepep_low_latency VLLM_USE_DEEP_GEMM=1 vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --disable-log-requests --tensor-parallel-size 1 --enable-expert-parallel --data-parallel-size 8 ``` ## Error Info ``` (EngineCore_2 pid=399817) File "/jeejee/miniconda3/envs/jeejee/lib/python3.11/site-packages/torch/_ops.py", line 756, in __call__ [69/1918] (EngineCore_2 pid=399817) return self._op(*args, **kwargs) (EngineCore_2 pid=399817) ^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_2 pid=399817) File "/jeejee/Code/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1594, in moe_forward (EngineCore_2 pid=399817) return self.forward_impl(hidden_states, router_logits) (EngineCore_2 pid=399817) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_2 pid=399817) File "/jeejee/Code/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1493, in forward_impl (EngineCore_2 pid=399817) return self.forward_impl_chunked(hidden_states, router_logits) (EngineCore_2 pid=399817) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_2 pid=399817) File "/jeejee/Code/vllm/vllm/model_e...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: ce Script ```shell VLLM_ALL2ALL_BACKEND=deepep_low_latency VLLM_USE_DEEP_GEMM=1 vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --disable-log-requests --tensor-parallel-size 1 --enable-expert-parallel --data-parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization cuda;fp8;moe;operator;quantization;triton build_error dtype;env_depe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ency VLLM_USE_DEEP_GEMM=1 vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --disable-log-requests --tensor-parallel-size 1 --enable-expert-parallel --data-parallel-size 8 ``` ## Error Info ``` (EngineCore_2 pid=399817...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nt ### 🐛 Describe the bug ## Reproduce Script ```shell VLLM_ALL2ALL_BACKEND=deepep_low_latency VLLM_USE_DEEP_GEMM=1 vllm serve Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --disable-log-requests --tensor-parallel-size 1 --en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
