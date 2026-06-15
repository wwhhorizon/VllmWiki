# vllm-project/vllm#7345: [Bug]:`vllm server` will get some error and `python3 -m vllm.entrypoints.openai.api_server` is correct

| 字段 | 值 |
| --- | --- |
| Issue | [#7345](https://github.com/vllm-project/vllm/issues/7345) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:`vllm server` will get some error and `python3 -m vllm.entrypoints.openai.api_server` is correct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug have download model in local path `/mnt/models`,when i run `vllm serve llava1.5-7b --model /mnt/models/ --trust-remote-code --load-format safetensors --tensor-parallel-size 2 --chat-template template_llava.jinja`, will get error ``` Traceback (most recent call last): File "/usr/local/bin/vllm", line 8, in sys.exit(main()) File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 149, in main args.dispatch_function(args) File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 30, in serve asyncio.run(run_server(args)) File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/usr/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete return future.result() File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 342, in run_server async with build_async_engine_client(args) as async_engine_client: File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ return await anext(self.gen) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 100, in build_async_engine_clie...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g ### Your current environment ### 🐛 Describe the bug have download model in local path `/mnt/models`,when i run `vllm serve llava1.5-7b --model /mnt/models/ --trust-remote-code --load-format safetensors --tensor-parall...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ib/python3.10/dist-packages/vllm/scripts.py", line 149, in main args.dispatch_function(args) File "/usr/local/lib/python3.10/dist-packages/vllm/scripts.py", line 30, in serve asyncio.run(run_server(args)) File "/usr/lib...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lib/python3.10/dist-packages/vllm/scripts.py", line 30, in serve asyncio.run(run_server(args)) File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/usr/lib/python3.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el;frontend_api;hardware_porting;model_support;sampling_logits attention;cuda;operator;sampling;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
