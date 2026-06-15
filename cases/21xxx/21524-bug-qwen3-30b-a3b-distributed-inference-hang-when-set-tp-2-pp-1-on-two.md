# vllm-project/vllm#21524: [Bug]: Qwen3-30B-A3B distributed Inference hang when set tp 2 pp 1 on two H100 node

| 字段 | 值 |
| --- | --- |
| Issue | [#21524](https://github.com/vllm-project/vllm/issues/21524) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;moe;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-30B-A3B distributed Inference hang when set tp 2 pp 1 on two H100 node

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use lws to start the server in two node In leader pod: ``` "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=$(LWS_GROUP_SIZE); python3 -m vllm.entrypoints.openai.api_server --max-log-len=200 --model=/models/Qwen/Qwen3-30B-A3B --served-model-name=atom --gpu-memory-utilization=0.9 -tp=2 --port=8080 --root-path=/openai --trust-remote-code --enable-auto-tool-choice --tool-call-parser=hermes" ``` in work pod: ``` bash /vllm-workspace/examples/online_serving/multi-node-serving.sh worker --ray_address=$(LWS_LEADER_ADDRESS) ``` vllm hang at: ``` (RayWorkerWrapper pid=345, ip=10.224.1.180) INFO 07-24 11:24:57 [backends.py:136] Cache the graph of shape None for later use (RayWorkerWrapper pid=345, ip=10.224.1.180) WARNING 07-24 11:25:39 [fused_moe.py:668] Using default MoE config. Performance might be sub-optimal! Config file not found at /usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=128,N=384,device_name=NVIDIA_H100_80GB_HBM3.json (RayWorkerWrapper pid=691) INFO 07-24 11:25:36 [backends.py:148] Compiling a graph for general shape takes 44.78 s (RayWork...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: pper pid=345, ip=10.224.1.180) INFO 07-24 11:26:30 [monitor.py:33] torch.compile takes 54.49 s in total (RayWorkerWrapper pid=691) WARNING 07-24 11:25:39 [fused_moe.py:668] Using default MoE config. Performance might be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Bug]: Qwen3-30B-A3B distributed Inference hang when set tp 2 pp 1 on two H100 node bug ### Your current environment ### 🐛 Describe the bug I use lws to start the server in two node In leader pod: ``` "bash /vllm-workspa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-30B-A3B distributed Inference hang when set tp 2 pp 1 on two H100 node bug ### Your current environment ### 🐛 Describe the bug I use lws to start the server in two node In leader pod: ``` "bash /vllm-worksp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: at: ``` (RayWorkerWrapper pid=345, ip=10.224.1.180) INFO 07-24 11:24:57 [backends.py:136] Cache the graph of shape None for later use (RayWorkerWrapper pid=345, ip=10.224.1.180) WARNING 07-24 11:25:39 [fused_moe.py:668]...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 91) vllm-0:691:12585 [0] INFO 07-24 11:26:32 [kv_cache_utils.py:634] GPU KV cache size: 878,416 tokens INFO 07-24 11:26:32 [kv_cache_utils.py:637] Maximum concurrency for 40,960 tokens per request: 21.45x INFO 07-24 11:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
