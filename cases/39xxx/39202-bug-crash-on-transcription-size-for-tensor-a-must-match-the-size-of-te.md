# vllm-project/vllm#39202: [Bug]: Crash on Transcription (size for tensor a must match the size of tensor b) with reproduce

| 字段 | 值 |
| --- | --- |
| Issue | [#39202](https://github.com/vllm-project/vllm/issues/39202) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash on Transcription (size for tensor a must match the size of tensor b) with reproduce

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Reproduce Steps 1. Launch vLLM with command: ``` VLLM_DISABLE_COMPILE_CACHE=1 vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --host 0.0.0.0 --port 7899 --quantization fp8 --gpu-memory-utilization 0.25 --max-model-len 10240 --served-model-name model --compilation_config '{"cudagraph_mode": "PIECEWISE"}' ``` 2. Invoke Multiple Times with HTTP `/v1/audio/transcriptions` Endpoint: ``` curl -s -X POST \ -H "Authorization: Bearer $VLLM_API_KEY" \ -H "Content-Type: multipart/form-data" \ -F "file=@/path/to/audio.wav" \ -F "model=$MODEL_ID" \ http://localhost:8000/v1/audio/transcriptions ``` https://docs.vllm.ai/en/latest/contributing/model/transcription/#test-with-the-api 3. After Many Invocations, the system crashes. ### Git commit vLLM commit: latest `a435e3108d82eb96d9b3954c1935afbbf4c5f69b` with pre-compiled binaries. ### Console log ``` (EngineCore pid=47271) WARNING 04-07 18:18:14 [voxtral_realtime.py:310] Realtime model received empty multimodal embeddings for 1 input tokens. Returning zero emb eddings to avoid engine crash. (EngineCore pid=47271) WARNING 04-07 18:18:14 [voxtral_realtime.py:310] Realtime model received em...

## 现有链接修复摘要

#40719 [fix] mismatch dim during capture graph if with --gpu-memory-utilization

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: b39382b2) with config: model='mistralai/Voxtral-M ini-4B-Realtime-2602', speculative_config=None, tokenizer='mistralai/Voxtral-Mini-4B-Realtime-2602', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None , toke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: bug ### Reproduce Steps 1. Launch vLLM with command: ``` VLLM_DISABLE_COMPILE_CACHE=1 vllm serve mistralai/Voxtral-Mini-4B-Realtime-2602 --host 0.0.0.0 --port 7899 --quantization fp8 --gpu-memory-utilization 0.25 --max-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rve mistralai/Voxtral-Mini-4B-Realtime-2602 --host 0.0.0.0 --port 7899 --quantization fp8 --gpu-memory-utilization 0.25 --max-model-len 10240 --served-model-name model --compilation_config '{"cudagraph_mode": "PIECEWISE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 0.0.0 --port 7899 --quantization fp8 --gpu-memory-utilization 0.25 --max-model-len 10240 --served-model-name model --compilation_config '{"cudagraph_mode": "PIECEWISE"}' ``` 2. Invoke Multiple Times with HTTP `/v1/audio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: --max-model-len 10240 --served-model-name model --compilation_config '{"cudagraph_mode": "PIECEWISE"}' ``` 2. Invoke Multiple Times with HTTP `/v1/audio/transcriptions` Endpoint: ``` curl -s -X POST \ -H "Authorization:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40719](https://github.com/vllm-project/vllm/pull/40719) | mentioned | 0.6 | [fix] mismatch dim during capture graph if with --gpu-memory-utilization | c1.dev134+gfe9c3d6c5`. Although untested, this might also work for #39202. ## Test Result Start the `vllm serve` successful, and crash with error `RuntimeError: The size of tens |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
