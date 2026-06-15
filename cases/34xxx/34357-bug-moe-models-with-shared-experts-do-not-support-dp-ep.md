# vllm-project/vllm#34357: [Bug]: MoE models with shared experts do not support DP+EP

| 字段 | 值 |
| --- | --- |
| Issue | [#34357](https://github.com/vllm-project/vllm/issues/34357) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MoE models with shared experts do not support DP+EP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When launching the DS32 model using DP8+EP, the following error is raised. It looks like this error was introduced by https://github.com/vllm-project/vllm/pull/32344 ```bash (EngineCore_DP4 pid=444654) File "/mnt/ephemeral/vllm/.venv/lib/python3.12/site-packages/torch/_inductor/utils.py", line 3220, in run (EngineCore_DP4 pid=444654) out = model(new_inputs) (EngineCore_DP4 pid=444654) ^^^^^^^^^^^^^^^^^ (EngineCore_DP4 pid=444654) File "/mnt/ephemeral/tmp_build/torchinductor_ubuntu/ev/cevy5utq4cbawggmc2bfe5fbgentx6v6g5wgpnlpecxhnm7viccx.py", line 1803, in call (EngineCore_DP4 pid=444654) buf12 = torch.ops.vllm.moe_forward_shared.default(buf9, buf10, buf11, 'from_forward_context') (EngineCore_DP4 pid=444654) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP4 pid=444654) File "/mnt/ephemeral/vllm/.venv/lib/python3.12/site-packages/torch/_ops.py", line 819, in __call__ (EngineCore_DP4 pid=444654) return self._op(*args, **kwargs) (EngineCore_DP4 pid=444654) ^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP4 pid=444654) File "/mnt/ephemeral/vllm/vllm/model_executor/layers/fused_moe/runner/defau...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ^^^^^^^^^^^^^^^^^ (EngineCore_DP4 pid=444654) File "/mnt/ephemeral/tmp_build/torchinductor_ubuntu/ev/cevy5utq4cbawggmc2bfe5fbgentx6v6g5wgpnlpecxhnm7viccx.py", line 1803, in call (EngineCore_DP4 pid=444654) buf12 = torch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: MoE models with shared experts do not support DP+EP bug ### Your current environment ### 🐛 Describe the bug When launching the DS32 model using DP8+EP, the following error is raised. It looks like this error was...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pSeek-V3.2 \ -dp 8 \ --enable-expert-parallel \ --all2all-backend pplx \ --no-enable-prefix-caching \ --max-model-len 100000 \ --trust-remote-code ``` ### Before submitting a new issue... - [x] Make sure you already sea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: match the size of tensor b (8192) at non-singleton dimension 0 ``` ## Reproduce code ```python vllm serve deepseek-ai/DeepSeek-V3.2 \ -dp 8 \ --enable-expert-parallel \ --all2all-backend pplx \ --no-enable-prefix-cachin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
