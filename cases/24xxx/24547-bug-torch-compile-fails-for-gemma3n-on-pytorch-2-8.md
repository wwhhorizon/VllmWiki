# vllm-project/vllm#24547: [Bug]: torch.compile fails for Gemma3n on pytorch 2.8

| 字段 | 值 |
| --- | --- |
| Issue | [#24547](https://github.com/vllm-project/vllm/issues/24547) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: torch.compile fails for Gemma3n on pytorch 2.8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run ``` vllm serve google/gemma-3n-E2B-it -tp 1 ``` on torch==2.8.0: ``` (EngineCore_DP0 pid=2805721) File "/data/users/yhshin/gitrepos/vllm/vllm/compilation/backends.py", line 330, in call_module (EngineCore_DP0 pid=2805721) compiler_manager.compile( (EngineCore_DP0 pid=2805721) ^^^^^^^^ (EngineCore_DP0 pid=2805721) File "/data/users/yhshin/gitrepos/vllm/vllm/compilation/backends.py", line 179, in compile (EngineCore_DP0 pid=2805721) compiled_graph, handle = self.compiler.compile( (EngineCore_DP0 pid=2805721) ^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2805721) File "/data/users/yhshin/gitrepos/vllm/vllm/compilation/compiler_interface.py", line 217, in compile (EngineCore_DP0 pid=2805721) compiled_graph.save(path=path, format="unpacked") (EngineCore_DP0 pid=2805721) File "/home/yhshin/uv_env/vllm/lib/python3.12/site-packages/torch/_inductor/standalone_compile.py", line 73, in save (EngineCore_DP0 pid=2805721) assert len(cache_info.aot_autograd_artifacts) == 1, cache_info (EngineCore_DP0 pid=2805721) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2805721) torch._dynamo.exc.BackendCompilerFailed: backend=' ' raised...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: torch.compile fails for Gemma3n on pytorch 2.8 bug;torch.compile ### Your current environment ### 🐛 Describe the bug run ``` vllm serve google/gemma-3n-E2B-it -tp 1 ``` on torch==2.8.0: ``` (EngineCore_DP0 pid=28...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0 pid=2805721) File "/data/users/yhshin/gitrepos/vllm/vllm/compilation/backends.py", line 330, in call_module (EngineCore_DP0 pid=2805721) compiler_manager.compile( (EngineCore_DP0 pid=2805721) ^^^^^^^^ (EngineCore_DP0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: torch.compile fails for Gemma3n on pytorch 2.8 bug;torch.compile ### Your current environment ### 🐛 Describe the bug run ``` vllm serve google/gemma-3n-E2B-it -tp 1 ``` on torch==2.8.0: ``` (EngineCore_DP0 pid=28...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: put ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: torch.compile fails for Gemma3n on pytorch 2.8 bug;torch.compile ### Your current environment ### 🐛 Describe the bug run ``` vllm serve google/gemma-3n-E2B-it -tp 1 ``` on torch==2.8.0: ``` (EngineCore_DP0 pid=28...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
