# vllm-project/vllm#25469: [Bug]: qwen3 next fp8 failed on 4 * L40s, EOFError

| 字段 | 值 |
| --- | --- |
| Issue | [#25469](https://github.com/vllm-project/vllm/issues/25469) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3 next fp8 failed on 4 * L40s, EOFError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug i installed vllm latest in docker vllm-openai:v0.10.2 ``` Successfully installed vllm-0.10.2rc3.dev375+gbabad6e5d.precompiled xgrammar-0.1.24 ``` using model [Qwen/Qwen3-Next-80B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8), launch command is ``` python3 -m vllm.entrypoints.openai.api_server \ --served-model-name qwen3-next-80b-a3b-instruct \ --model /data/model-cache/Qwen3-Next-80B-A3B-Instruct-FP8 \ --tensor-parallel-size 4 \ --enable-expert-parallel ``` error logs ``` (EngineCore_DP0 pid=279) EngineCore failed to start. (EngineCore_DP0 pid=279) Traceback (most recent call last): (EngineCore_DP0 pid=279) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 699, in run_engine_core (EngineCore_DP0 pid=279) engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=279) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=279) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 498, in __init__ (EngineCore_DP0 pid=279) super().__init__(vllm_config, executor_class, log_stats, (EngineCore_DP0 pid=279) File "/usr/local/lib/python3.12/dist-packages/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ror bug;stale ### Your current environment ### 🐛 Describe the bug i installed vllm latest in docker vllm-openai:v0.10.2 ``` Successfully installed vllm-0.10.2rc3.dev375+gbabad6e5d.precompiled xgrammar-0.1.24 ``` using m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: qwen3 next fp8 failed on 4 * L40s, EOFError bug;stale ### Your current environment ### 🐛 Describe the bug i installed vllm latest in docker vllm-openai:v0.10.2 ``` Successfully installed vllm-0.10.2rc3.dev375+gba...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: qwen3 next fp8 failed on 4 * L40s, EOFError bug;stale ### Your current environment ### 🐛 Describe the bug i installed vllm latest in docker vllm-openai:v0.10.2 ``` Successfully installed vllm-0.10.2rc3.dev375+gba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ms that the dynamic shared memory you requested exceeds the limit of the SM89 architecture GPU(100KB). is that the real reason? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: qwen3 next fp8 failed on 4 * L40s, EOFError bug;stale ### Your current environment ### 🐛 Describe the bug i installed vllm latest in docker vllm-openai:v0.10.2 ``` Successfully installed vllm-0.10.2rc3.dev375+gba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
