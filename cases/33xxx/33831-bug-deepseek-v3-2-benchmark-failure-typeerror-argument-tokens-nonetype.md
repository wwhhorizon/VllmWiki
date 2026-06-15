# vllm-project/vllm#33831: [Bug]: Deepseek V3.2 Benchmark failure "TypeError: argument 'tokens': 'NoneType' object"

| 字段 | 值 |
| --- | --- |
| Issue | [#33831](https://github.com/vllm-project/vllm/issues/33831) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek V3.2 Benchmark failure "TypeError: argument 'tokens': 'NoneType' object"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Benchmarking Deepseek v3.2 throws error: ``` vllm serve deepseek-ai/DeepSeek-V3.2 \ -tp 8 \ --tokenizer-mode deepseek_v32 \ --load-format dummy ``` ``` vllm bench serve \ --model deepseek-ai/DeepSeek-V3.2 \ --dataset-name random \ --random-input 1024 \ --random-output 8192 \ --num-prompt 5 \ --max-concurrency 1 \ --trust-remote-code ``` Error: ``` Traceback (most recent call last): [async_llm.py:687] File "vllm/vllm/v1/engine/async_llm.py", line 658, in output_handler [async_llm.py:687] processed_outputs = output_processor.process_outputs( [async_llm.py:687] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [async_llm.py:687] File "vllm/vllm/v1/engine/output_processor.py", line 632, in process_outputs [async_llm.py:687] stop_string = req_state.detokenizer.update( [async_llm.py:687] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [async_llm.py:687] File "vllm/vllm/v1/engine/detokenizer.py", line 120, in update [async_llm.py:687] self.output_text += self.decode_next(new_token_id) [async_llm.py:687] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [async_llm.py:687] File "vllm/vllm/v1/engine/detokenizer.py", line 299, in decode_next [async_llm.py:687] new_tokens, decoded_text, prefix...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pt to demonstrate the None output: ``` from vllm.tokenizers.deepseek_v32 import DeepseekV32Tokenizer tokenizer = DeepseekV32Tokenizer.from_pretrained( path_or_repo_id="deepseek-ai/DeepSeek-V3.2", trust_remote_code=True,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: t.py", line 666, in convert_tokens_to_string [async_llm.py:687] self.backend_tokenizer.decoder.decode(tokens) [async_llm.py:687] TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString' ``` Scri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: em. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: epSeek-V3.2 \ -tp 8 \ --tokenizer-mode deepseek_v32 \ --load-format dummy ``` ``` vllm bench serve \ --model deepseek-ai/DeepSeek-V3.2 \ --dataset-name random \ --random-input 1024 \ --random-output 8192 \ --num-prompt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: py", line 120, in update [async_llm.py:687] self.output_text += self.decode_next(new_token_id) [async_llm.py:687] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [async_llm.py:687] File "vllm/vllm/v1/engine/detokenizer.py", line 299, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
