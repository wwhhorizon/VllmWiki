# vllm-project/vllm#23278: [Bug]: gpt-oss 120b does not work while gpt-oss 20b works on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#23278](https://github.com/vllm-project/vllm/issues/23278) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpt-oss 120b does not work while gpt-oss 20b works on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash conda create -n vllm python=3.12 conda activate vllm vllm serve openai/gpt-oss-20b ``` The above commands work well, while the following command got error: ```bash vllm serve openai/gpt-oss-120b ``` Seems it was due to VRAM crash, but it said gpt-oss 120b can fit in single H100. Error message: INFO 08-20 18:03:39 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=5710) INFO 08-20 18:03:40 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=5710) INFO 08-20 18:03:40 [utils.py:326] non-default args: {'model_tag': 'openai/gpt-oss-120b', 'model': 'openai/gpt-oss-120b'} (APIServer pid=5710) INFO 08-20 18:03:46 [__init__.py:711] Resolved architecture: GptOssForCausalLM Parse safetensors files: 100%|██████████████████| 15/15 [00:01 (APIServer pid=5710) sys.exit(main()) (APIServer pid=5710) ^^^^^^ (APIServer pid=5710) File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=5710) args.dispatch_function(args) (APIServer pid=5710) File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/serv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: erver pid=5710) INFO 08-20 18:03:40 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=5710) INFO 08-20 18:03:40 [utils.py:326] non-default args: {'model_tag': 'openai/gpt-oss-120b', 'model': 'openai/gpt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: gpt-oss 120b does not work while gpt-oss 20b works on H100 bug;stale ### Your current environment ### 🐛 Describe the bug ```bash conda create -n vllm python=3.12 conda activate vllm vllm serve openai/gpt-oss-20b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss 120b does not work while gpt-oss 20b works on H100 bug;stale ### Your current environment ### 🐛 Describe the bug ```bash conda create -n vllm python=3.12 conda activate vllm vllm serve openai/gpt-oss-20b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: gpt-oss 120b does not work while gpt-oss 20b works on H100 bug;stale ### Your current environment ### 🐛 Describe the bug ```bash conda create -n vllm python=3.12 conda activate vllm vllm serve openai/gpt-oss-20b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: entrypoints/cli/main.py", line 54, in main (APIServer pid=5710) args.dispatch_function(args) (APIServer pid=5710) File "/home/ubuntu/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
