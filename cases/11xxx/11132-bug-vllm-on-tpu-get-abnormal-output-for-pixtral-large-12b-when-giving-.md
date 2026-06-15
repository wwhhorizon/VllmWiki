# vllm-project/vllm#11132: [Bug]: vLLM on TPU get abnormal output for pixtral-large/12B when giving input with image.

| 字段 | 值 |
| --- | --- |
| Issue | [#11132](https://github.com/vllm-project/vllm/issues/11132) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM on TPU get abnormal output for pixtral-large/12B when giving input with image.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Abnormal output from both `mistralai/Pixtral-Large-Instruct-2411` & `mistralai/Pixtral-12B-2409` with **multimodal input** backed by **vLLM+TPU**(v5p-8) only. **It works fine on vLLM+GPU(H100)**. I installed vLLM on TPU following this [official documentation](https://docs.vllm.ai/en/latest/getting_started/tpu-installation.html) I also tried [v0.6.4.post1](https://github.com/vllm-project/vllm/releases/tag/v0.6.4.post1), but get the same outcome. I started the serving using, ``` vllm serve mistralai/Pixtral-Large-Instruct-2411 --config-format mistral --load-format mistral --tokenizer-mode mistral --max-model-len=8192 --limit_mm_per_prompt 'image=10' --tensor-parallel-size 4 --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --dtype=bfloat16 ``` Below script for reproduction was drafted according to the [official example](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411). ```python import requests import json from huggingface_hub import hf_hub_download from datetime import datetime, timedelta url = "http://localhost:8000/v1/chat/completions" headers = {"Content-Type": "appl...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: abnormal output for pixtral-large/12B when giving input with image. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Abnormal output from both `mistralai/Pixtral-Large-In...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ked by **vLLM+TPU**(v5p-8) only. **It works fine on vLLM+GPU(H100)**. I installed vLLM on TPU following this [official documentation](https://docs.vllm.ai/en/latest/getting_started/tpu-installation.html) I also tried [v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: giving input with image. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Abnormal output from both `mistralai/Pixtral-Large-Instruct-2411` & `mistralai/Pixtral-12B-2409`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -size 4 --num-scheduler-steps 4 --swap-space 16 --disable-log-requests --dtype=bfloat16 ``` Below script for reproduction was drafted according to the [official example](https://huggingface.co/mistralai/Pixtral-Large-In...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: input** backed by **vLLM+TPU**(v5p-8) only. **It works fine on vLLM+GPU(H100)**. I installed vLLM on TPU following this [official documentation](https://docs.vllm.ai/en/latest/getting_started/tpu-installation.html) I al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
