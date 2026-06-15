# vllm-project/vllm#18875: [Usage]: Does vllm support inference or service startup of CPU small model?

| 字段 | 值 |
| --- | --- |
| Issue | [#18875](https://github.com/vllm-project/vllm/issues/18875) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vllm support inference or service startup of CPU small model?

### Issue 正文摘录

### Your current environment vllm serve /dfs/data/model/bge-m3/ --task embed --trust-remote-code --max-model-len 8192 Using the above command to start in the CPU environment will result in an error： Traceback (most recent call last): File “/dfs/data/miniconda/envs/Qwen2-New/bin/vllm”, line 8, in sys.exit(main()) File “/dfs/data/miniconda/envs/Qwen2-New/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py”, line 53, in main args.dispatch_function(args) File “/dfs/data/miniconda/envs/Qwen2-New/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py”, line 27, in cmd uvloop.run(run_server(args)) File “/dfs/data/miniconda/envs/Qwen2-New/lib/python3.10/site-packages/uvloop/init.py”, line 82, in run return loop.run_until_complete(wrapper()) File “uvloop/loop.pyx”, line 1517, in uvloop.loop.Loop.run_until_complete File “/dfs/data/miniconda/envs/Qwen2-New/lib/python3.10/site-packages/uvloop/init.py”, line 61, in wrapper return await main File “/dfs/data/miniconda/envs/Qwen2-New/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py”, line 1078, in run_server async with build_async_engine_client(args) as engine_client: File “/dfs/data/miniconda/envs/Qwen2-New/lib/python...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: m/entrypoints/openai/api_server.py”, line 1078, in run_server async with build_async_engine_client(args) as engine_client: File “/dfs/data/miniconda/envs/Qwen2-New/lib/python3.10/contextlib.py”, line 199, in aenter retu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Does vllm support inference or service startup of CPU small model? usage;stale ### Your current environment vllm serve /dfs/data/model/bge-m3/ --task embed --trust-remote-code --max-model-len 8192 Using the abo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Does vllm support inference or service startup of CPU small model? usage;stale ### Your current environment vllm serve /dfs/data/model/bge-m3/ --task embed --trust-remote-code --max-model-len 8192 Using the abo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n3.10/site-packages/vllm/entrypoints/cli/main.py”, line 53, in main args.dispatch_function(args) File “/dfs/data/miniconda/envs/Qwen2-New/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py”, line 27, in cmd uvlo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Does vllm support inference or service startup of CPU small model? usage;stale ### Your current environment vllm serve /dfs/data/model/bge-m3/ --task embed --trust-remote-code --max-model-len 8192 Using the above comman...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
