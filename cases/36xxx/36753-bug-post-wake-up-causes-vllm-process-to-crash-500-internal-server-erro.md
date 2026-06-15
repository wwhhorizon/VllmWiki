# vllm-project/vllm#36753: [Bug]: POST /wake_up causes vLLM process to crash. 500 Internal Server Error

| 字段 | 值 |
| --- | --- |
| Issue | [#36753](https://github.com/vllm-project/vllm/issues/36753) |
| 状态 | open |
| 标签 | bug |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | crash;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: POST /wake_up causes vLLM process to crash. 500 Internal Server Error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug So, I am working on putting multiple models on 1 H100 HBM GPU and leverage the vLLM Sleep/Awake feature to serve models. Since my models in question are only being used for batch flow use cases, I do not care of latency or TTFT since I have an upper window on when I can serve the request. My models were served like this: ``` - | # 0. Verify lmcache is available python3 -c "import lmcache; print('lmcache successfully imported')" || { echo "Failed to import lmcache" exit 1 } # 1. Start LMCache Server (Background) echo "Starting LMCache server..." python3 -m lmcache.server 0.0.0.0 8100 cpu & sleep 2 # 2. Start Granite-8B CUDA_VISIBLE_DEVICES=0 vllm serve /mnt/models/granite-8b-code-instruct/models--ibm--granite-8b-code-instruct \ --served-model-name ibm/granite-8b-code-instruct-prashil \ --port 8080 \ --enable-sleep-mode \ --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}' \ --gpu-memory-utilization 0.8 & until curl -s http://localhost:8080/health; do echo "Health Check for granite-8b-code-instruct..." sleep 5 done echo "Evicting 8080 from GPU..." curl -X POST http://localhost:8080/sleep -d '{"level":...

## 现有链接修复摘要

#37065 [Bugfix][sleepmode] Serialize GPU VMM operations to fix sleep/wakeup race condition

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### 🐛 Describe the bug So, I am working on putting multiple models on 1 H100 HBM GPU and leverage the vLLM Sleep/Awake feature to serve models. Since my models in question are only being used for batch flow use cases, I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: of latency or TTFT since I have an upper window on when I can serve the request. My models were served like this: ``` - | # 0. Verify lmcache is available python3 -c "import lmcache; print('lmcache successfully imported...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: - | # 0. Verify lmcache is available python3 -c "import lmcache; print('lmcache successfully imported')" || { echo "Failed to import lmcache" exit 1 } # 1. Start LMCache Server (Background) echo "Starting LMCache s
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ronment ### 🐛 Describe the bug So, I am working on putting multiple models on 1 H100 HBM GPU and leverage the vLLM Sleep/Awake feature to serve models. Since my models in question are only being used for batch flow use...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: m(APIServer pid=68)[0;0m INFO 03-11 07:18:31 [entrypoints/.../sleep/api_router.py:38] wake up the engine with tags: None [0;36m(APIServer pid=68)[0;0m INFO: 127.0.0.1:33724 - "POST /wake_up HTTP/1.1" 500 Internal Ser...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37065](https://github.com/vllm-project/vllm/pull/37065) | closes_keyword | 0.95 | [Bugfix][sleepmode] Serialize GPU VMM operations to fix sleep/wakeup race condition | Fixes #36753 This PR addresses a critical race condition in vLLM V1's sleep and wake_up transitions when multiple engine instances share the same GPU. ### Problem In vLLM V1, ind |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
