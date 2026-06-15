# vllm-project/vllm#18955: [Bug]: Under high concurrency, kvcache will be tampered with, causing duplicate characters or gibberish in subsequent request results

| 字段 | 值 |
| --- | --- |
| Issue | [#18955](https://github.com/vllm-project/vllm/issues/18955) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Under high concurrency, kvcache will be tampered with, causing duplicate characters or gibberish in subsequent request results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We found that under high concurrent requests, some requests returned duplicate characters. By checking the kvcache content during the running process, we found that this was caused by the kvcache being modified during the request process, and the subsequent requests used the wrong kvcache. The launch script，we use 64 concurrent: ```bash clear export CUDA_VISIBLE_DEVICES=7 export VLLM_USE_V1=0 vllm serve Qwen3-32B --enforce-eager\ --gpu-memory-utilization 0.95 --tensor-parallel-size 1 \ --max-model-len 32000 --port 34007 --served-model-name chat \ --swap-space 0 --enable-chunked-prefill --enable-prefix-caching ``` Each request content is the following format (the uuid used to avoid influence of prefix cache): ``` {uuid} - {content} ``` We change the `vllm/attention/layer.py/unified_attention_with_output` to record the kvcache chage: ```py import uuid,json process_id = str(uuid.uuid4()) block_recorder = dict() def unified_attention_with_output( query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, output: torch.Tensor, layer_name: str, ) -> None: wait_for_kv_layer_from_connector(layer_name) forward_context: ForwardContext =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: yer.py/unified_attention_with_output` to record the kvcache chage: ```py import uuid,json process_id = str(uuid.uuid4()) block_recorder = dict() def unified_attention_with_output( query: torch.Tensor, key: torch.Tensor,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: the kvcache chage: ```py import uuid,json process_id = str(uuid.uuid4()) block_recorder = dict() def unified_attention_with_output( query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, output: torch.Tensor, laye...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e tampered with, causing duplicate characters or gibberish in subsequent request results bug ### Your current environment ### 🐛 Describe the bug We found that under high concurrent requests, some requests returned dupli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Under high concurrency, kvcache will be tampered with, causing duplicate characters or gibberish in subsequent request results bug ### Your current environment ### 🐛 Describe the bug We found that under high conc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ash clear export CUDA_VISIBLE_DEVICES=7 export VLLM_USE_V1=0 vllm serve Qwen3-32B --enforce-eager\ --gpu-memory-utilization 0.95 --tensor-parallel-size 1 \ --max-model-len 32000 --port 34007 --served-model-name chat \ -...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
