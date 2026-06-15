# vllm-project/vllm#16061: [Bug]: KeyError: 'local_attn_masks' on running gemma3 models with kv-cache quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#16061](https://github.com/vllm-project/vllm/issues/16061) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'local_attn_masks' on running gemma3 models with kv-cache quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tried running `gemma3:12b` with vllm docker using `fp8_e5m2` kv-cache quantization and got error `KeyError: 'local_attn_masks'`. > Exact command used: `docker run --rm -it --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p "8000:8000" --ipc=host vllm/vllm-openai:latest --model gaunernst/gemma-3-12b-it-int4-awq --quantization awq_marlin --trust-remote-code --dtype bfloat16 --kv-cache-dtype fp8_e5m2 --max-model-len 4096 --served-model-name gemma3-12b --enable-sleep-mode --enable-chunked-prefill --enable-prefix-caching --max-log-len 400 --tokenizer-pool-size 8 -O 3 --gpu-memory-utilization 0.95` this happens with options `fp8` and `fp8_e4m3` as well. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ug]: KeyError: 'local_attn_masks' on running gemma3 models with kv-cache quantization bug;stale ### Your current environment ### 🐛 Describe the bug Tried running `gemma3:12b` with vllm docker using `fp8_e5m2` kv-cache q...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ronment ### 🐛 Describe the bug Tried running `gemma3:12b` with vllm docker using `fp8_e5m2` kv-cache quantization and got error `KeyError: 'local_attn_masks'`. > Exact command used: `docker run --rm -it --gpus all -v ~/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: KeyError: 'local_attn_masks' on running gemma3 models with kv-cache quantization bug;stale ### Your current environment ### 🐛 Describe the bug Tried running `gemma3:12b` with vllm docker using `fp8_e5m2` kv-cache...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ocal_attn_masks' on running gemma3 models with kv-cache quantization bug;stale ### Your current environment ### 🐛 Describe the bug Tried running `gemma3:12b` with vllm docker using `fp8_e5m2` kv-cache quantization and g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
