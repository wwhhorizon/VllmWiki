# vllm-project/vllm#7441: [Bug]: base_model.model.score.weight is unsupported LoRA weight

| 字段 | 值 |
| --- | --- |
| Issue | [#7441](https://github.com/vllm-project/vllm/issues/7441) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: base_model.model.score.weight is unsupported LoRA weight

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was trying to deploy llama 3.1 8B Instruct with Lora adapters. The adapter_config is as follows: { "alpha_pattern": {}, "auto_mapping": null, "base_model_name_or_path": "meta-llama/Meta-Llama-3.1-8B-Instruct", "bias": "none", "fan_in_fan_out": false, "inference_mode": true, "init_lora_weights": true, "layer_replication": null, "layers_pattern": null, "layers_to_transform": null, "loftq_config": {}, "lora_alpha": 8, "lora_dropout": 0.05, "megatron_config": null, "megatron_core": "megatron.core", "modules_to_save": [ "classifier", "score" ], "peft_type": "LORA", "r": 16, "rank_pattern": {}, "revision": null, "target_modules": [ "v_proj", "q_proj", "o_proj", "gate_proj", "down_proj", "up_proj", "k_proj" ], "task_type": "SEQ_CLS", "use_dora": false, "use_rslora": false } And the error I was getting is as follows: Exception in callback _log_task_completion(error_callback= >)( ) at /home/yiwang/yi-env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py:37 handle: >)( ) at /home/yiwang/yi-env/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py:37> Traceback (most recent call last): File "/home/lib/python3.10/site-pac...

## 现有链接修复摘要

#42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t But I think those layers are supported for llama 3.1. Thx! correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: base_model.model.score.weight is unsupported LoRA weight bug;stale ### Your current environment ### 🐛 Describe the bug I was trying to deploy llama 3.1 8B Instruct with Lora adapters. The adapter_config is as fol...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ers. The adapter_config is as follows: { "alpha_pattern": {}, "auto_mapping": null, "base_model_name_or_path": "meta-llama/Meta-Llama-3.1-8B-Instruct", "bias": "none", "fan_in_fan_out": false, "inference_mode": true, "i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: base_model.model.score.weight is unsupported LoRA weight bug;stale ### Your current environment ### 🐛 Describe the bug I was trying to deploy llama 3.1 8B Instruct with Lora adapters. The adapter_config is as fol...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-upd...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | pping (<a href="https://redirect.github.com/psf/requests/issues/7441">#7441</a>)</li> <li><a href="https://github.com/psf/requests/commit/b7b549b54571d03950b16afd2d01bc6ff0348224"… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | pping (<a href="https://redirect.github.com/psf/requests/issues/7441">#7441</a>)</li> <li><a href="https://github.com/psf/requests/commit/b7b549b54571d03950b16afd2d01bc6ff0348224"… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | pping (<a href="https://redirect.github.com/psf/requests/issues/7441">#7441</a>)</li> <li><a href="https://github.com/psf/requests/commit/b7b549b54571d03950b16afd2d01bc6ff0348224"… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | pping (<a href="https://redirect.github.com/psf/requests/issues/7441">#7441</a>)</li> <li><a href="https://github.com/psf/requests/commit/b7b549b54571d03950b16afd2d01bc6ff0348224"… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
