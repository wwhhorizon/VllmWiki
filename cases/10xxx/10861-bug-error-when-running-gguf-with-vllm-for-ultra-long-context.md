# vllm-project/vllm#10861: [Bug]: Error When Running gguf with vllm for Ultra-Long Context

| 字段 | 值 |
| --- | --- |
| Issue | [#10861](https://github.com/vllm-project/vllm/issues/10861) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error When Running gguf with vllm for Ultra-Long Context

### Issue 正文摘录

### Your current environment ### Model Input Dumps [error-log.txt](https://github.com/user-attachments/files/17992286/error-log.txt) ### 🐛 Describe the bug I want to run gguf with vllm for ultra-long context, setting `--kv-cache-dtype=fp8` and `--tensor-parallel-size=2`. The model supports 512k context, but when I set `--max-model-len=280000`, it throws an error. The log is attached above, and the error message is `ERROR 12-03 03:28:37 engine.py:135] assert builder.options.allow_fp8e4nv, "fp8e4nv data type is not supported on CUDA arch < 89"`. It runs fine when the context is set to 20000. ``` docker run --rm ` --gpus all ` -v /d/workspace/text-generation-webui/models:/opt/models ` -e "HF_ENDPOINT=https://hf-mirror.com" ` -p 5000:8000 ` --ipc=host ` vllm/vllm-openai:v0.6.4.post1 ` --gpu-memory-utilization=0.99 ` --tensor-parallel-size=2 ` --served-model=gpt-4 ` --max-model-len=280000 ` --host=0.0.0.0 ` --port=8000 ` --kv-cache-dtype=fp8 ` --quantization=gguf ` --tokenizer=princeton-nlp/Llama-3-8B-ProLong-512k-Instruct ` --model=/opt/models/princeton-nlp.Llama-3-8B-ProLong-512k-Instruct.Q8_0.gguf ``` ### Before submitting a new issue... - [X] Make sure you already searched for rele...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: and the error message is `ERROR 12-03 03:28:37 engine.py:135] assert builder.options.allow_fp8e4nv, "fp8e4nv data type is not supported on CUDA arch < 89"`. It runs fine when the context is set to 20000. ``` docker run...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: I want to run gguf with vllm for ultra-long context, setting `--kv-cache-dtype=fp8` and `--tensor-parallel-size=2`. The model supports 512k context, but when I set `--max-model-len=280000`, it throws an error. The log i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ith vllm for Ultra-Long Context bug ### Your current environment ### Model Input Dumps [error-log.txt](https://github.com/user-attachments/files/17992286/error-log.txt) ### 🐛 Describe the bug I want to run gguf with vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt builder.options.allow_fp8e4nv, "fp8e4nv data type is not supported on CUDA arch < 89"`. It runs fine when the context is set to 20000. ``` docker run --rm ` --gpus all ` -v /d/workspace/text-generation-webui/models:/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
