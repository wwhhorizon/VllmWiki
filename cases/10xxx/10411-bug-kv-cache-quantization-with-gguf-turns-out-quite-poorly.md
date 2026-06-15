# vllm-project/vllm#10411: [Bug]: KV Cache Quantization with GGUF turns out quite poorly.

| 字段 | 值 |
| --- | --- |
| Issue | [#10411](https://github.com/vllm-project/vllm/issues/10411) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV Cache Quantization with GGUF turns out quite poorly.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run --runtime nvidia --gpus all ` >> -v "D:\AIModels:/models" ` >> -p 8000:8000 ` >> --ipc=host ` >> -e VLLM_ATTENTION_BACKEND=FLASHINFER ` >> vllm/vllm-openai:latest ` >> --model "/models/MaziyarPanahi/Qwen2.5-7B-Instruct-abliterated-v2-GGUF/Qwen2.5-7B-Instruct-abliterated-v2.Q5_K_M.gguf" ` >> --tokenizer "Qwen/Qwen2.5-7B-Instruct" ` >> --kv-cache-dtype fp8_e4m3 ``` I've tried both fp8_e5m2 and fp8_e4m3. The model works perfectly without kv-cache quantization. When I enable it, the model gets exceptionally bad. With e5m2 it just repeats a word over and over. With e4m3 it gets about half a sentence in, then also repeats over forever. I can understand perhaps a some loss in precision, but not basically 100%. It's essentially non-functional with the FP8 kv-cache. Without the quantized cache the model is on the level of GPT-3.5. I had read that there shouldn't be much difference between the two, so I though perhaps it wasn't working right because it's a GGUF or something to do with that. Here are the init logs: ``` PS D:\AITools\vllm> docker run --runtime nvidia --gpus all ` >> -v "D:\A...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: KV Cache Quantization with GGUF turns out quite poorly. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run --runtime nvidia --gpus all ` >> -v "D:\AIM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: t ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run --runtime nvidia --gpus all ` >> -v "D:\AIModels:/models" ` >> -p 8000:8000 ` >> --ipc=host ` >> -e VLLM_ATTENTION_BACKEND=FLASHINFER ` >> vllm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: KV Cache Quantization with GGUF turns out quite poorly. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run --runtime nvidia --gpus all ` >> -v "D:\AIM...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: [Bug]: KV Cache Quantization with GGUF turns out quite poorly. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run --runtime nvidia --gpus all ` >> -v "D:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: F turns out quite poorly. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` docker run --runtime nvidia --gpus all ` >> -v "D:\AIModels:/models" ` >> -p 8000:8000 ` >>...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
