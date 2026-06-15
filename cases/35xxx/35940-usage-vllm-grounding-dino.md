# vllm-project/vllm#35940: [Usage]: vllm 可以部署grounding-dino模型吗

| 字段 | 值 |
| --- | --- |
| Issue | [#35940](https://github.com/vllm-project/vllm/issues/35940) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm 可以部署grounding-dino模型吗

### Issue 正文摘录

### Your current environment 日志 ``` 36m(APIServer pid=3254242)[0;0m INFO 03-04 09:49:44 [api_server.py:1896] vLLM API server version 0.10.2 [1;36m(APIServer pid=3254242)[0;0m INFO 03-04 09:49:44 [utils.py:328] non-default args: {'model_tag': '/appdata/zhangkailin/models/IDEA-Research/grounding-dino-base', 'host': '0.0.0.0', 'port': 8002, 'model': '/appdata/zhangkailin/models/IDEA-Research/grounding-dino-base', 'served_model_name': ['dino']} [1;36m(APIServer pid=3254242)[0;0m Traceback (most recent call last): [1;36m(APIServer pid=3254242)[0;0m File "/home//.conda/envs/vllm/bin/vllm", line 7, in [1;36m(APIServer pid=3254242)[0;0m sys.exit(main()) [1;36m(APIServer pid=3254242)[0;0m ^^^^^^ [1;36m(APIServer pid=3254242)[0;0m File "/home//.conda/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 54, in main [1;36m(APIServer pid=3254242)[0;0m args.dispatch_function(args) [1;36m(APIServer pid=3254242)[0;0m File "/home//.conda/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd [1;36m(APIServer pid=3254242)[0;0m uvloop.run(run_server(args)) [1;36m(APIServer pid=3254242)[0;0m File "/home//.conda/envs/vllm/lib/p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: id=3254242)[0;0m INFO 03-04 09:49:44 [utils.py:328] non-default args: {'model_tag': '/appdata/zhangkailin/models/IDEA-Research/grounding-dino-base', 'host': '0.0.0.0', 'port': 8002, 'model': '/appdata/zhangkailin/model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: =3254242)[0;0m INFO 03-04 09:49:44 [api_server.py:1896] vLLM API server version 0.10.2 [1;36m(APIServer pid=3254242)[0;0m INFO 03-04 09:49:44 [utils.py:328] non-default args: {'model_tag': '/appdata/zhangkailin/model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 8] non-default args: {'model_tag': '/appdata/zhangkailin/models/IDEA-Research/grounding-dino-base', 'host': '0.0.0.0', 'port': 8002, 'model': '/appdata/zhangkailin/models/IDEA-Research/grounding-dino-base', 'served_mode...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: MaxM1ForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BailingMoeForCausalLM', 'BambaForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'Cohere2ForCausal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: main.py", line 54, in main [1;36m(APIServer pid=3254242)[0;0m args.dispatch_function(args) [1;36m(APIServer pid=3254242)[0;0m File "/home//.conda/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
