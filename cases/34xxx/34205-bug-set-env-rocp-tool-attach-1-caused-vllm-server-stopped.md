# vllm-project/vllm#34205: [Bug]: Set env ROCP_TOOL_ATTACH=1 caused vllm server stopped

| 字段 | 值 |
| --- | --- |
| Issue | [#34205](https://github.com/vllm-project/vllm/issues/34205) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Set env ROCP_TOOL_ATTACH=1 caused vllm server stopped

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I start vllm server by: ``` vllm serve Qwen/Qwen3-0.6B ``` And run the benchmark: ``` vllm bench serve --backend vllm \ --model Qwen/Qwen3-0.6B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /workspace/datasets/ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 10 ``` It runs correctly. But if I set the env: ``` export ROCP_TOOL_ATTACH=1 ``` And then start vllm server ``` vllm serve Qwen/Qwen3-0.6B ``` Then run the benchmark. The vllm serve died with the output: ```shell (EngineCore_DP0 pid=48436) DEBUG 02-10 03:44:18 [v1/worker/gpu_model_runner.py:3375] Running batch with cudagraph_mode: FULL, batch_descriptor: BatchDescriptor(num_tokens=8, nu m_reqs=8, uniform=True, has_lora=False), should_ubatch: False, num_tokens_across_dp: None (EngineCore_DP0 pid=48436) DEBUG 02-10 03:44:18 [v1/worker/gpu_model_runner.py:3396] ubatch_slices: None, ubatch_slices_padded: None (EngineCore_DP0 pid=48436) DEBUG 02-10 03:44:18 [v1/worker/gpu_model_runner.py:3375] Running batch with cudagraph_mode: FULL, batch_descriptor: BatchDescriptor(num_tokens=8, nu m_reqs=8, uniform=True, has_lora=False), should_ubatch: False,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;kernel;operator;triton build_error;crash env_d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Set env ROCP_TOOL_ATTACH=1 caused vllm server stopped bug;rocm ### Your current environment ### 🐛 Describe the bug I start vllm server by: ``` vllm serve Qwen/Qwen3-0.6B ``` And run the benchmark: ``` vllm bench...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nment ### 🐛 Describe the bug I start vllm server by: ``` vllm serve Qwen/Qwen3-0.6B ``` And run the benchmark: ``` vllm bench serve --backend vllm \ --model Qwen/Qwen3-0.6B \ --endpoint /v1/completions \ --dataset-name...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: serve Qwen/Qwen3-0.6B ``` And run the benchmark: ``` vllm bench serve --backend vllm \ --model Qwen/Qwen3-0.6B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /workspace/datasets/ShareGPT_V3_unfi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: I start vllm server by: ``` vllm serve Qwen/Qwen3-0.6B ``` And run the benchmark: ``` vllm bench serve --backend vllm \ --model Qwen/Qwen3-0.6B \ --endpoint /v1/completions \ --dataset-name sharegpt \ --dataset-path /wo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
