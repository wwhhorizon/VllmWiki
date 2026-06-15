# vllm-project/vllm#8388: [Bug]: loading qwen2-vl-7b fails with error: `assert "factor" in rope_scaling`

| 字段 | 值 |
| --- | --- |
| Issue | [#8388](https://github.com/vllm-project/vllm/issues/8388) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: loading qwen2-vl-7b fails with error: `assert "factor" in rope_scaling`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` Traceback (most recent call last): File "/home/anton/personal/transformer-experiments/inference/vllm_multi.py", line 21, in run_server(args) File "/home/anton/personal/transformer-experiments/inference/vllm_multi.py", line 9, in run_server llm = load_model(args.model, 8192, args.gpu) File "/home/anton/personal/transformer-experiments/inference/model.py", line 19, in load_model engine = AsyncLLMEngine.from_engine_args(AsyncEngineArgs( File "/home/anton/personal/transformer-experiments/env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 726, in from_engine_args engine_config = engine_args.create_engine_config() File "/home/anton/personal/transformer-experiments/env/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 844, in create_engine_config model_config = self.create_model_config() File "/home/anton/personal/transformer-experiments/env/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 782, in create_model_config return ModelConfig( File "/home/anton/personal/transformer-experiments/env/lib/python3.10/site-packages/vllm/config.py", line 227, in __init__ self.max_model_len = _get_and_ve...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: loading qwen2-vl-7b fails with error: `assert "factor" in rope_scaling` bug ### Your current environment ### 🐛 Describe the bug ``` Traceback (most recent call last): File "/home/anton/personal/transformer-experi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error;crash env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error;crash env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
