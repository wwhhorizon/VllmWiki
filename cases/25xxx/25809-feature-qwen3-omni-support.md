# vllm-project/vllm#25809: [Feature]: Qwen3 Omni Support

| 字段 | 值 |
| --- | --- |
| Issue | [#25809](https://github.com/vllm-project/vllm/issues/25809) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Qwen3 Omni Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am encountering this when deploying Qwen3 Omni on H200 [service]: INFO 09-27 12:03:27 [__init__.py:216] Automatically detected platform cuda. [service]: [1;36m(APIServer pid=20)[0;0m INFO 09-27 12:03:35 [api_server.py:1839] vLLM API server version 0.11.0rc2.dev33+gc216119d6 [service]: [1;36m(APIServer pid=20)[0;0m INFO 09-27 12:03:35 [utils.py:233] non-default args: {'model_tag': 'Qwen/Qwen3-Omni-30B-A3B-Instruct', 'host': '0.0.0.0', 'port': 8001, 'api_key': ['test-key'], 'model': 'Qwen/Qwen3-Omni-30B-A3B-Instruct', 'trust_remote_code': True, 'enforce_eager': True, 'gpu_memory_utilization': 0.85, 'enable_prefix_caching': True} [service]: [1;36m(APIServer pid=20)[0;0m The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. [service]: [1;36m(APIServer pid=20)[0;0m Traceback (most recent call last): [service]: [1;36m(APIServer pid=20)[0;0m File "/usr/local/bin/vllm", line 10, in [service]: [1;36m(APIServer pid=20)[0;0m sys.exit(main()) [service]: [1;36m(APIServer pid=20)[0;0m ^^^^^^ [service]: [1;36m(APIServer pid=20)[0;0m File "/usr/local/lib/python3.12/dist-packages/vllm/entryp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: Qwen3 Omni Support feature request ### 🚀 The feature, motivation and pitch I am encountering this when deploying Qwen3 Omni on H200 [service]: INFO 09-27 12:03:27 [__init__.py:216] Automatically detected plat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r pid=20)[0;0m INFO 09-27 12:03:35 [api_server.py:1839] vLLM API server version 0.11.0rc2.dev33+gc216119d6 [service]: [1;36m(APIServer pid=20)[0;0m INFO 09-27 12:03:35 [utils.py:233] non-default args: {'model_tag': '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ]: INFO 09-27 12:03:27 [__init__.py:216] Automatically detected platform cuda. [service]: [1;36m(APIServer pid=20)[0;0m INFO 09-27 12:03:35 [api_server.py:1839] vLLM API server version 0.11.0rc2.dev33+gc216119d6 [serv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: y", line 54, in main [service]: [1;36m(APIServer pid=20)[0;0m args.dispatch_function(args) [service]: [1;36m(APIServer pid=20)[0;0m File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: error, The checkpoint you are trying to load has model type `qwen3_omni_moe` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Trans...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
