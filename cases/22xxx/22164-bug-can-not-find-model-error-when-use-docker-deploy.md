# vllm-project/vllm#22164: [Bug]: can not find model error when use docker deploy

| 字段 | 值 |
| --- | --- |
| Issue | [#22164](https://github.com/vllm-project/vllm/issues/22164) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can not find model error when use docker deploy

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` sudo docker run --runtime nvidia --gpus '"device=7"' --name my_vllm_container_model_scope -v /home/ubuntu/modelscope:/root/.cache/modelscope --env "HF_HUB_OFFLINE=1" --env "VLLM_USE_MODELSCOPE=True" -p 19000:8000 --ipc=host vllm/vllm-openai:v0.9.1 --model Qwen3-30B-A3B-Thinking-2507 --api-key qweasdzxc --trust-remote-code --enable-auto-tool-choice --tool-call-parser hermes ``` and error is ``` INFO 08-03 19:16:41 [__init__.py:244] Automatically detected platform cuda. INFO 08-03 19:16:46 [api_server.py:1287] vLLM API server version 0.9.1 INFO 08-03 19:16:46 [cli_args.py:309] non-default args: {'api_key': 'qweasdzxc', 'enable_auto_tool_choice': True, 'tool_call_parser': 'hermes', 'model': 'Qwen3-30B-A3B-Thinking-2507', 'trust_remote_code': True} 2025-08-03 19:16:47,111 - modelscope - ERROR - The request model: Qwen3-30B-A3B-Thinking-2507 does not exist! ERROR 08-03 19:16:47 [config.py:114] Error retrieving file list: The request model: Qwen3-30B-A3B-Thinking-2507 does not exist!, retrying 1 of 2 2025-08-03 19:16:49,360 - modelscope - ERROR - The request model: Qwen3-30B-A3B-Thinking-2507 does not exist! ERROR 08-03 19:16:49 [c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: can not find model error when use docker deploy bug ### Your current environment ### 🐛 Describe the bug ``` sudo docker run --runtime nvidia --gpus '"device=7"' --name my_vllm_container_model_scope -v /home/ubunt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: can not find model error when use docker deploy bug ### Your current environment ### 🐛 Describe the bug ``` sudo docker run --runtime nvidia --gpus '"device=7"' --name my_vllm_container_model_scope -v /home/ubunt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` INFO 08-03 19:16:41 [__init__.py:244] Automatically detected platform cuda. INFO 08-03 19:16:46 [api_server.py:1287] vLLM API server version 0.9.1 INFO 08-03 19:16:46 [cli_args.py:309] non-default args: {'api_key': '...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t_remote_code': True} 2025-08-03 19:16:47,111 - modelscope - ERROR - The request model: Qwen3-30B-A3B-Thinking-2507 does not exist! ERROR 08-03 19:16:47 [config.py:114] Error retrieving file list: The request model: Qwe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
