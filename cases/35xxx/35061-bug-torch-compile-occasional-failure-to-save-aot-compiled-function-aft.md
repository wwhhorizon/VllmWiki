# vllm-project/vllm#35061: [Bug]: [torch.compile] occasional failure to save AOT compiled function after successful graph compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#35061](https://github.com/vllm-project/vllm/issues/35061) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [torch.compile] occasional failure to save AOT compiled function after successful graph compilation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Phenomenon I occasionally got the following `unable to save AOT compiled function to ...` warning after a successful `torch.compile` run: ```log ... (Worker_DP0_TP6_DCP6_EP6 pid=1139) INFO 02-22 23:21:09 [backends.py:350] Cache the graph of compile range (1, 32768) for later use (Worker_DP0_TP3_DCP3_EP3 pid=1136) INFO 02-22 23:21:09 [backends.py:350] Cache the graph of compile range (1, 32768) for later use (Worker_DP0_TP1_DCP1_EP1 pid=1134) INFO 02-22 23:21:09 [backends.py:350] Cache the graph of compile range (1, 32768) for later use (EngineCore_DP0 pid=333) INFO 02-22 23:21:42 [shm_broadcast.py:548] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). (Worker_DP0_TP0_DCP0_EP0 pid=1133) INFO 02-22 23:22:09 [backends.py:366] Compiling a graph for compile range (1, 32768) takes 65.20s (Worker_DP0_TP0_DCP0_EP0 pid=1133) INFO 02-22 23:22:09 [monitor.py:35] torch.compile takes 85.78 s in total (Worker_DP0_TP0_DCP0_EP0 pid=1133) INFO 02-22 23:22:09 [decorators.py:575] saving AOT compi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: [torch.compile] occasional failure to save AOT compiled function after successful graph compilation bug;torch.compile ### Your current environment ### 🐛 Describe the bug # Phenomenon I occasionally got the follow...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: run: ```log ... (Worker_DP0_TP6_DCP6_EP6 pid=1139) INFO 02-22 23:21:09 [backends.py:350] Cache the graph of compile range (1, 32768) for later use (Worker_DP0_TP3_DCP3_EP3 pid=1136) INFO 02-22 23:21:09 [backends.py:350]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ty. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -22 23:21:42 [shm_broadcast.py:548] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 82f3e10140ac9c20cdb17fbfd4b84165ea0eb4672c03f59b6daa0f86cf0d2b4/rank_0_0/model (Worker_DP0_TP7_DCP7_EP7 pid=1140) INFO 02-22 23:22:09 [decorators.py:575] saving AOT compiled function to /tmp/cache/vllm/torch_compile_cac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
