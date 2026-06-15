# vllm-project/vllm#19257: [Bug]: PermissionError when loading Qwen2.5 model due to empty command path in subprocess

| 字段 | 值 |
| --- | --- |
| Issue | [#19257](https://github.com/vllm-project/vllm/issues/19257) |
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

> [Bug]: PermissionError when loading Qwen2.5 model due to empty command path in subprocess

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** When loading Qwen-2.5-7B-Instruct model, vLLM fails with PermissionError: [Errno 13] Permission denied: '' during model architecture inspection. The error occurs in registry.py when spawning a subprocess, where sys.executable unexpectedly resolves to an empty string in the subprocess context. Here is my script: ``` export CUDA_VISIBLE_DEVICES=1 export PYTHONPATH="/data6/fanbingbing02/.conda/envs/NLPHW/bin/python" export VLLM_LOGGING_LEVEL=DEBUG MODELNAME="Qwen-2.5-7B-Instruct" USER="fbb" exec -a "vllm-$MODELNAME@$USER" $PYTHONPATH -m vllm.entrypoints.openai.api_server \ --api-key fiblab@fbb \ --model /data6/fanbingbing02/NLP-hw/data/model/Qwen-2.5-7B-Instruct \ --port 23198 \ --host 0.0.0.0 \ --gpu-memory-utilization 0.95 ``` Here is the error message I got: ``` (NLPHW) fanbingbing02@LM1:~$ bash /data6/fanbingbing02/NLP-hw/vllm-serve.sh DEBUG 06-06 15:16:09 [__init__.py:31] No plugins for group vllm.platform_plugins found. DEBUG 06-06 15:16:09 [__init__.py:35] Checking if TPU platform is available. DEBUG 06-06 15:16:09 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' DEBUG 06-06 15...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lugins to load. INFO 06-06 15:16:12 [api_server.py:1289] vLLM API server version 0.9.1.dev205+g90b78ec5 INFO 06-06 15:16:12 [cli_args.py:309] non-default args: {'host': '0.0.0.0', 'port': 23198, 'api_key': 'fiblab@fbb',...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ails with PermissionError: [Errno 13] Permission denied: '' during model architecture inspection. The error occurs in registry.py when spawning a subprocess, where sys.executable unexpectedly resolves to an empty string...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: PermissionError when loading Qwen2.5 model due to empty command path in subprocess bug ### Your current environment ### 🐛 Describe the bug **Description:** When loading Qwen-2.5-7B-Instruct model, vLLM fails with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
