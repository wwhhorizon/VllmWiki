# vllm-project/vllm#12522: [Bug]: Error Using V1 Engine with DeepSeek Llama 70B

| 字段 | 值 |
| --- | --- |
| Issue | [#12522](https://github.com/vllm-project/vllm/issues/12522) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error Using V1 Engine with DeepSeek Llama 70B

### Issue 正文摘录

### Your current environment Vllm 0.7.0 CUDA 12.6 Driver Version 560.94 torch 2.5.1 transformers 4.46.0 ### Model Input Dumps Traceback (most recent call last): File "/home/nd600/miniconda3/envs/vllm/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/home/nd600/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/scripts.py", line 201, in main args.dispatch_function(args) File "/home/nd600/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server(args)) File "/home/nd600/miniconda3/envs/vllm/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/home/nd600/miniconda3/envs/vllm/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/home/nd600/miniconda3/envs/vllm/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/home/nd600/miniconda3/envs/vllm/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/home/nd600/miniconda3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Llama 70B bug ### Your current environment Vllm 0.7.0 CUDA 12.6 Driver Version 560.94 torch 2.5.1 transformers 4.46.0 ### Model Input Dumps Traceback (most recent call last): File "/home/nd600/miniconda3/envs/vllm/bin/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Error Using V1 Engine with DeepSeek Llama 70B bug ### Your current environment Vllm 0.7.0 CUDA 12.6 Driver Version 560.94 torch 2.5.1 transformers 4.46.0 ### Model Input Dumps Traceback (most recent call last): F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ine with DeepSeek Llama 70B bug ### Your current environment Vllm 0.7.0 CUDA 12.6 Driver Version 560.94 torch 2.5.1 transformers 4.46.0 ### Model Input Dumps Traceback (most recent call last): File "/home/nd600/minicond...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.12/site-packages/vllm/scripts.py", line 201, in main args.dispatch_function(args) File "/home/nd600/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/scripts.py", line 42, in serve uvloop.run(run_server(...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ost 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1234 --num-scheduler-steps 8 --max-model-len 16000 When I set the env to use V1 engine i got the above error. When I don't set to V1, it runs fine. I would appreci...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
