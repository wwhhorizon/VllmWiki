# vllm-project/vllm#10182: [Feature]: Error launching model gemma-2-27b-it-fp8-dynamic-rope: Disabling sliding window is not supported for models with rope_scaling. Please raise an issue so we can investigate.

| 字段 | 值 |
| --- | --- |
| Issue | [#10182](https://github.com/vllm-project/vllm/issues/10182) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Error launching model gemma-2-27b-it-fp8-dynamic-rope: Disabling sliding window is not supported for models with rope_scaling. Please raise an issue so we can investigate.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am setting up the inference for the model https://huggingface.co/CalamitousFelicitousness/gemma-2-27b-it-fp8-dynamic-rope CUDA_VISIBLE_DEVICES=1 VLLM_LOGGING_LEVEL=DEBUG python -m vllm.entrypoints.openai.api_server --host ... --port **** --model /data/models/gemma-2-27b-it-fp8-dynamic-rope --trust-remote-code --served-model-name gemma-2-27b-it-fp8-dynamic-rope --gpu_memory_utilization 0.9 --max-model-len 16384 --enable-prefix-caching --kv-cache-dtype fp8_e5m2 --quantization fp8 But I am getting the following error: INFO 11-09 14:37:47 config.py:107] Replacing legacy 'type' key with 'rope_type' WARNING 11-09 14:37:47 config.py:185] gemma2 has interleaved attention, which is currently not supported by vLLM. Disabling sliding window and capping the max length to the sliding window size (4096). Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/data/venvs/vllm/lib/python3.12/site-p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Error launching model gemma-2-27b-it-fp8-dynamic-rope: Disabling sliding window is not supported for models with rope_scaling. Please raise an issue so we can investigate. feature request;stale ### Your curre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ting up the inference for the model https://huggingface.co/CalamitousFelicitousness/gemma-2-27b-it-fp8-dynamic-rope CUDA_VISIBLE_DEVICES=1 VLLM_LOGGING_LEVEL=DEBUG python -m vllm.entrypoints.openai.api_server --host ......
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Error launching model gemma-2-27b-it-fp8-dynamic-rope: Disabling sliding window is not supported for models with rope_scaling. Please raise an issue so we can investigate. feature request;stale ### Your curre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: with rope_scaling. Please raise an issue so we can investigate. feature request;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am setting up the inference for the model h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /huggingface.co/CalamitousFelicitousness/gemma-2-27b-it-fp8-dynamic-rope CUDA_VISIBLE_DEVICES=1 VLLM_LOGGING_LEVEL=DEBUG python -m vllm.entrypoints.openai.api_server --host ... --port **** --model /data/models/gemma-2-2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
