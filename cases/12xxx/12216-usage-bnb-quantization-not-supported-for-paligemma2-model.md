# vllm-project/vllm#12216: [Usage]: BNB quantization not supported for Paligemma2 model

| 字段 | 值 |
| --- | --- |
| Issue | [#12216](https://github.com/vllm-project/vllm/issues/12216) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | attention;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: BNB quantization not supported for Paligemma2 model

### Issue 正文摘录

### Your current environment ```text The output of `docker run --runtime nvidia --gpus all -v /path/to/models:/data/vllm.model --env "HUGGING_FACE_HUB_TOKEN=hf_token" -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model /path/to/model/dir/paligemma2-28b-pt-896 --quantization bitsandbytes --load-format bitsandbytes --served-model-name paligemma2-28b --max-model-len 8192 --distributed-executor-backend mp --tensor-parallel-size 2 ` ``` I adjusted some code to use quantization 4bit bitsandbytes based on model repo and tested in jupyter notebook without problem but i get this error when running with vllm https://huggingface.co/google/paligemma2-28b-pt-896 https://huggingface.co/blog/paligemma2 ``` (VllmWorkerProcess pid=70) INFO 01-20 01:25:05 selector.py:217] Cannot use FlashAttention-2 backend for Volta and Turing GPU s. (VllmWorkerProcess pid=70) INFO 01-20 01:25:05 selector.py:129] Using XFormers backend. ERROR 01-20 01:25:05 engine.py:366] Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla V 100-PCIE-32GB GPU has compute capability 7.0. You can use float16 instead by explicitly setting the`dtype` flag in CLI, for example: --dtype=half. ERROR...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: BNB quantization not supported for Paligemma2 model usage ### Your current environment ```text The output of `docker run --runtime nvidia --gpus all -v /path/to/models:/data/vllm.model --env "HUGGING_FACE_HUB_T...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: igemma2 model usage ### Your current environment ```text The output of `docker run --runtime nvidia --gpus all -v /path/to/models:/data/vllm.model --env "HUGGING_FACE_HUB_TOKEN=hf_token" -p 8000:8000 --ipc=host vllm/vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: BNB quantization not supported for Paligemma2 model usage ### Your current environment ```text The output of `docker run --runtime nvidia --gpus all -v /path/to/models:/data/vllm.model --env "HUGGING_FACE_HUB_T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -name paligemma2-28b --max-model-len 8192 --distributed-executor-backend mp --tensor-parallel-size 2 ` ``` I adjusted some code to use quantization 4bit bitsandbytes based on model repo and tested in jupyter notebook wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 01:25:05 engine.py:366] Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla V 100-PCIE-32GB GPU has compute capability 7.0. You can use float16 instead by explicitly setting the`dtype`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
