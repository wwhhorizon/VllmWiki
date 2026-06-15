# vllm-project/vllm#27340: [Bug]: Qwen3-VL-2B-Instruct vllm推理报错

| 字段 | 值 |
| --- | --- |
| Issue | [#27340](https://github.com/vllm-project/vllm/issues/27340) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-2B-Instruct vllm推理报错

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ------------------COMMEND：----------------------- nohup vllm serve Qwen3-VL-2B-Instruct --port 8088 --served-model-name qwen3vl_2b_dense - -limit-mm-per-prompt.image=24 --limit-mm-per-prompt.video=0 --max-model-len 32768 --mm-encoder-tp-mode data --mm-processor-cache-gb 0 --tensor-parallel-size 8 --enforce_eager --disable-custom-all-reduce --enable-log-requests --uvicorn-log-level info --disable-log-stats > server_qwen3vl_2b_dense.1.log 2>&1 & ------------------LOG：-------------------------- Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:01 (APIServer pid=1229872) sys.exit(main()) (APIServer pid=1229872) File "/root/conda/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=1229872) args.dispatch_function(args) (APIServer pid=1229872) File "/root/conda/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 57, in cmd (APIServer pid=1229872) uvloop.run(run_server(args)) (APIServer pid=1229872) File "/root/conda/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run (APIServer pid=1229872) return loop.run_until_complete(wrapper()) (APIServer pid=1229872)...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-VL-2B-Instruct vllm推理报错 bug;stale ### Your current environment ### 🐛 Describe the bug ------------------COMMEND：----------------------- nohup vllm serve Qwen3-VL-2B-Instruct --port 8088 --served-model-name...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: , line 1902, in run_server_worker (APIServer pid=1229872) async with build_async_engine_client( (APIServer pid=1229872) File "/root/conda/lib/python3.10/contextlib.py", line 199, in __aenter__ (APIServer pid=1229872) re...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rypoints/cli/main.py", line 54, in main (APIServer pid=1229872) args.dispatch_function(args) (APIServer pid=1229872) File "/root/conda/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 57, in cmd (APISer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: {} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3-VL-2B-Instruct vllm推理报错 bug;stale ### Your current environment ### 🐛 Describe the bug ------------------COMMEND：----------------------- nohup vllm serve Qwen3-VL-2B-Instruct --port 8088 --served-model-name...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
