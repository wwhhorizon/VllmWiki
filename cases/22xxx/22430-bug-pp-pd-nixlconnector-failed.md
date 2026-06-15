# vllm-project/vllm#22430: [Bug]: PP+PD NixlConnector failed

| 字段 | 值 |
| --- | --- |
| Issue | [#22430](https://github.com/vllm-project/vllm/issues/22430) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PP+PD NixlConnector failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to use NixlConnector for PD+PP online inference. But I try ray+pp2+tp2 for prefiller, ray+pp2+tp2 for decoder, It failed. And I test PD+Nixlconnector+ray without PP, it works well. Does the current NixL Connector support PD+PP? Prefiller: ```sh UCX_TLS=cuda_ipc,cuda_copy,tcp \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=0,1,2,3 \ VLLM_NIXL_SIDE_CHANNEL_PORT=5559 \ vllm serve $MODEL \ -tp 2\ -pp 2\ --port 8100 \ --gpu-memory-utilization 0.7\ --enforce-eager \ --distributed-executor-backend ray\ --kv-transfer-config \ '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' ``` Decoder: ```sh UCX_TLS=cuda_ipc,cuda_copy,tcp \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=4,5,6,7 \ VLLM_NIXL_SIDE_CHANNEL_PORT=5569 \ vllm serve $MODEL \ --port 8200 \ -tp 2\ -pp 2\ --gpu-memory-utilization 0.7\ --enforce-eager \ --distributed-executor-backend ray\ --kv-transfer-config \ '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...

## 现有链接修复摘要

#22976 [BugFix] pp cannot run successfully under NixlConnector

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: PP+PD NixlConnector failed bug;stale ### Your current environment ### 🐛 Describe the bug I want to use NixlConnector for PD+PP online inference. But I try ray+pp2+tp2 for prefiller, ray+pp2+tp2 for decoder, It fa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tilization 0.7\ --enforce-eager \ --distributed-executor-backend ray\ --kv-transfer-config \ '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' ``` Decoder: ```sh UCX_TLS=cuda_ipc,cuda_copy,tcp \ VLLM_ENABLE_V1_MULT...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cuda;operator;quantization;sampling;triton build_error;crash dtype;env_dependenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Does the current NixL Connector support PD+PP? Prefiller: ```sh UCX_TLS=cuda_ipc,cuda_copy,tcp \ VLLM_ENABLE_V1_MULTIPROCESSING=1 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ CUDA_VISIBLE_DEVICES=0,1,2,3 \ VLLM_NIXL_SIDE_CHAN...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22976](https://github.com/vllm-project/vllm/pull/22976) | mentioned | 0.6 | [BugFix] pp cannot run successfully under NixlConnector | cessfully under NixlConnector ## Purpose I previously raised issue #22430 regarding NixlConnector failing with Pipeline Parallelism (PP) + Prefill-Decode (PD) configurations, but… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
