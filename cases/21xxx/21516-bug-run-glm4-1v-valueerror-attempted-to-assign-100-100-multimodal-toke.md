# vllm-project/vllm#21516: [Bug]: run glm4.1v ,ValueError: Attempted to assign 100 = 100 multimodal tokens to 30000 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#21516](https://github.com/vllm-project/vllm/issues/21516) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: run glm4.1v ,ValueError: Attempted to assign 100 = 100 multimodal tokens to 30000 placeholders

### Issue 正文摘录

### Your current environment os: ubuntu20.4 env: conda cuda: 12.8 and T4 *2 vllm: 0.9.2 transformer: 4.53.3 ### 🐛 Describe the bug vllm serve /mnt/vdb/project/glm4.1v-model --tensor-parallel-size=2 --served-model-name=ui-tars INFO 07-24 17:34:54 [__init__.py:244] Automatically detected platform cuda. INFO 07-24 17:34:57 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-24 17:34:57 [cli_args.py:325] non-default args: {'model': '/mnt/vdb/project/glm4.1v-model', 'served_model_name': ['ui-tars'], 'tensor_parallel_size': 2} INFO 07-24 17:35:04 [config.py:841] This model supports multiple tasks: {'embed', 'reward', 'classify', 'generate'}. Defaulting to 'generate'. WARNING 07-24 17:35:04 [config.py:3320] Your device 'Tesla T4' (with compute capability 7.5) doesn't support torch.bfloat16. Falling back to torch.float16 for compatibility. WARNING 07-24 17:35:04 [config.py:3371] Casting torch.bfloat16 to torch.float16. INFO 07-24 17:35:04 [config.py:1472] Using max model len 65536 WARNING 07-24 17:35:04 [arg_utils.py:1735] Compute Capability sys.exit(main()) ^^^^^^ File "/mnt/vdb/anaconda3/envs/glm4.1v/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 65, in main arg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: platform cuda. INFO 07-24 17:34:57 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-24 17:34:57 [cli_args.py:325] non-default args: {'model': '/mnt/vdb/project/glm4.1v-model', 'served_model_name': ['ui-tars'],...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ur device 'Tesla T4' (with compute capability 7.5) doesn't support torch.bfloat16. Falling back to torch.float16 for compatibility. WARNING 07-24 17:35:04 [config.py:3371] Casting torch.bfloat16 to torch.float16. INFO 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: run glm4.1v ,ValueError: Attempted to assign 100 = 100 multimodal tokens to 30000 placeholders bug ### Your current environment os: ubuntu20.4 env: conda cuda: 12.8 and T4 *2 vllm: 0.9.2 transformer: 4.53.3 ### 🐛...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: placeholders bug ### Your current environment os: ubuntu20.4 env: conda cuda: 12.8 and T4 *2 vllm: 0.9.2 transformer: 4.53.3 ### 🐛 Describe the bug vllm serve /mnt/vdb/project/glm4.1v-model --tensor-parallel-size=2 --se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 1/site-packages/vllm/entrypoints/cli/main.py", line 65, in main args.dispatch_function(args) File "/mnt/vdb/anaconda3/envs/glm4.1v/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 55, in cmd uvloop.run(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
