# vllm-project/vllm#25148: [Bug]: nccl allReduce error since v0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#25148](https://github.com/vllm-project/vllm/issues/25148) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nccl allReduce error since v0.10.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **HARDWARE:** 8x RTX 3070 split in two nodes (4x | 4x) **RUNTIME:** docker image: rayproject/ray:2.48.0-py312-gpu **VLLM COMMAND:** vllm serve QuantTrio/Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 --served-model-name=qwen --host=0.0.0.0 --port=80 --load-format=auto --distributed-executor-backend ray --pipeline-parallel-size=2 --tensor-parallel-size=4 --gpu-memory-utilization=0.8 --max-model-len=8000 --swap-space=0 --enable-chunked-prefill --disable-custom-all-reduce --disable-fastapi-docs --trust-remote-code --enable-auto-tool-choice --tool-call-parser=hermes **NOTES:** same everything works fine with **vllm==0.10.1** **OUTPUT:** ``` (EngineCore_DP0 pid=16862) (RayWorkerWrapper pid=11954, ip=10.10.168.253) INFO 09-18 00:55:15 [utils/__init__.py:1433] Found nccl from library libnccl.so.2 (EngineCore_DP0 pid=16862) (RayWorkerWrapper pid=11955, ip=10.10.168.253) INFO 09-18 00:55:15 [distributed/device_communicators/pynccl.py:70] vLLM is using nccl==2.27.3 (EngineCore_DP0 pid=16862) (RayWorkerWrapper pid=17032) DEBUG 09-18 00:55:15 [distributed/device_communicators/shm_broadcast.py:243] Binding to ipc:///tmp/8a137503-a017-4015-b91b-89cb782...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ug **HARDWARE:** 8x RTX 3070 split in two nodes (4x | 4x) **RUNTIME:** docker image: rayproject/ray:2.48.0-py312-gpu **VLLM COMMAND:** vllm serve QuantTrio/Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 --served-model-name=qwen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ## Your current environment ### 🐛 Describe the bug **HARDWARE:** 8x RTX 3070 split in two nodes (4x | 4x) **RUNTIME:** docker image: rayproject/ray:2.48.0-py312-gpu **VLLM COMMAND:** vllm serve QuantTrio/Qwen3-30B-A3B-I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rayproject/ray:2.48.0-py312-gpu **VLLM COMMAND:** vllm serve QuantTrio/Qwen3-30B-A3B-Instruct-2507-GPTQ-Int8 --served-model-name=qwen --host=0.0.0.0 --port=80 --load-format=auto --distributed-executor-backend ray --pipe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ory-utilization=0.8 --max-model-len=8000 --swap-space=0 --enable-chunked-prefill --disable-custom-all-reduce --disable-fastapi-docs --trust-remote-code --enable-auto-tool-choice --tool-call-parser=hermes **NOTES:** same...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: =qwen --host=0.0.0.0 --port=80 --load-format=auto --distributed-executor-backend ray --pipeline-parallel-size=2 --tensor-parallel-size=4 --gpu-memory-utilization=0.8 --max-model-len=8000 --swap-space=0 --enable-chunked-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
