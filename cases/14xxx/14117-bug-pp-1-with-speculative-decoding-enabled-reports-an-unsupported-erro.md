# vllm-project/vllm#14117: [Bug]: PP > 1 with speculative decoding enabled reports an unsupported error

| 字段 | 值 |
| --- | --- |
| Issue | [#14117](https://github.com/vllm-project/vllm/issues/14117) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PP > 1 with speculative decoding enabled reports an unsupported error

### Issue 正文摘录

### Your current environment Hi all, I try to use speculative decoding with tp=8 and pp=2 on the 2 x 8H20 testbed, with following command: ``` vllm serve /vllm-workspace/DeepSeek-R1/ \ --host 0.0.0.0 \ --port 8081 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.8 \ --max-num-seqs 16 \ --max-model-len 32768 \ --served-model-name deepseek_r1 \ --device cuda \ --quantization fp8 \ --trust-remote-code \ --num-speculative-tokens 1 ``` But it reports the error: ``` INFO 02-28 00:11:01 [config.py:334] Overriding HF config with Traceback (most recent call last): File "/root/anaconda3/envs/vllm/bin/vllm", line 8, in sys.exit(main()) File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 34, in cmd uvloop.run(run_server(args)) File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/root/anaconda3/envs/vllm/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper return...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --served-model-name deepseek_r1 \ --device cuda \ --quantization fp8 \ --trust-remote-code \ --num-speculative-tokens 1 ``` But it reports the error: ``` INFO 02-28 00:11:01 [config.py:334] Overriding HF config with Tra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: --gpu-memory-utilization 0.8 \ --max-num-seqs 16 \ --max-model-len 32768 \ --served-model-name deepseek_r1 \ --device cuda \ --quantization fp8 \ --trust-remote-code \ --num-speculative-tokens 1 ``` But it reports the e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l-len 32768 \ --served-model-name deepseek_r1 \ --device cuda \ --quantization fp8 \ --trust-remote-code \ --num-speculative-tokens 1 ``` But it reports the error: ``` INFO 02-28 00:11:01 [config.py:334] Overriding HF c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: PP > 1 with speculative decoding enabled reports an unsupported error bug ### Your current environment Hi all, I try to use speculative decoding with tp=8 and pp=2 on the 2 x 8H20 testbed, with following command:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 34, in cmd uvloop.run(run_server(args)) File "/root/anaconda3/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
