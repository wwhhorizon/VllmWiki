# vllm-project/vllm#29138: [Bug]: AttributeError: 'NoneType' object has no attribute 'use_mxfp4_w4a16'

| 字段 | 值 |
| --- | --- |
| Issue | [#29138](https://github.com/vllm-project/vllm/issues/29138) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'NoneType' object has no attribute 'use_mxfp4_w4a16'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Command to reproduce bug: ``` python3 -m vllm.entrypoints.openai.api_server \ --model unsloth/qwen3-30b-a3b-instruct-2507 \ --enable-lora \ --lora-module lora-model=/root/.cache/huggingface/hub/models--myorganization--mymodel/snapshots/mycommitID \ --dtype auto \ --quantization bitsandbytes \ --max-num-seqs 8 \ --max-model-len 20584 \ --gpu-memory-utilization 0.91 \ --chat-template /app/templates/my_chat_template.jinja \ --tensor-parallel-size 2 \ --enable-log-requests \ --enable-log-outputs ``` Stack trace: ``` Loading safetensors checkpoint shards: 0% Completed | 0/16 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 6% Completed | 1/16 [00:02<00:39, 2.66s/it] Loading safetensors checkpoint shards: 12% Completed | 2/16 [00:05<00:35, 2.55s/it] Loading safetensors checkpoint shards: 19% Completed | 3/16 [00:09<00:42, 3.27s/it] Loading safetensors checkpoint shards: 25% Completed | 4/16 [00:12<00:41, 3.42s/it] Loading safetensors checkpoint shards: 31% Completed | 5/16 [00:15<00:36, 3.30s/it] Loading safetensors checkpoint shards: 38% Completed | 6/16 [00:19<00:34, 3.45s/it] Loading safetensors checkpoint shards: 44% Complet...

## 现有链接修复摘要

#29231 Fix: Handle NoneType quant_config in FusedMoE LoRA injection

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: AttributeError: 'NoneType' object has no attribute 'use_mxfp4_w4a16' bug;stale ### Your current environment ### 🐛 Describe the bug Command to reproduce bug: ``` python3 -m vllm.entrypoints.openai.api_server \ --m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: roduce bug: ``` python3 -m vllm.entrypoints.openai.api_server \ --model unsloth/qwen3-30b-a3b-instruct-2507 \ --enable-lora \ --lora-module lora-model=/root/.cache/huggingface/hub/models--myorganization--mymodel/snapsho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: AttributeError: 'NoneType' object has no attribute 'use_mxfp4_w4a16' bug;stale ### Your current environment ### 🐛 Describe the bug Command to reproduce bug: ``` python3 -m vllm.entrypoints.openai.api_server \ --model un...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29231](https://github.com/vllm-project/vllm/pull/29231) | closes_keyword | 0.95 | Fix: Handle NoneType quant_config in FusedMoE LoRA injection | Fixes #29138 ## Test Plan **Verification:** The fix adds a guard clause `if quant_config is not None` before accessing `.use_mxfp4_w4a16`. This defaults to the standard `modular_t |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
