# vllm-project/vllm#38818: [Bug]: Error when running Devstral Small 2 with HF format

| 字段 | 值 |
| --- | --- |
| Issue | [#38818](https://github.com/vllm-project/vllm/issues/38818) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when running Devstral Small 2 with HF format

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I recently encountered an issue after downloading Devstral Small 2 (https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512). I can run the model with no problem when it uses Mistral format files (```params.json```, ```consolidated.safetensors``` and ```tekken.json```) when running the following command : ``` vllm serve /root/.cache/huggingface/devstral-small-2 --port 8080 --host 0.0.0.0 --gpu-memory-utilization 0.7 --served-model-name devstral --max-model-len 262144 --enable-auto-tool-choice --tool-call-parser mistral ``` However, it crashes when I try to use the HF format files with the same command (I simply removed the previous files out of the model folder), with the following error : ``` (EngineCore pid=149) ERROR 04-02 12:18:35 [core.py:1108] EngineCore failed to start. (EngineCore pid=149) ERROR 04-02 12:18:35 [core.py:1108] Traceback (most recent call last): (EngineCore pid=149) ERROR 04-02 12:18:35 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1082, in run_engine_core (EngineCore pid=149) ERROR 04-02 12:18:35 [core.py:1108] engine_core = EngineCoreProc(*args, engi...

## 现有链接修复摘要

#39293 [Bugfix][Model] Fix Devstral Small 2 HF format weight loading

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Error when running Devstral Small 2 with HF format bug ### Your current environment ### 🐛 Describe the bug I recently encountered an issue after downloading Devstral Small 2 (https://huggingface.co/mistralai/Devs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 5 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=149) ERROR 04-02 12:18:35 [core.py:1108] return func(*args, **kwargs) (EngineCore pid=149)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: l;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding activation;cuda;fp8;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency #392...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Error when running Devstral Small 2 with HF format bug ### Your current environment ### 🐛 Describe the bug I recently encountered an issue after downloading Devstral Small 2 (https://huggingface.co/mistralai/Devs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: m/entrypoints/cli/main.py", line 75, in main (APIServer pid=71) args.dispatch_function(args) (APIServer pid=71) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 122, in cmd (APIServer p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39293](https://github.com/vllm-project/vllm/pull/39293) | closes_keyword | 0.95 | [Bugfix][Model] Fix Devstral Small 2 HF format weight loading | Fixes #38818 ## Test plan - [x] Verified FP8 scale values are identical between native (`qscale_weight`/`qscale_act`) and HF (`weight_scale_inv`/`activation_scale`) formats by co |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
