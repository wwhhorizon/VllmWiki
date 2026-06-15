# vllm-project/vllm#30269: [Bug]: Multi-node deployment fails with TP=1 and PP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#30269](https://github.com/vllm-project/vllm/issues/30269) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-node deployment fails with TP=1 and PP=2

### Issue 正文摘录

### Your current environment I have a multi-node setup deployed as ray cluster with 2 worker nodes, where each node has 1x L40s. So I am configuring vllm with ` --tensor-parallel-size 1 --pipeline-parallel-size 2 `. This setup was working fine till version 0.11.2. Probably broke already in 0.11.1, but didn't tested that version. The error is not related to the model I deploy, since that error occures over all models I deploy. ### 🐛 Describe the bug I am using the vllm docker container with vllm==v0.12.0. The error occured first in vllm==v0.11.2. I didn't tested vllm==v0.11.1. vllm==v0.11.0 works without any error. Log Output: ```text vllm-worker-node | Starting vllm API server... vllm-worker-node | (APIServer pid=482) INFO 12-08 07:44:22 [api_server.py:1772] vLLM API server version 0.12.0 vllm-worker-node | (APIServer pid=482) INFO 12-08 07:44:22 [utils.py:253] non-default args: {'enable_auto_tool_choice': True, 'tool_call_parser': 'openai', 'model': '/models/openai/gpt-oss-120b', 'served_model_name': ['gpt-oss-120b'], 'pipeline_parallel_size': 2, 'gpu_memory_utilization': 0.95} vllm-worker-node | (APIServer pid=482) INFO 12-08 07:44:27 [model.py:637] Resolved architecture: GptOss...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l-size 1 --pipeline-parallel-size 2 `. This setup was working fine till version 0.11.2. Probably broke already in 0.11.1, but didn't tested that version. The error is not related to the model I deploy, since that error...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: APIServer pid=482) INFO 12-08 07:44:29 [model.py:2086] Downcasting torch.float32 to torch.bfloat16. vllm-worker-node | (APIServer pid=482) INFO 12-08 07:44:29 [model.py:1750] Using max model len 131072 vllm-worker-node...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: as ray cluster with 2 worker nodes, where each node has 1x L40s. So I am configuring vllm with ` --tensor-parallel-size 1 --pipeline-parallel-size 2 `. This setup was working fine till version 0.11.2. Probably broke alr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: n.py", line 73, in main vllm-worker-node | (APIServer pid=482) args.dispatch_function(args) vllm-worker-node | (APIServer pid=482) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 60, i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -node | (APIServer pid=482) INFO 12-08 07:44:27 [model.py:637] Resolved architecture: GptOssForCausalLM vllm-worker-node | (APIServer pid=482) INFO 12-08 07:44:29 [model.py:2086] Downcasting torch.float32 to torch.bfloa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
