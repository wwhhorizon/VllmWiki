# vllm-project/vllm#35820: [Bug]: deploy Qwen3.5-27B error

| 字段 | 值 |
| --- | --- |
| Issue | [#35820](https://github.com/vllm-project/vllm/issues/35820) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deploy Qwen3.5-27B error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug use the following command: ``` CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 4 --data-parallel-size 4 --enable-expert-parallel --model /data/models/Qwen3.5-27B --served-model-name Qwen3.5-27B --mm-encoder-tp-mode data --mm-processor-cache-type shm --reasoning-parser qwen3 --enable-prefix-caching --tool-call-parser qwen3_coder --enable-auto-tool-choice --gpu-memory-utilization 0.9 --max_model_len 262144 --port 8060 ``` The errors: ``` (APIServer pid=2104388) Traceback (most recent call last): (APIServer pid=2104388) File " ", line 198, in _run_module_as_main (APIServer pid=2104388) File " ", line 88, in _run_code (APIServer pid=2104388) File "/home/test/miniconda3/envs/vllm-qwen35/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 545, in (APIServer pid=2104388) uvloop.run(run_server(args)) (APIServer pid=2104388) File "/home/test/miniconda3/envs/vllm-qwen35/lib/python3.12/site-packages/uvloop/__init__.py", line 96, in run (APIServer pid=2104388) return __asyncio.run( (APIServer pid=2104388) ^^^^^^^^^^^^^^ (APIServer pid=2104388) File "/home/test/miniconda3/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: p/__init__.py", line 96, in run (APIServer pid=2104388) return __asyncio.run( (APIServer pid=2104388) ^^^^^^^^^^^^^^ (APIServer pid=2104388) File "/home/test/miniconda3/envs/vllm-qwen35/lib/python3.12/asyncio/runners.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: environment ### 🐛 Describe the bug use the following command: ``` CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 4 --data-parallel-size 4 --enable-expert-parallel --mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: deploy Qwen3.5-27B error bug;stale ### Your current environment ### 🐛 Describe the bug use the following command: ``` CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --tensor-parallel-si...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: nai.api_server --tensor-parallel-size 4 --data-parallel-size 4 --enable-expert-parallel --model /data/models/Qwen3.5-27B --served-model-name Qwen3.5-27B --mm-encoder-tp-mode data --mm-processor-cache-type shm --reasonin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: deploy Qwen3.5-27B error bug;stale ### Your current environment ### 🐛 Describe the bug use the following command: ``` CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --tensor-parallel-si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
