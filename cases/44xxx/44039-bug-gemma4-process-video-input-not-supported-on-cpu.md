# vllm-project/vllm#44039: [Bug]: gemma4 _process_video_input not supported on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#44039](https://github.com/vllm-project/vllm/issues/44039) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma4 _process_video_input not supported on CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug gemma4 calls mem_get_info() which fails on the CPU build: ``` INFO 05-29 23:33:27 [model_executor/model_loader/default_loader.py:397] Loading weights took 2.77 seconds INFO 05-29 23:33:30 [v1/worker/cpu_model_runner.py:121] Warming up model for the compilation... INFO 05-29 23:33:30 [v1/worker/gpu_model_runner.py:6136] Encoder cache will be initialized with a budget of 4096 tokens, and profiled with 1 video items of the maximum feature size. WARNING 05-29 23:33:30 [platforms/interface.py:873] Current platform cpu does not have 'mem_get_info' attribute. [rank0]: Traceback (most recent call last): [rank0]: File " ", line 1, in [rank0]: File "/opt/venv/lib/python3.12/site-packages/vllm/entrypoints/llm.py", line 349, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/llm_engine.py", line 170, in from_engine_args [rank0]: return cls( [rank0]: ^^^^ [rank0]: File "/opt/venv/lib/python3.12/site-packages/vllm/v1/engine/llm_engine.py", line 104, in __init__ [rank0]: self.engine_core = EngineCoreClient.make_client( [rank...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gemma4 _process_video_input not supported on CPU bug ### Your current environment ### 🐛 Describe the bug gemma4 calls mem_get_info() which fails on the CPU build: ``` INFO 05-29 23:33:27 [model_executor/model_loa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: # 🐛 Describe the bug gemma4 calls mem_get_info() which fails on the CPU build: ``` INFO 05-29 23:33:27 [model_executor/model_loader/default_loader.py:397] Loading weights took 2.77 seconds INFO 05-29 23:33:30 [v1/worker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 136] Encoder cache will be initialized with a budget of 4096 tokens, and profiled with 1 video items of the maximum feature size. WARNING 05-29 23:33:30 [platforms/interface.py:873] Current platform cpu does not have 'm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ar;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
