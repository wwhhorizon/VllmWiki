# vllm-project/vllm#13071: [Bug]: ValueError: Attempted to assign 72 + 72 + 72 + 72 + 72 + 72 = 432 multimodal tokens to 360 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#13071](https://github.com/vllm-project/vllm/issues/13071) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Attempted to assign 72 + 72 + 72 + 72 + 72 + 72 = 432 multimodal tokens to 360 placeholders

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ValueError: Attempted to assign 72 + 72 + 72 + 72 + 72 + 72 = 432 multimodal tokens to 360 placeholders ```shell nohup vllm serve /root/.cache/huggingface/Qwen/Qwen2.5-VL-72B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --dtype bfloat16 \ --limit-mm-per-prompt image=2,video=0 \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --served-model-name WestGenesis-LLM \ --gpu_memory_utilization 0.95 \ --max-model-len 65536 \ --max-num-seqs 16 \ --enable-chunked-prefill \ --max-num-batched-tokens 65536 \ --enable-auto-tool-choice --tool-call-parser hermes \ > vllm.log 2>&1 & ``` INFO 02-10 17:49:55 async_llm_engine.py:211] Added request chatcmpl-4aaa19dfd9b046cfa441c0ada91d9191. INFO 02-10 17:49:55 logger.py:39] Received request chatcmpl-e03d4f81b9a9469e92a5016945a8b68b: prompt: ' system\nYou are a helpful assistant. \n user\n \nBased on the following context, analyze this vehicle system icon and provide ONLY a JSON response:\n\nContext:\n- Caption: icon: btn_ic_defrost\n- Resource ID: com.omosoft.hvac:id/btn_ic_defrost\n- XML Info: {\'NAF\': \'true\', \'index\': \'3\', \'text\': \'\', \'resource-id\': \'com.omosoft.hvac:id/btn_ic_de...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: ValueError: Attempted to assign 72 + 72 + 72 + 72 + 72 + 72 = 432 multimodal tokens to 360 placeholders bug ### Your current environment ### 🐛 Describe the bug ValueError: Attempted to assign 72 + 72 + 72 + 72 +...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: --max-model-len 65536 \ --max-num-seqs 16 \ --enable-chunked-prefill \ --max-num-batched-tokens 65536 \ --enable-auto-tool-choice --tool-call-parser hermes \ > vllm.log 2>&1 & ``` INFO 02-10 17:49:55 async_llm_engine.py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tokens=65247, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: No...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: n/Qwen2.5-VL-72B-Instruct \ --port 8000 \ --host 0.0.0.0 \ --dtype bfloat16 \ --limit-mm-per-prompt image=2,video=0 \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --served-model-name WestGenesis-LLM \ --gpu_m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
