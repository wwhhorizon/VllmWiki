# vllm-project/vllm#15277: [Bug]: GGUF model with architecture deepseek2 is not supported yet while vllm version is 0.8.1

| 字段 | 值 |
| --- | --- |
| Issue | [#15277](https://github.com/vllm-project/vllm/issues/15277) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: GGUF model with architecture deepseek2 is not supported yet while vllm version is 0.8.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### I use llama.cpp to merge the unsloth DeepSeek-V3-GGUF Q4_K_M into one merge.gguf and try to serve it: ``` vllm serve ./merge.gguf --tokenizer ../DeepSeek-V3/ --max_model_len 102400 --gpu-memory-utilization 0.9 --tensor-parallel-size 5 ``` Then I get error below ``` Traceback (most recent call last): File "/home/purui/env/a100env/bin/vllm", line 8, in sys.exit(main()) File "/home/purui/env/a100env/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/home/purui/env/a100env/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 33, in cmd uvloop.run(run_server(args)) File "/home/purui/env/a100env/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/home/purui/env/a100env/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper return await main File "/home/purui/env/a100env/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1012, in run_server async with build_async_engine_client(args) as e...

## 现有链接修复摘要

#13167 [Model] Deepseek GGUF support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : GGUF model with architecture deepseek2 is not supported yet while vllm version is 0.8.1 bug ### Your current environment ### 🐛 Describe the bug ### I use llama.cpp to merge the unsloth DeepSeek-V3-GGUF Q4_K_M into one...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GGUF model with architecture deepseek2 is not supported yet while vllm version is 0.8.1 bug ### Your current environment ### 🐛 Describe the bug ### I use llama.cpp to merge the unsloth DeepSeek-V3-GGUF Q4_K_M int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: GGUF model with architecture deepseek2 is not supported yet while vllm version is 0.8.1 bug ### Your current environment ### 🐛 Describe the bug ### I use llama.cpp to merge the unsloth DeepSeek-V3-GGUF Q4_K_M int...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 0/site-packages/vllm/entrypoints/cli/main.py", line 75, in main args.dispatch_function(args) File "/home/purui/env/a100env/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 33, in cmd uvloop.run(run_serv...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: vironment ### 🐛 Describe the bug ### I use llama.cpp to merge the unsloth DeepSeek-V3-GGUF Q4_K_M into one merge.gguf and try to serve it: ``` vllm serve ./merge.gguf --tokenizer ../DeepSeek-V3/ --max_model_len 102400 -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#13167](https://github.com/vllm-project/vllm/pull/13167) | mentioned | 0.45 | [Model] Deepseek GGUF support  | vllm v0.8.0 claimed that add unsloth deepseek gguf model support at #13167 and this issue has been discussed before. as my current vllm version is 0.8.1, i still encounter same is… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
