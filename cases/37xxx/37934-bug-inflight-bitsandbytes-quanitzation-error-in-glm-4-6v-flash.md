# vllm-project/vllm#37934: [Bug]: Inflight bitsandbytes quanitzation error in GLM-4.6V-Flash

| 字段 | 值 |
| --- | --- |
| Issue | [#37934](https://github.com/vllm-project/vllm/issues/37934) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inflight bitsandbytes quanitzation error in GLM-4.6V-Flash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am unable to launch VLLM on GLM-4.6V-Flash with [inflight bitsandbytes quantization](https://docs.vllm.ai/en/latest/features/quantization/bnb/#openai-compatible-server): ``` vllm serve zai-org/GLM-4.6V-Flash --port 80 --host 0.0.0.0 --max-model-len 16384 --tensor-parallel-size 2 --quantization bitsandbytes ``` It works just fine without the quantization flag. The error is: ``` (Worker_TP1 pid=1277) INFO 03-23 21:44:18 [bitsandbytes_loader.py:786] Loading weights with BitsAndBytes quantization. May take a while ... (Worker_TP0 pid=1276) INFO 03-23 21:44:18 [bitsandbytes_loader.py:786] Loading weights with BitsAndBytes quantization. May take a while ... Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 25% Completed | 1/4 [00:01<00:04, 1.46s/it] Loading safetensors checkpoint shards: 50% Completed | 2/4 [00:03<00:03, 1.81s/it] Loading safetensors checkpoint shards: 75% Completed | 3/4 [00:05<00:01, 1.97s/it] (Worker_TP1 pid=1277) ERROR 03-23 21:44:25 [multiproc_executor.py:852] WorkerProc failed to start. (Worker_TP1 pid=1277) ERROR 03-23 21:44:25 [multiproc_executor...

## 现有链接修复摘要

#38010 [Model] Fix BitsAndBytes quantization for GLM-4.1V/4.6V-Flash vision encoder

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ): ``` vllm serve zai-org/GLM-4.6V-Flash --port 80 --host 0.0.0.0 --max-model-len 16384 --tensor-parallel-size 2 --quantization bitsandbytes ``` It works just fine without the quantization flag. The error is: ``` (Worke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: executor.py:852] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (Worker_TP1 pid=1277) ERROR 03-23 21:44:25 [multiproc_executor.py:852] return func(*args, **kwargs) (Worker...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency;shape #38010 [Model] Fix BitsAndBytes quantization for GLM-4.1V/4.6V-Flash vision encoder Your cur...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: I am unable to launch VLLM on GLM-4.6V-Flash with [inflight bitsandbytes quantization](https://docs.vllm.ai/en/latest/features/quantization/bnb/#openai-compatible-server): ``` vllm serve zai-org/GLM-4.6V-Flash --port 80...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38010](https://github.com/vllm-project/vllm/pull/38010) | closes_keyword | 0.95 | [Model] Fix BitsAndBytes quantization for GLM-4.1V/4.6V-Flash vision encoder | Fixes #37934 ## Purpose Fix `AssertionError: assert param_data.shape == loaded_weight.shape` crash when loading GLM-4.1V / GLM-4.6V-Flash with BitsAndBytes 4-bit quantization |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
