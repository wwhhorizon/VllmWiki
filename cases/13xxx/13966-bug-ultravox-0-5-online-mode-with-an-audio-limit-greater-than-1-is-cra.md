# vllm-project/vllm#13966: [Bug]: Ultravox 0.5 online mode with an audio limit greater than 1 is crashing

| 字段 | 值 |
| --- | --- |
| Issue | [#13966](https://github.com/vllm-project/vllm/issues/13966) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ultravox 0.5 online mode with an audio limit greater than 1 is crashing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, The command `vllm serve fixie-ai/ultravox-v0_5-llama-3_1-8b --tensor-parallel-size 1 --max-model-len 8012 --trust-remote-code --limit-mm-per-prompt "audio=20"` is crashing with the following error: ``` ERROR 02-27 14:01:03 engine.py:400] File "/home/ubuntu/miniconda3/envs/vllm_temp/lib/python3.11/site-packages/vllm/inputs/registry.py", line 172, in call_hf_processor ERROR 02-27 14:01:03 engine.py:400] raise RuntimeError(msg) from exc ERROR 02-27 14:01:03 engine.py:400] RuntimeError: Failed to apply UltravoxProcessor on data={'text': ' ', 'audio': array([0., 0., 0., ..., 0., 0., 0.])} with kwargs={'sampling_rate': 16000} Process SpawnProcess-1: Traceback (most recent call last): File "/home/ubuntu/miniconda3/envs/vllm_temp/lib/python3.11/site-packages/vllm/inputs/registry.py", line 167, in call_hf_processor return hf_processor(**data, **merged_kwargs, return_tensors="pt") ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ubuntu/.cache/huggingface/modules/transformers_modules/fixie-ai/ultravox-v0_5-llama-3_1-8b/779bcda5ad4b7ed18fd0a37f065a564ca18efa31/ultravox_processing.py", line 349, in __call__ raise Val...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 🐛 Describe the bug Hi, The command `vllm serve fixie-ai/ultravox-v0_5-llama-3_1-8b --tensor-parallel-size 1 --max-model-len 8012 --trust-remote-code --limit-mm-per-prompt "audio=20"` is crashing with the following error...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: re aren't any issues with multiple audios whereas with vllm, I'm above facing error. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /fixie-ai/ultravox-v0_5-llama-3_1-8b/779bcda5ad4b7ed18fd0a37f065a564ca18efa31/ultravox_processing.py", line 349, in __call__ raise ValueError( ValueError: Text contains too many audio placeholders. (Expected 1 placehold...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;gemm;operator;quantization;sampling;triton build_error;crash;nan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
