# vllm-project/vllm#12581: [Bug]: AssertionError: fp8e4nv data type is not supported on CUDA arch < 89 (attempting to serve DeepSeek R1)

| 字段 | 值 |
| --- | --- |
| Issue | [#12581](https://github.com/vllm-project/vllm/issues/12581) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError: fp8e4nv data type is not supported on CUDA arch < 89 (attempting to serve DeepSeek R1)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Summary I'm trying to serve the DeepSeek R1 model via vLLM. From what I can tell, this should be supported (it's confirmed in https://github.com/vllm-project/vllm/issues/12226 and in the DeepSeek R1 huggingface model card [https://huggingface.co/deepseek-ai/DeepSeek-R1]). However, when I try to run the model, I get the following error: `AssertionError: fp8e4nv data type is not supported on CUDA arch < 89`. This happens after loading all checkpoint shards. I've tried the following commands, all without success. 1. `vllm serve deepseek-ai/DeepSeek-R1 --tensor-parallel-size 8 --enforce-eager --trust-remote-code --cpu-offload-gb 128 --max-model-len 4096` 2. `vllm serve deepseek-ai/DeepSeek-R1 --tensor-parallel-size 8 --enforce-eager --trust-remote-code --cpu-offload-gb 128 --enable-chunked-prefill=False` 3. `FLASH_ATTN=0 vllm serve deepseek-ai/DeepSeek-R1 --tensor-parallel-size 8 --enforce-eager --trust-remote-code --cpu-offload-gb 128 --enable-chunked-prefill=False` 4. `vllm serve deepseek-ai/DeepSeek-R1 --tensor-parallel-size 8 --enforce-eager --trust-remote-code --cpu-offload-gb 128 --enable...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: AssertionError: fp8e4nv data type is not supported on CUDA arch < 89 (attempting to serve DeepSeek R1) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Summary I'm t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ROR 01-30 16:32:24 engine.py:387] return semantic.cast(self, dtype, _builder, fp_downcast_rounding) ERROR 01-30 16:32:24 engine.py:387] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: AssertionError: fp8e4nv data type is not supported on CUDA arch < 89 (attempting to serve DeepSeek R1) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Summary I'm t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ttempting to serve DeepSeek R1) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Summary I'm trying to serve the DeepSeek R1 model via vLLM. From what I can tell, this shou...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: engine.py:387] File "/home/ubuntu/*/.venv/lib/python3.12/site-packages/triton/language/core.py", line 35, in wrapper ERROR 01-30 16:32:24 engine.py:387] return fn(*args, **kwargs) ERROR 01-30 16:32:24 engine.py:387] ^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
